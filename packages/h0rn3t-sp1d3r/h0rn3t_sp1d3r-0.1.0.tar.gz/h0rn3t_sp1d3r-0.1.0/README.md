# h0rnet

A small Python package to scan WordPress sites for suspicious/backdoor paths.
**Only use on systems you own or have explicit permission to test.**

## Quick start

1. Create a newline-separated file `targets.txt` with hostnames or URLs (e.g. `example.com` or `http://example.com`).
2. Run:

```bash
python -m h0rn3t targets.txt
```

3. Positive matches are appended to `BADS-OK.txt`.

## Notes
- Customize `DEFAULT_PATHS` in `h0rn3t/core.py`.
- Respect target's rules and legal constraints.
