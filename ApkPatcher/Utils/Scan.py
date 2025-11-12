from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from .Files_Check import FileCheck

F = FileCheck(); F.Set_Path();

EX = f"{C.P}\n   |\n   ╰{C.CC}┈{C.OG}➢ {C.G}ApkPatcher {' '.join(M.sys.argv[1:])} {C.OG}"


# ---------------- Scan APK ----------------
def Scan_Apk(apk_path, isFlutter, isPairip):

    print(f"\n{C.CC}{'_' * 61}\n")

    Package_Name = ''

    if M.os.name == 'posix':
        # ---------------- Extract Package Name with AAPT ----------------
        Package_Name = M.subprocess.run(
            ['aapt', 'dump', 'badging', apk_path],
            capture_output=True, text=True
        ).stdout.split("package: name='")[1].split("'")[0]

        if Package_Name:
            print(f"\n{C.S} Package Name {C.E} {C.OG}➸❥ {C.P}'{C.G}{Package_Name}{C.P}' {C.G} ✔")


    # ---------------- Extract Package Name with APKEditor ----------------
    if not Package_Name:
        Package_Name = M.subprocess.run(
            ["java", "-jar", F.APKEditor_Path, "info", "-package", "-i", apk_path],
            capture_output=True, text=True
        ).stdout.split('"')[1]

        print(f"\n{C.S} Package Name {C.E} {C.OG}➸❥ {C.P}'{C.G}{Package_Name}{C.P}' {C.G} ✔")


    
    # ---------------- Check Flutter / Pairip Protection ----------------
    isPairip_lib = isFlutter_lib = False

    with M.zipfile.ZipFile(apk_path, 'r') as zip_ref:
        for item in zip_ref.infolist():
            if item.filename.startswith('lib/'):
                if item.filename.endswith('libpairipcore.so'):
                    isPairip_lib = True
                if item.filename.endswith('libflutter.so'):
                    isFlutter_lib = True

    
    # ---------------- Check Flutter Protection ----------------
    if isFlutter_lib:
        def check_java_installation():
            try:
                M.subprocess.run(['radare2', '-v'], capture_output=True, text=True)
            except (M.subprocess.CalledProcessError, FileNotFoundError):
                if M.os.name == 'posix':
                    for pkg in ['radare2']:
                        try:

                            result = M.subprocess.run(['pkg', 'list-installed'], capture_output=True, text=True)

                            if pkg not in result.stdout:
                                print(f"\n{C.S} Installing {C.E} {C.OG}➸❥ {C.G}{pkg}...\n")
                                M.subprocess.check_call(['pkg', 'install', '-y', pkg])

                                M.os.system('cls' if M.os.name == 'nt' else 'clear')

                        except (M.subprocess.CalledProcessError, Exception):
                            exit(
                                f"\n\n{C.ERROR} No Internet Connection.  ✘\n"
                                f"\n{C.INFO} Internet Connection is Required to Installation {C.G} pkg install {pkg}\n"
                            )
                else:
                    exit(
                        f"\n\n{C.ERROR} Radare2 is not installed on Your System.  ✘\n"
                        f"\n{C.INFO} Install Radare2 and Run Script Again in New CMD.\n"
                        f"\n{C.INFO} Verify Radare2 Installation {C.G} radare2 -v"
                )

        check_java_installation()

        FP = f"\n\n{C.S} Flutter Protection {C.E} {C.OG}➸❥ {C.P}'{C.G}libflutter.so{C.P}' {C.G} ✔"

        if not isFlutter:
            exit(
                f"{FP}\n\n"
                f"\n{C.WARN} This is Flutter APK, So For SSL Bypass , Use {C.G} -f  {C.B}Flag:\n\n"
                f"\n{C.INFO} If APK is Flutter, Then Use Additional Flag: {C.OG}-f"
                f"{EX}-f {C.Y}-c certificate.cert\n"
            )

        else:
            if isFlutter:
                print(FP)


    # ---------------- Check Pairip Protection ----------------
    if isPairip_lib:
        PP = f"\n\n{C.S} Pairip Protection {C.E} {C.OG}➸❥ {C.P}'{C.G}libpairipcore.so{C.P}' {C.G} ✔"

        if not isPairip:
            exit(
                f"{PP}\n\n"
                f"\n{C.WARN} This is Pairip APK, So For SSL Bypass, Use {C.G} -p {C.C} / {C.G} -p -x  {C.C}( <isCoreX> ) {C.B}Flag:\n\n"
                f"\n{C.INFO} If APK is Pairip, Then Use Additional Flag: {C.OG}-p {C.P}( Without Sign APK Use Only in VM / Multi_App )"
                f"{EX}-p {C.Y}-c certificate.cert\n\n"
                f"\n{C.INFO} If APK is Pairip, Then Hook CoreX & Use Additional Flag: {C.OG}-p -x {C.P}( Install Directly Only For [ arm64 ] )"
                f"{EX}-p -x {C.Y}-c certificate.cert\n\n"
                f"\n{C.INFO} Note Both Method Not Stable, May be APK Crash {C.P}( So Try Your Luck ) 😂\n"
            )

        else:
            if isPairip:
                print(PP)

    return Package_Name, isFlutter_lib, isPairip_lib