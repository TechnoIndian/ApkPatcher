from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from importlib.metadata import version

__version__ = version("ApkPatcherX")


# ---------------- Set Path ----------------
run_dir = M.os.path.dirname(M.os.path.abspath(M.sys.argv[0]))
script_dir = M.os.path.dirname(M.os.path.abspath(__file__))


class FileCheck:
    # ---------------- Set Jar & Files Paths ----------------
    def Set_Path(self):
        self.APKEditor_Path = M.os.path.join(run_dir, "APKEditor.jar")
        self.APKTool_Path = M.os.path.join(run_dir, "APKTool_AP.jar")
        self.Sign_Jar = M.os.path.join(run_dir, "Uber-Apk-Signer.jar")
        self.AES_Smali = M.os.path.join(script_dir, "AES.smali")
        self.Pairip_CoreX = M.os.path.join(script_dir, "lib_Pairip_CoreX.so")


    def isEmulator(self):
        self.APKTool_Path_E = M.os.path.join(run_dir, "APKTool_OR.jar")


    # ---------------- SHA-256 CheckSum ----------------
    def Calculate_CheckSum(self, file_path):
        sha256_hash = M.hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except FileNotFoundError:
            return None


    # ---------------- Download Files ----------------    
    def Download_Files(self, Jar_Files):

        import requests

        downloaded_urls = set()

        for File_URL, File_Path, Expected_CheckSum in Jar_Files:
            File_Name = M.os.path.basename(File_Path)

            if M.os.path.exists(File_Path):
                if self.Calculate_CheckSum(File_Path) == Expected_CheckSum:
                    continue
                else:
                    print(
                        f"{C.ERROR} {C.C}{File_Name} {C.R}is Corrupt (Checksum Mismatch).  ✘\n"
                        f"\n{C.INFO} Re-Downloading, Need Internet Connection.\n"
                    )

                    M.os.remove(File_Path)

            try:
                Version = requests.get("https://raw.githubusercontent.com/TechnoIndian/ApkPatcher/main/VERSION").text.strip()

                if Version != str(__version__):
                    print(f"\n{C.S} Updating {C.E} {C.OG} ApkPatcher ➸❥ {C.G}{Version}...\n\n")

                    if M.os.name == "nt":
                        cmd = "pip install --force-reinstall git+https://github.com/TechnoIndian/ApkPatcher.git"
                    else:
                        cmd = "pip install --force-reinstall https://github.com/TechnoIndian/ApkPatcher/archive/refs/heads/main.zip"

                    M.subprocess.run(cmd, shell=isinstance(cmd, str), check=True)

                print(f'\n{C.S} Downloading {C.E} {C.G}{File_Name}')

                with requests.get(File_URL, stream=True) as response:
                    if response.status_code == 200:
                        total_size = int(response.headers.get('content-length', 0))
                        with open(File_Path, 'wb') as f:
                            print(f'       |')
                            for data in response.iter_content(1024 * 64):
                                f.write(data)

                                print(f"\r       {C.CC}╰┈ PS {C.OG}➸❥ {C.G}{f.tell()/(1024*1024):.2f}/{total_size/(1024*1024):.2f} MB ({f.tell()/total_size*100:.1f}%)", end='', flush=True)

                        print('  ✔\n')

                    else:
                        exit(
                            f'\n\n{C.ERROR} Failed to download {C.Y}{File_Name} {C.R}Status Code: {response.status_code}  ✘\n'
                            f'\n{C.INFO} Restart Script...\n'
                        )

            except requests.exceptions.RequestException:
                exit(
                    f'\n\n{C.ERROR} Got an error while Fetching {C.Y}{File_Path}\n'
                    f'\n{C.ERROR} No internet Connection\n'
                    f'\n{C.INFO} Internet Connection is Required to Download {C.Y}{File_Name}\n'
                )


    # ---------------- Files Download Link ----------------
    def F_D(self):

        self.Download_Files(
            [
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKEditor.jar",
                    self.APKEditor_Path,
                    "71999a1f28cf6b457aff17c139436349cd6ea30d75a0f9cd52f07bd52e21897b"
                ),
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool.jar" if M.os.name == 'nt' else "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool_Modified.jar",

                    self.APKTool_Path,

                    "66cf4524a4a45a7f56567d08b2c9b6ec237bcdd78cee69fd4a59c8a0243aeafa" if M.os.name == 'nt' else "4bd618905d147f5b9235c583863d8c766045c4ac1f85713aa74b5766899d1214"
                ),
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/Uber-Apk-Signer.jar",
                    self.Sign_Jar,
                    "e1299fd6fcf4da527dd53735b56127e8ea922a321128123b9c32d619bba1d835"
                ),
                (
                    "https://raw.githubusercontent.com/TechnoIndian/Objectlogger/refs/heads/main/AES.smali",
                    self.AES_Smali,
                    "09db8c8d1b08ec3a2680d2dc096db4aa8dd303e36d0e3c2357ef33226a5e5e52"
                ),
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/lib_Pairip_CoreX.so",
                    self.Pairip_CoreX,
                    "22a7954092001e7c87f0cacb7e2efb1772adbf598ecf73190e88d76edf6a7d2a"
                )
            ]
        )

        M.os.system('cls' if M.os.name == 'nt' else 'clear')


    # ---------------- Files Download isEmulator ----------------
    def F_D_A(self):

        self.Download_Files(
            [
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool.jar",
                    self.APKTool_Path_E,
                    "66cf4524a4a45a7f56567d08b2c9b6ec237bcdd78cee69fd4a59c8a0243aeafa"
                )
            ]
        )