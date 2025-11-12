from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from .Files_Check import FileCheck

F = FileCheck(); F.Set_Path()

C_Line = f"{C.CC}{'_' * 61}"

Merge_Ext = ['.apks', '.apkm', '.xapk']


# ---------------- Anti Split ----------------
def Anti_Split(apk_path, isMerge, isCoreX):

    base_name, Ext = M.os.path.splitext(apk_path)

    if apk_path and isCoreX and M.os.path.splitext(apk_path)[-1].lower() not in Merge_Ext:
        exit(f"\n{C.X}{C.C} Only Supported Extensions {C.G}{Merge_Ext} with {C.OG}CoreX\n")

    if Ext in Merge_Ext:
        output_path = f"{base_name.replace(' ', '_')}.apk"

        print(
            f"{C_Line}\n\n"
            f"\n{C.X}{C.C} Anti-Split Start..."
        )

        print(
            f"{C.G}  |\n  └──── {C.CC}Decompiling ~{C.G}$ java -jar {M.os.path.basename(F.APKEditor_Path)} m -i {apk_path} -f -o {output_path}"
            + (" -extractNativeLibs true" if isCoreX else "")
            + f"\n\n{C_Line}{C.G}\n"
        )

        cmd = ["java", "-jar", F.APKEditor_Path, "m", "-i", apk_path, "-f", "-o", output_path]

        if isCoreX:
            cmd += ["-extractNativeLibs", "true"]

        try:
            result = M.subprocess.run(cmd, check=True)

            print(
                f"\n{C.X}{C.C} Anti-Split Successful {C.G} ✔\n"
                f"\n{C_Line}\n"
            )

            if isMerge: exit()

            return output_path

        except M.subprocess.CalledProcessError as e:
            exit(f"\n{C.ERROR} Anti-Split Failed !  ✘\n")

    if isMerge and Ext not in Merge_Ext:
        exit(
            f"\n{C.ERROR} Split  ✘\n\n"
            f"\n{C.INFO} {C.C} Only Supported Extensions {C.G}{Merge_Ext}\n"
        )

    return apk_path