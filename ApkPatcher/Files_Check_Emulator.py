from .C_M import CM
C = CM()
class F_C_E:
    # Full path to jar & other
    def set_paths(self):
        script_dir = C.os.path.dirname(C.os.path.abspath(C.sys.argv[0]))
        self.apktool_path = C.os.path.join(script_dir, "APKTool_OR.jar")

    # Function to download files
    def download_file(self, jar_urls_and_paths, isEmulator):
        import requests
        downloaded_urls = set()
        for file_url, local_path in jar_urls_and_paths:
            lo_path = C.os.path.basename(local_path)
            if C.os.path.exists(local_path) or file_url in downloaded_urls:
                continue
            try:
                print(f"{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{lo_path}", end='', flush=True)
                response = requests.get(file_url, stream=True, timeout=10)

                if response.status_code == 200:
                    total_size = int(response.headers.get('content-length', 0))
                    block_size = 1024
                    downloaded = 0
                    with open(local_path, 'wb') as f:
                        for data in response.iter_content(block_size):
                            downloaded += len(data)
                            f.write(data)
                            progress = downloaded / total_size * 100 if total_size > 0 else 0
                            mb_downloaded = downloaded / (1024 * 1024)
                            total_mb = total_size / (1024 * 1024) if total_size > 0 else 0
                            progress_line = f"\r{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{lo_path}{C.g} ➸❥  {progress:.2f}% ({mb_downloaded:.2f}/{total_mb:.2f} MB)"
                            print(progress_line, end='\r')
                    print(f"\n{C.g}       |\n       └──── {C.r}Downloaded ~{C.g}$ {lo_path} Successfully. ✔\n")
                else:
                    exit(f'\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Failed to download {C.y}{lo_path} {C.rd}Status Code: {response.status_code}\n\n{C.lb}[ {C.rd}INFO {C.lb}]{C.rd} Restart Script...{C.r}\n')
            except requests.exceptions.RequestException:
                exit(f'\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Got an error while Fetching {C.y}{local_path}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No internet Connection\n\n{C.lb}[ {C.rd}INFO {C.lb}]{C.rd} Internet connection is required to download {C.y}{lo_path}\n')

    def F_D(self, isEmulator):
        jar_urls_and_paths = []
        if isEmulator:
            jar_urls_and_paths = [
                (("https://github.com/TechnoIndian/RKPairip/releases/download/Editor/apktool.jar"), self.apktool_path)
            ]
        else:
            pass
        self.download_file(jar_urls_and_paths, isEmulator)