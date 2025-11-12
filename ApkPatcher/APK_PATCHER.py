from .CLI import parse_arguments
from .ANSI_COLORS import ANSI; C = ANSI()
from .MODULES import IMPORT; M = IMPORT()

from ApkPatcher.Utils.CRC import CRC_Fix
from ApkPatcher.Utils.Credits import Credits
from ApkPatcher.Utils.Scan import Scan_Apk
from ApkPatcher.Utils.Anti_Splits import Anti_Split
from ApkPatcher.Utils.Files_Check import FileCheck, __version__
from ApkPatcher.Utils.Decompile_Compile import Decompile_Apk, Recompile_Apk, FixSigBlock, Sign_Apk

from ApkPatcher.Patch.AES import Copy_AES_Smali
from ApkPatcher.Patch.Smali_Patch import Smali_Patch
from ApkPatcher.Patch.Ads_Patch import Ads_Smali_Patch
from ApkPatcher.Patch.Spoof_Patch import Patch_Random_Info
from ApkPatcher.Patch.Cert_Net_Config import Write_Net_Config
from ApkPatcher.Patch.Flutter_SSL_Patch import Patch_Flutter_SSL
from ApkPatcher.Patch.Pairip_CoreX import Check_CoreX, Hook_Core
from ApkPatcher.Patch.Manifest_Patch import Fix_Manifest, Patch_Manifest, Permission_Manifest


def Clear():
    M.os.system('cls' if M.os.name == 'nt' else 'clear')
Clear()


# ---------------- Install Require Module ---------------
required_modules = ['requests', 'r2pipe', 'asn1crypto', 'multiprocess']
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"{C.S} Installing {C.E} {C.OG}➸❥ {C.G}{module}...\n")
        try:
            M.subprocess.check_call([M.sys.executable, "-m", "pip", "install", module])
            Clear()
        except (M.subprocess.CalledProcessError, Exception):
            exit(
                f"\n{C.ERROR} No Internet Connection.  ✘\n"
                f"\n{C.INFO} Internet Connection is Required to Install {C.G} pip install {module}\n"
            )


# ---------------- Check Dependencies ---------------
def check_dependencies():
    try:
        M.subprocess.run(['java', '-version'], stdout=M.subprocess.PIPE, stderr=M.subprocess.PIPE, check=True, text=True)
    except (M.subprocess.CalledProcessError, FileNotFoundError):
        if M.os.name == 'posix':
            install_package('openjdk-17')
        else:
            exit(
                f'\n\n{C.ERROR} Java is not installed on Your System.  ✘\n'
                f'\n{C.INFO} Install Java & Run Script Again in New CMD.  ✘\n'
                f'\n{C.INFO} Verify Java Installation {C.G} java --version\n'
            )

    if M.os.name == 'posix': install_package('aapt')


# ---------------- Install Package ---------------
def install_package(pkg):
    try:
        result = M.subprocess.run(['pkg', 'list-installed'], stdout=M.subprocess.PIPE, stderr=M.subprocess.PIPE, text=True)
        if pkg not in result.stdout:
            print(f"{C.S} Installing {C.E} {C.OG}➸❥ {C.G}{pkg}...\n")
            M.subprocess.check_call(['pkg', 'install', '-y', pkg])
            Clear()
    except (M.subprocess.CalledProcessError, Exception):
        exit(
            f"\n\n{C.ERROR} No Internet Connection.  ✘\n"
            f"\n{C.INFO} Internet Connection is Required to Installation  {C.G}pkg install {pkg}\n"
        )

check_dependencies()

F = FileCheck(); F.Set_Path(); F.F_D()

Date = M.datetime.now().strftime('%d/%m/%y')
print(f"{C.OG}{f'v{__version__}':>22}")

