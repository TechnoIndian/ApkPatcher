from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from importlib.metadata import version

__version__ = version("ApkPatcherX")


# ---------------- Set Path ----------------
run_dir = M.os.path.dirname(M.os.path.abspath(M.sys.argv[0]))
script_dir = M.os.path.dirname(M.os.path.abspath(__file__))

files_dir = M.os.path.join(script_dir, "Files")
pine_dir = M.os.path.join(script_dir, "Pine")
M.os.makedirs(files_dir, exist_ok=True)
M.os.makedirs(pine_dir,  exist_ok=True)


class FileCheck:
    # ---------------- Set Jar & Files Paths ----------------
    def Set_Path(self):

        # ---------------- Jar Tools ----------------
        self.APKTool_Path, self.APKEditor_Path, self.Sign_Jar = (
            M.os.path.join(run_dir, jar)
            for jar in ("APKTool.jar", "APKEditor.jar", "Uber-Apk-Signer.jar")
        )

        # ---------------- HooK Files ----------------
        self.AES_Smali, self.Hook_Smali, self.Pairip_CoreX = (
            M.os.path.join(files_dir, files)
            for files in ("AES.smali", "Hook.smali", "lib_Pairip_CoreX.so")
        )

        # ---------------- Pine HooK ----------------
        self.config, self.libpine32, self.libpine64, self.loader = (
            M.os.path.join(pine_dir, pine)
            for pine in ("config.json", "libpine32", "libpine64", "loader.dex")
        )


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
                    "6b766e71ed5f4c7cce338e74a1ab786cc1ecc1896d9f37f9f1bf639398e5eadc"
                ),
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool.jar" if M.os.name == 'nt' else "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool_Termux.jar",

                    self.APKTool_Path,

                    "d0a81361670b17b713fea45baec3ed04b26bc8b69b30bde9a6f367c13fc25697" if M.os.name == 'nt' else "e00bcfd10d38318e0f52a4666da472cd4e5683a74a0c0d7fc82a362a59b338a9"
                ),
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/Uber-Apk-Signer.jar",
                    self.Sign_Jar,
                    "e1299fd6fcf4da527dd53735b56127e8ea922a321128123b9c32d619bba1d835"
                ),
                (
                    "https://raw.githubusercontent.com/TechnoIndian/Objectlogger/refs/heads/main/Hook.smali",
                    self.Hook_Smali,
                    "c62ac39b468eeda30d0732f947ab6c118f44890a51777f7787f1b11f8f3722c4"
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
                ),
                
                # ---------------- Pine HooK Source ----------------
                (
                    "https://github.com/TechnoIndian/PineHookPlus/releases/download/v1.0/config.json",
                    self.config,
                    "da5eef2fa153068e19fca6fabfd144fbb9d7075a61e333814369bd36c51289c1"
                ),
                (
                    "https://github.com/TechnoIndian/PineHookPlus/releases/download/v1.0/libpine32",
                    self.libpine32,
                    "94854417f9bbb4e2dc49a5edede51dfc1eafca2c7cbb163f59585da7d97fc5db"
                ),
                (
                    "https://github.com/TechnoIndian/PineHookPlus/releases/download/v1.0/libpine64",
                    self.libpine64,
                    "d3e415243b80b866d2c75408cc9a26ba4fcab0775f798442f9a622097d845e0c"
                ),
                (
                    "https://github.com/TechnoIndian/PineHookPlus/releases/download/v1.0/loader.dex",
                    self.loader,
                    "c23fcc7aac75d3ea760523876dc837b6506726194c2fe4376d5172c8271b7c46"
                ),
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
                    "d0a81361670b17b713fea45baec3ed04b26bc8b69b30bde9a6f367c13fc25697"
                )
            ]
        )