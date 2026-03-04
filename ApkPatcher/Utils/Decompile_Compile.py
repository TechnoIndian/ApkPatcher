from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from .Files_Check import FileCheck;

F = FileCheck(); F.Set_Path(); F.isEmulator()

C_Line = f"{C.CC}{'_' * 61}"

SUGGEST = (
    f"{C_Line}\n\n"
    f"\n{C.SUGGEST} Try With APKEditor, Flag {C.OG}-a"
    f"\n     |\n     └──── {C.CC}~ Ex. {C.G}$ {C.OG}ApkPatcher {C.Y}{' '.join(M.sys.argv[1:])} {C.OG}-a\n"
)


# ---------------- Decompile APK ----------------
def Decompile_Apk(apk_path, decompile_dir, isEmulator, isAPKEditor, isAES, isAlgorithm, isPine_Hook, Package_Name):

    APKTool_Path = F.APKTool_Path_E if isEmulator else F.APKTool_Path

    AA = f"{'APKEditor' if isAPKEditor else 'APKTool'}"

    print(
        f"\n{C_Line}\n\n"
        f"\n{C.X}{C.C} Decompile APK with {AA}..."
    )

    if isAPKEditor:
        cmd = ["java", "-jar", F.APKEditor_Path, "d", "-i", apk_path, "-o", decompile_dir, "-f", "-no-dex-debug", "-dex-lib", "jf"]

        if isPine_Hook:
            cmd += ["-dex"]

        print(
            f"{C.G}  |\n  └──── {C.CC}Decompiling ~{C.G}$ java -jar {M.os.path.basename(F.APKEditor_Path)} d -i {apk_path} -o {M.os.path.basename(decompile_dir)} -f -no-dex-debug -dex-lib jf\n"
            f"\n{C_Line}{C.G}\n"
        )

    else:
        cmd = ["java", "-jar", APKTool_Path, "d", apk_path, "-o", decompile_dir, "-p", decompile_dir, "-f"]

        if isAES or isAlgorithm:
            cmd += ["--no-debug-info"]

        if isPine_Hook:
            cmd += ["-s"]

        print(
            f"{C.G}  |\n  └──── {C.CC}Decompiling ~{C.G}$ java -jar {M.os.path.basename(APKTool_Path)} d {apk_path} -o {M.os.path.basename(decompile_dir)} -f\n"
            f"\n{C_Line}{C.G}\n"
        )

    try:
        M.subprocess.run(cmd, check=True)

        print(
            f"\n{C.X}{C.C} Decompile Successful {C.G} ✔\n"
            f"\n{C_Line}\n\n"
        )

    except M.subprocess.CalledProcessError:
        M.shutil.rmtree(decompile_dir)

        print(f"\n{C.ERROR} Decompile {Package_Name}.apk Failed with {AA}  ✘\n")

        if not isAPKEditor:
            print(SUGGEST)

        exit(1)


# ---------------- Recompile APK ----------------
def Recompile_Apk(decompile_dir, apk_path, build_dir, isEmulator, isAPKEditor, Package_Name):

    APKTool_Path = F.APKTool_Path_E if isEmulator else F.APKTool_Path

    AA = f"{'APKEditor' if isAPKEditor else 'APKTool'}"

    print(
        f"{C_Line}\n\n"
        f"\n{C.X}{C.C} Recompile APK with {AA}..."
    )

    if isAPKEditor:
        cmd = ["java", "-jar", F.APKEditor_Path, "b", "-i", decompile_dir, "-o", build_dir, "-f", "-dex-lib", "jf"]

        print(
            f"{C.G}  |\n  └──── {C.CC}Recompiling ~{C.G}$ java -jar {M.os.path.basename(F.APKEditor_Path)} b -i {M.os.path.basename(decompile_dir)} -o {M.os.path.basename(build_dir)} -f -dex-lib jf\n"
            f"\n{C_Line}{C.G}\n"
        )

    else:
        original_directory = M.os.path.join(decompile_dir, "original")

        for item in M.os.listdir(original_directory):
            if item != "META-INF":

                item_path = M.os.path.join(original_directory, item)

                if M.os.path.isdir(item_path):
                    M.shutil.rmtree(item_path)
                else:
                    M.os.remove(item_path)

        cmd = ["java", "-jar", APKTool_Path, "b", decompile_dir, "-o", build_dir, "-p", decompile_dir, "-f", "--copy-original"]

        print(
            f"{C.G}  |\n  └──── {C.CC}Recompiling ~{C.G}$ java -jar {M.os.path.basename(APKTool_Path)} b {M.os.path.basename(decompile_dir)} -o {M.os.path.basename(build_dir)} -f --copy-original\n"
            f"\n{C_Line}{C.G}\n"
        )

    try:
        M.subprocess.run(cmd, check=True)

        print(
            f"\n{C.X}{C.C} Recompile Successful {C.G} ✔\n"
            f"\n{C_Line}\n"
        )

    except M.subprocess.CalledProcessError:
        #M.shutil.rmtree(decompile_dir)

        print(f"\n{C.ERROR} Recompile {Package_Name}.apk Failed with {AA}...  ✘\n")

        if not isAPKEditor:
            print(SUGGEST)

        exit(1)

    if M.os.path.exists(build_dir):
        print(
            f"\n{C.S} APK Created {C.E} {C.OG}➸❥ {C.Y}{build_dir} {C.G} ✔\n"
            f"\n{C_Line}\n"
        )

    M.shutil.rmtree(decompile_dir)


# ---------------- FixSigBlock ----------------
def FixSigBlock(decompile_dir, apk_path, build_dir, rebuild_dir):

    M.os.rename(build_dir, rebuild_dir)

    sig_dir = decompile_dir.replace('_decompiled', '_SigBlock')

    for operation in ["d", "b"]:
        cmd = ["java", "-jar", F.APKEditor_Path, operation, "-t", "sig", "-i", (apk_path if operation == "d" else rebuild_dir), "-f", "-sig", sig_dir]

        if operation == "b":
            cmd.extend(["-o", build_dir])

        M.subprocess.run(cmd, check=True, text=True, capture_output=True)

    M.shutil.rmtree(sig_dir)

    M.os.remove(rebuild_dir)


# ---------------- Sign APK ----------------
def Sign_APK(build_dir):

    cmd = ["java", "-jar", F.Sign_Jar, "-a", build_dir, "--overwrite"]

    print(f"\n{C.X}{C.C} Signing APK...")

    print(
        f"{C.G}  |\n  └──── {C.CC}Signing ~{C.G}$ java -jar {M.os.path.basename(F.Sign_Jar)} -a {build_dir} --overwrite\n"
        f"\n{C_Line}{C.G}\n"
    )

    try:
        M.subprocess.run(cmd, check=True)

        print(f"\n{C.X}{C.C} Sign Successful {C.G} ✔\n")

        idsig_file = build_dir + ".idsig"

        if M.os.path.exists(idsig_file):
            M.os.remove(idsig_file)

        print(f'{C_Line}\n\n')

    except M.subprocess.CalledProcessError:
        exit(f"\n{C.ERROR} Sign Failed !  ✘\n")