# Logo ( 🙏 )
b64 = """eJzVlc9LAkEUx8/Ov9DlMXgNzLAfeMlUSAQLETx4ELGlJEehnEPgQSrqUlFYdIroHNShixDRP1DQn1DaqUv+Cc3MzszOrFtUt96u+2O+n/fmvTe7LoCwsdIEGStNzsRj8WgkSoYXe9fsdwtFp15tEsfSp8n8phyYjZKCU11tNCHTWK5V2GhE+yIUCgF1DYFplIY9s0RLGdG56EsU5PTjRgLcyfIJMk1IQNcDiaUsLCUKyYV0XoUL4H8QErNLbJxNBCtA4FSOikGdOufBj/DYAQS1L72WYreH7CB5ak+iUzPTtHSvZH32LWcYGxsX2Yp7KdIwyI2KJNx1ZpgIZ5TCURqm3qAAkNKona5qn3pkkP1QCZSbnM5QkXDG2MQpWA+fq7IuyAA8lh2e3TPNbASfBHxRkVwZI7QPkpqqUs2OjcAWLqbERv0j5uIqt685UM9bKFjUb8Swu7MFr4eX71fn/Z1jGHZ3j+CjdzfY3uufHr31OvDycAbPN4/3T90sP/B7/uKgfuckcG9/JXy//8XtFz4WiqweTJFchTi8Jtmbtq0WnLqzsl4hmmj73BeLuXTe56/FVKXl/Pt++f6XB51988Mw6ByI6tvqQxIjc+trLUHUONDYGNHz2XIhnVzILZYzuVQmITr0CawgFWQ="""
print(f"{M.zlib.decompress(M.base64.b64decode(b64)).decode('utf-8').rstrip('\n')} | {C.B}{Date}{C.CC}")
print("————————|——————————————————|—————————————————|——————————————|————")


# ---------------- Target All Classes Folder ---------------
def Find_Smali_Folders(decompile_dir, isAPKEditor):

    smali_path = M.os.path.join(decompile_dir, "smali") if isAPKEditor else decompile_dir

    prefix = "classes" if isAPKEditor else "smali_classes"

    folders = sorted([f for f in M.os.listdir(smali_path) if f == "smali" or f.startswith(prefix)], key=lambda x: int(x.split(prefix)[-1]) if x.split(prefix)[-1].isdigit() else 0)

    return [M.os.path.join(smali_path, f) for f in folders]


