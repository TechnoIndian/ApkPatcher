# -* coding: utf-8 *-
# @auhtor: AbhiTheModder

from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()


patterns = {
    "arm64": [
        "F. 0F 1C F8 F. 5. 01 A9 F. 5. 02 A9 F. .. 03 A9 .. .. .. .. 68 1A 40 F9",
        "F. 43 01 D1 FE 67 01 A9 F8 5F 02 A9 F6 57 03 A9 F4 4F 04 A9 13 00 40 F9 F4 03 00 AA 68 1A 40 F9",
        "FF 43 01 D1 FE 67 01 A9 .. .. 06 94 .. 7. 06 94 68 1A 40 F9 15 15 41 F9 B5 00 00 B4 B6 4A 40 F9",
    ],
    "arm": [
        "2D E9 F. 4. D0 F8 00 80 81 46 D8 F8 18 00 D0 F8",
    ],
    "x86": [
        "55 41 57 41 56 41 55 41 54 53 50 49 89 fe 48 8b 1f 48 8b 43 30 4c 8b b8 d0 01 00 00 4d 85 ff 74 12 4d 8b a7 90 00 00 00 4d 85 e4 74 4a 49 8b 04 24 eb 46",
        "55 41 57 41 56 41 55 41 54 53 50 49 89 f. 4c 8b 37 49 8b 46 30 4c 8b a. .. 0. 00 00 4d 85 e. 74 1. 4d 8b",
        "55 41 57 41 56 41 55 41 54 53 48 83 EC 18 49 89 FF 48 8B 1F 48 8B 43 30 4C 8B A0 28 02 00 00 4D 85 E4 74",
        "55 41 57 41 56 41 55 41 54 53 48 83 EC 38 C6 02 50 48 8B AF A. 00 00 00 48 85 ED 74 7. 48 83 7D 00 00 74",
        "55 41 57 41 56 41 55 41 54 53 48 83 EC 18 49 89 FE 4C 8B 27 49 8B 44 24 30 48 8B 98 D0 01 00 00 48 85 DB",
    ],
}


# ---------------- Get r2 Version ----------------
def get_r2_version():

    try:
        result = M.subprocess.run(["r2", "-V"], capture_output=True, text=True, check=True)
        results = result.stdout.strip().split()

        for result in results:
            if result.startswith(("5.", "6.")):
                result = result.split("-")[0]
                return result

        return None

    except (M.subprocess.CalledProcessError, FileNotFoundError):
        return None


# ---------------- Find Offset ----------------
def find_offset(r2, patterns, is_iA=False):

    if is_iA:
        arch = M.json.loads(r2.cmd("iAj"))
    else:
        arch = M.json.loads(r2.cmd("iaj"))

    arch_value = arch["bins"][0]["arch"]
    arch_bits = arch["bins"][0]["bits"]

    if arch_value == "arm" and arch_bits == 64:
        arch = "arm64"
    elif arch_value == "arm" and arch_bits == 16:
        arch = "arm"
    elif arch_value == "x86" and arch_bits == 64:
        arch = "x86"
    else:
        print(f"\n{C.ERROR} Unsupported architecture: {arch_value}\n")
        return

    if arch in patterns:
        for arch in patterns:
            for pattern in patterns[arch]:
                search_result = r2.cmd(f"/x {pattern}")
                search_result = search_result.strip().split(" ")[0]

                if search_result:
                    search_fcn = r2.cmd(f"{search_result};afl.").strip().split(" ")[0]
                    print(f"\n{C.X}{C.C} ssl_verify_peer_cert found at: {C.PN}{search_result}\n")

                    if not search_fcn and arch == "x86":
                        search_fcn = search_result
                        r2.cmd(f"af @{search_fcn}")

                    print(f"\n{C.X}{C.C} function at: {C.PN}{search_fcn}\n")
                    return search_fcn


# ---------------- Patch Flutter SSL ----------------
def Patch_Flutter_SSL(decompile_dir, isAPKEditor):

    print(f"\r{C.X}{C.C} Flutter SSL Patch, Script by {C.OG}🇮🇳 AbhiTheM0dder 🇮🇳\n")

    try:
        r2_version = tuple(map(int, get_r2_version().split(".")))
        ia_version = tuple(map(int, "5.9.5".split(".")))

        if r2_version <= ia_version:
            is_iA = True
        else:
            is_iA = False

    except Exception as e:
        exit(f"\n{C.ERROR} {str(e)}\n")

    architectures = ["arm64-v8a", "armeabi-v7a", "armeabi", "x86_64"]
    lib_so_path = None

    for arch in architectures:
        lib = "root/lib" if isAPKEditor else "lib"
        potential_path = M.os.path.join(decompile_dir, lib, arch, 'libflutter.so')

        if M.os.path.exists(potential_path):
            lib_so_path = potential_path
            break

    if lib_so_path:
        print(f"\n{C.S} Found {C.E} {C.OG}➸❥ {C.Y}{arch}/{M.os.path.basename(lib_so_path)} {C.G} ✔\n")
    else:
        exit(f"\n{C.ERROR} libflutter.so not found in any of the specified architectures {architectures}\n")

        M.shutil.rmtree(decompile_dir)

    import r2pipe

    if r2pipe.in_r2():
        r2 = r2pipe.open()
        r2.cmd("e log.quiet=true")
        r2.cmd("oo+")
    else:
        r2 = r2pipe.open(lib_so_path, flags=["-w", "-e", "log.quiet=true"])

    print(f"\n{C.X}{C.G} Analyzing function calls...\n")

    r2.cmd("aac")

    print(f"\n{C.X}{C.G} Searching for offset...\n")

    offset = find_offset(r2, patterns, is_iA)

    if offset:
        r2.cmd(f"{offset}")
        r2.cmd("wao ret0")
        print(f"\n{C.X}{C.C} ssl_verify_peer_cert: {C.G}Patched Successfully !  ✔\n")
    else:
        print(f"\n{C.ERROR} ssl_verify_peer_cert Not Found.  ✘\n")

    print(f"{C.CC}{'_' * 61}\n\n")

    r2.quit()