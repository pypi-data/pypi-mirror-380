# core.py
"""
Improved core for h0rn3t package.

Fixes & improvements:
 - session with retries
 - proper URL normalization and joining using urllib.parse
 - response size limiting (prevent huge downloads)
 - safer output file handling (basename only)
 - clearer exception handling and rate-limited concurrency
 - only flags when indicator strings are found in a limited-size snippet
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Iterable, List
from urllib.parse import urlparse, urljoin
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os

# Default suspicious paths to check (customize carefully)
DEFAULT_PATHS = ["wp-content/plugins/phpad/as.php"]

# Indicators that mark potential backdoor output
DEFAULT_INDICATORS = ["Uname:", "phpinfo("]

# Limits
MAX_RESPONSE_BYTES = 200 * 1024  # 200 KB (don't download huge bodies)
SNIPPET_LENGTH = 1000  # how many chars to keep for inspection
DEFAULT_WORKERS = 20
DEFAULT_TIMEOUT = 10  # seconds


def _make_session(total_retries: int = 2, backoff_factor: float = 0.3, status_forcelist=(429, 500, 502, 503, 504)):
    """
    Create a requests.Session with retry strategy.
    """
    session = requests.Session()
    retries = Retry(
        total=total_retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        allowed_methods=frozenset(["GET", "HEAD", "OPTIONS"])
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"})
    return session


def _is_valid_target(value: str) -> bool:
    """
    Basic validation for target host/URL.
    Accepts hostnames or full http(s) URLs.
    Rejects empty and obviously malicious/unsupported schemes.
    """
    if not value or not value.strip():
        return False
    v = value.strip()
    # If user provided a scheme, ensure it's http or https
    if v.startswith(("http://", "https://")):
        p = urlparse(v)
        return p.scheme in ("http", "https") and p.netloc != ""
    # If no scheme, check it's a plausible hostname (no spaces, no slashes)
    if " " in v or "/" in v:
        return False
    return True


def normalize_base_url(site: str) -> str:
    """
    Normalize to a base URL with http:// if missing and ensure trailing slash.
    Uses urlparse/urljoin to avoid simple string bugs.
    """
    s = site.strip()
    if not s:
        raise ValueError("empty hostname")
    if not s.startswith(("http://", "https://")):
        s = "http://" + s
    p = urlparse(s)
    if p.scheme not in ("http", "https") or not p.netloc:
        raise ValueError("invalid URL/host")
    base = f"{p.scheme}://{p.netloc}/"
    return base


def _safe_join(base: str, path: str) -> str:
    """
    Safely join base URL and path using urljoin.
    Ensures no scheme-switching or removal of base.
    """
    candidate = urljoin(base, path.lstrip("/"))
    # ensure candidate still under same netloc as base
    if urlparse(candidate).netloc != urlparse(base).netloc:
        raise ValueError("joined URL left target host")
    return candidate


def _read_limited(resp: requests.Response, max_bytes: int) -> str:
    """
    Read up to max_bytes from response (streaming) and return text (decoded).
    Protects from giant bodies.
    """
    try:
        chunks = []
        total = 0
        for chunk in resp.iter_content(chunk_size=4096, decode_unicode=False):
            if chunk is None:
                break
            total += len(chunk)
            if total > max_bytes:
                # stop reading more
                chunks.append(chunk[: max(0, max_bytes - (total - len(chunk)))])
                break
            chunks.append(chunk)
        data = b"".join(chunks)
        # try to decode as utf-8 (fallback latin-1)
        try:
            return data.decode("utf-8", errors="replace")
        except Exception:
            return data.decode("latin-1", errors="replace")
    except Exception:
        return ""


def check_path(session: requests.Session, base_url: str, path: str, timeout: int = DEFAULT_TIMEOUT) -> dict:
    """
    Check a single path on a base URL. Returns dict with status and limited snippet or error.
    """
    try:
        full = _safe_join(base_url, path)
    except Exception as e:
        return {"url": None, "error": f"join_error: {e}"}

    try:
        # stream=True so we can limit how much we download
        r = session.get(full, timeout=timeout, stream=True, allow_redirects=True, verify=True)
        snippet = _read_limited(r, MAX_RESPONSE_BYTES)
        if len(snippet) > SNIPPET_LENGTH:
            snippet = snippet[:SNIPPET_LENGTH]
        return {"url": full, "status_code": getattr(r, "status_code", None), "text_snippet": snippet}
    except requests.exceptions.RequestException as e:
        return {"url": full, "error": f"request_error: "}
    except Exception as e:
        return {"url": full, "error": f"unknown_error: "}


def _is_positive(snippet: str, indicators: Iterable[str]) -> bool:
    """
    Decide whether the response snippet indicates a possible backdoor.
    Case-insensitive search of indicators.
    """
    if not snippet:
        return False
    low = snippet.lower()
    for ind in indicators:
        if ind.lower() in low:
            return True
    return False


def scan_target(site: str, paths: Iterable[str] = None, indicators: Iterable[str] = None, timeout: int = DEFAULT_TIMEOUT) -> List[dict]:
    """
    Scan a single site for provided paths. Returns list of result dicts (positives and negatives).
    """
    if paths is None:
        paths = DEFAULT_PATHS
    if indicators is None:
        indicators = DEFAULT_INDICATORS

    if not _is_valid_target(site):
        return []

    base = normalize_base_url(site)
    session = _make_session()

    results = []
    for path in paths:
        # basic sanity: path should not be too long
        if not path or len(path) > 400:
            results.append({"url": None, "error": "invalid_path"})
            continue
        res = check_path(session, base, path, timeout=timeout)
        results.append(res)
    return results


def scan_file_list(filename: str, paths: Iterable[str] = None, indicators: Iterable[str] = None,
                   workers: int = DEFAULT_WORKERS, timeout: int = DEFAULT_TIMEOUT, out_filename: str = "BADS-OK.txt") -> List[dict]:
    """
    Read newline-separated targets from filename and scan using a thread pool.
    Returns list of positive findings. Writes matches to out_filename (basename only).
    """
    if paths is None:
        paths = DEFAULT_PATHS
    if indicators is None:
        indicators = DEFAULT_INDICATORS

    # ensure out_filename is not a path-traversal value; use basename only
    out_basename = os.path.basename(out_filename) or "BADS-OK.txt"

    try:
        with open(filename, "r", encoding="utf-8") as fh:
            sites = [line.strip() for line in fh if line.strip()]
    except FileNotFoundError:
        raise

    findings = []

    def worker(site):
        try:
            res_list = scan_target(site, paths=paths, indicators=indicators, timeout=timeout)
            pos = []
            for r in res_list:
                if r.get("error"):
                    continue
                snippet = r.get("text_snippet", "")
                if _is_positive(snippet, indicators):
                    pos.append(r)
            return pos
        except Exception:
            return []

    # limit number of workers to reasonable bounds
    workers = max(1, min(100, int(workers)))

    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(worker, s): s for s in sites}
        for fut in as_completed(futures):
            try:
                pos_list = fut.result()
                for p in pos_list:
                    findings.append(p)
            except Exception:
                # ignore single-thread failure
                pass

    # append results to file (one URL per line)
    if findings:
        try:
            with open(out_basename, "a", encoding="utf-8") as outfh:
                for f in findings:
                    url = f.get("url")
                    if url:
                        outfh.write(url + "\n")
        except Exception:
            # fail silently for file errors to avoid crashing scans
            pass

    return findings


def run_cli():
    """
    Simple CLI entrypoint to run as `python -m h0rnet targets.txt`.
    """
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m h0rnet <targets-file>")
        return
    filename = sys.argv[1]
    try:
        findings = scan_file_list(filename)
        print(f"Scan complete. {len(findings)} findings.")
        for f in findings:
            print("FOUND:", f.get("url"))
    except FileNotFoundError:
        print("[!] File not found")
    except Exception as e:
        print("[!] Error:")


if __name__ == "__main__":
    run_cli()
