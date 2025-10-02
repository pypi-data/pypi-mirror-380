# @h0rn3t_sp1d3r  - tg id
import requests
import threading
from colorama import Fore
from colorama import init
init(autoreset=True)
fr = Fore.RED
fw = Fore.WHITE
fg = Fore.GREEN
    
class VulnScanner:
    def init(self, sites_file, paths, check_texts, threads=10, output_file="BADS_OK.txt"):
        self.sites = self.load_sites(sites_file)
        self.paths = paths
        self.check_texts = check_texts
        self.threads = threads
        self.output_file = output_file
        self.lock = threading.Lock()

    def load_sites(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f" File not found: {filename}")
            return []

    def check_site(self, site, path):
        url = site.rstrip("/") + "/" + path.lstrip("/")
        try:
            r = requests.get(url, timeout=5)
            found = False

            for text in self.check_texts:
                if text in r.text:
                    found = True
                    print(f" BADS : {url} {fg}--> VULN")
                    with self.lock:
                        with open(self.output_file, "a") as f:
                            f.write(f"{url}\n")
                    break

            if not found:
                print(f" BADS : {url} {fr}--> NO")

        except Exception as e:
            print(f" BADS : {url} {fr}--> NO")

    def run(self):
        threads_list = []
        for site in self.sites:
            for path in self.paths:
                t = threading.Thread(target=self.check_site, args=(site, path))
                threads_list.append(t)
                t.start()
                if len(threads_list) >= self.threads:
                    for th in threads_list:
                        th.join()
                    threads_list = []