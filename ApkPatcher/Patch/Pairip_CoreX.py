from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from ApkPatcher.Utils.Files_Check import FileCheck

F = FileCheck(); F.Set_Path()


# ---------------- Check CoreX ----------------
def Check_CoreX(decompile_dir, isAPKEditor):

    Lib_CoreX = []

    lib_paths = M.os.path.join(decompile_dir,
            *(
                ['root', 'lib', 'arm64-v8a'] if isAPKEditor else ['lib', 'arm64-v8a']
            )
        )

    for target_file in ['lib_Pairip_CoreX.so', 'libFirebaseCppApp.so']:
        if M.os.path.isfile(M.os.path.join(lib_paths, target_file)):
            Lib_CoreX.append(f"{C.G}{target_file} ➸❥ {C.P}arm64-v8a")

    if Lib_CoreX:
        print(f"{C.INFO}{C.C} Already Added {C.OG}➸❥ {f' {C.OG}& '.join(Lib_CoreX)} {C.G} ✔\n")

        return True
    return False


# ---------------- HooK CoreX ----------------
def Hook_Core(apk_path, decompile_dir, isAPKEditor, Package_Name):

    with M.zipfile.ZipFile(apk_path, 'r') as zf:
        base_apk = "base.apk" if "base.apk" in zf.namelist() else f"{Package_Name}.apk"

    try:
        if M.os.name == 'nt' and M.shutil.which("7z"):
            M.subprocess.run(["7z", "e", apk_path, base_apk, "-y"], text=True, capture_output=True)

            with M.zipfile.ZipFile(apk_path) as zf:
                zf.extract(base_apk)

        else:
            if M.shutil.which("unzip"):
                M.subprocess.run(["unzip", "-o", apk_path, base_apk], text=True, capture_output=True)

                with M.zipfile.ZipFile(apk_path) as zf:
                    zf.extract(base_apk)

        print(f'\n{C.S} Dump {C.E} {C.G}➸❥ {C.OG}{base_apk}\n')

        Dump_Apk = "libFirebaseCppApp.so"
        M.os.rename(base_apk, Dump_Apk)

        lib_paths = M.os.path.join(decompile_dir,
            *(
                ['root', 'lib', 'arm64-v8a'] if isAPKEditor else ['lib', 'arm64-v8a']
            )
        )

        print(f"\n{C.S} Arch {C.E} {C.G}➸❥ arm64-v8a\n")

        M.shutil.move(Dump_Apk, lib_paths); M.shutil.copy(F.Pairip_CoreX, lib_paths);

        print(
            f'\n{C.S} HooK {C.E} {C.G}➸❥ {C.OG}libFirebaseCppApp.so {C.G} ✔\n'
            f'\n{C.S} HooK {C.E} {C.G}➸❥ {C.OG}lib_Pairip_CoreX.so {C.G} ✔\n'
        )

        return True

    except Exception as e:
        print(f"\n{C.ERROR} {e}  ✘")