# ---------------- Execute Main Function ---------------
def RK_Techno_IND():
    args = parse_arguments()
    isCoreX = args.Hook_CoreX
    isFlutter = args.Flutter; isPairip = args.Pairip
    Skip_Patch = args.Skip_Patch if args.Skip_Patch else []
    isAPKEditor = args.APKEditor; isEmulator = args.For_Emulator

    if isEmulator:
        F.isEmulator()
        F.F_D_A()

    if args.Credits_Instruction:
        Credits()

    apk_path = args.input or args.Merge

    if not M.os.path.isfile(apk_path):
        exit(
            f"\n{C.ERROR} APK file '{apk_path}' not found.  ✘\n\n"
            f"\n{C.FYI}{C.G} Make Sure There Is 'No Extra Space' In The Folder/Apk Name In The Input Text. If Yes, Then Remove Extra Space & Correct It By Renaming It.\n"
        )
    
    if args.CA_Certificate:
        isCert = [Cert for Cert in args.CA_Certificate if not M.os.path.isfile(Cert)]

        if isCert:
            exit(f"\n{C.ERROR} Not exist: {', '.join(isCert)}\n")

    apk_path = Anti_Split(apk_path, args.Merge, isCoreX)

    # ---------------- Set All Paths Directory ----------------
    decompile_dir = M.os.path.join(M.os.path.expanduser("~"), f"{M.os.path.splitext(M.os.path.basename(apk_path))[0]}_decompiled")

    build_dir = M.os.path.abspath(M.os.path.join(M.os.path.dirname(apk_path), f"{M.os.path.splitext(M.os.path.basename(apk_path))[0]}_Patched.apk"))

    rebuild_dir = build_dir.replace('_Patched.apk', '_Patch.apk')

    manifest_path = M.os.path.join(decompile_dir, 'AndroidManifest.xml')

    if M.os.name == 'posix':
        M.subprocess.run(['termux-wake-lock'])
        print(f"\n{C.X}{C.C} Acquiring Wake Lock...\r")

    start_time = M.time.time()

    # ---------------- Scan & Decompile APK ---------------
    Package_Name, isFlutter_lib, isPairip_lib = Scan_Apk(apk_path, isFlutter, isPairip)
    Decompile_Apk(apk_path, decompile_dir, isEmulator, isAPKEditor, args.AES_Logs)
    smali_folders = Find_Smali_Folders(decompile_dir, isAPKEditor)

    # ---------------- AES Logs Inject ----------------
    if args.AES_Logs:
        Copy_AES_Smali(decompile_dir, smali_folders, manifest_path, args.AES_S, isAPKEditor)
        Permission_Manifest(decompile_dir, manifest_path, isAPKEditor)

    # ---------------- Remove Ads ----------------
    if args.Remove_Ads:
        Ads_Smali_Patch(smali_folders)

    # ---------------- Fake / Spoof Device Info ----------------
    if args.Random_Info:
        Patch_Random_Info(smali_folders, args.Android_ID)

    if args.AES_Logs or args.Remove_Ads or args.Random_Info:
        Fix_Manifest(manifest_path, smali_folders, args.Spoof_PKG)
    else:
        if isFlutter and isFlutter_lib:
            Patch_Flutter_SSL(decompile_dir, isAPKEditor)

        # ---------------- Smali Patching / Hook CoreX ----------------
        if isCoreX and isPairip and isPairip_lib and Check_CoreX(decompile_dir, isAPKEditor):
            M.shutil.rmtree(decompile_dir)
            exit(1)

        Smali_Patch(decompile_dir, smali_folders, isAPKEditor, args.CA_Certificate, args.Android_ID, isPairip, isPairip_lib, args.Spoof_PKG, args.Purchase, args.Remove_SC, Skip_Patch, args.Remove_USB, isCoreX)

        if isCoreX and isPairip and isPairip_lib:
            Hook_Core(args.input, decompile_dir, isAPKEditor, Package_Name)

        # ---------------- Patch Manifest & Write Network Config ----------------
        Fix_Manifest(manifest_path, smali_folders, args.Spoof_PKG)
        Patch_Manifest(decompile_dir, manifest_path)
        Write_Net_Config(decompile_dir, isAPKEditor, args.CA_Certificate)

    # ---------------- Recompile APK ----------------
    Recompile_Apk(decompile_dir, apk_path, build_dir, isEmulator, isAPKEditor)

    # ---------------- Fix CRC / Sign APK ----------------
    if not isCoreX and isPairip and isPairip_lib or args.unsigned_apk:

        if not isAPKEditor:
            FixSigBlock(decompile_dir, apk_path, build_dir, rebuild_dir);

        CRC_Fix(apk_path, build_dir, ["AndroidManifest.xml", ".dex"])

    else:
        Sign_Apk(build_dir)

    if M.os.path.exists(build_dir):
        print(f'{C.S} Final APK {C.E} {C.G}︻デ═一 {C.Y}{build_dir} {C.G} ✔')

    print(f"\n{C.CC}{'_' * 61}\n")

    if not isCoreX and isPairip and isPairip_lib:
        print(f'\n{C.FYI}{C.C} This is Pairip Apk So U Install {C.G}( Keep Apk Without Sign ) {C.C}in VM / Multi_App\n')

    elapsed_time = M.time.time() - start_time

    print(f'\n{C.S} Time Spent {C.E} {C.G}︻デ═一 {C.PN}{elapsed_time:.2f} {C.CC}Seconds {C.G} ✔\n')

    print(f'\n🚩 {C.CC}࿗ {C.OG}Jai Shree Ram {C.CC}࿗ 🚩\n     🛕🛕🙏🙏🙏🛕🛕\n')

    if M.os.name == 'posix':
        M.subprocess.run(['termux-wake-unlock'])
        exit(f"\n{C.X}{C.C} Releasing Wake Lock...\n")
    exit(0)