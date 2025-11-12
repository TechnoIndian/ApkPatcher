from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from collections import defaultdict
from ApkPatcher.Utils.Files_Check import FileCheck

F = FileCheck(); F.Set_Path()
C_Line = f"{C.CC}{'_' * 61}"


# ---------------- Regex Scan ----------------
def R_S_F(smali_folders):
    for smali_folder in smali_folders:
        for root, _, files in M.os.walk(smali_folder):
            for file in files:
                file_path = M.os.path.join(root, file)
                yield file_path, open(file_path, 'r', encoding='utf-8', errors='ignore').read()


# ---------------- AES Logs Inject ----------------
def AES_Logs_Inject(decompile_dir, smali_folders):
    reg = M.re.compile(r'"AES/[^/]+/[^"]+"')
    Class_P = M.re.compile(r'\.class[^;]* (L[^;]+;)')
    Met_P = M.re.compile(r'\.method.*?\s([a-zA-Z0-9_<>\$]+)\((.*?)\)(.*)')

    Match_F = defaultdict(list)

    matched_files = []

    total_files = 0

    for file_path, content in R_S_F(smali_folders):
        if "Ljavax/crypto/Cipher;->doFinal([B)[B" in content and "Ljavax/crypto/spec/SecretKeySpec;" in content and "Ljavax/crypto/spec/IvParameterSpec;" in content:

            Class_N = Class_P.search(content)[1]

            for block in content.split('.method')[1:]:

                if reg.search(block):
                    Met_M = Met_P.search(".method" + block.split('\n', 1)[0])

                    if Met_M:
                        total_files += 1

                        Met_Sig = f"{Met_M[1]}({Met_M[2]}){Met_M[3]}"

                        match = f"{Class_N}->{Met_Sig}"

                        Match_F[match].append(file_path)

                    print(f"\r{C.S} Total Method Signature {C.E} {C.OG}➸❥ {C.PN}{total_files}", end='', flush=True)

    if total_files == 0:
        M.shutil.rmtree(decompile_dir)

        exit(
            f"{C.ERROR} No Matching Patterns found !  ✘\n"
            f"\n{C.INFO} Sorry Bro Your Bad Luck !, Not Working MT Logs Method in This Apk, Try Another Method.\n"
        )

    print(f" {C.G} ✔\n\n", flush=True)

    for file_path, content in R_S_F(smali_folders):
        if any(match in content for match in Match_F):
            total_files += 1

            matched_files.append(file_path)

        print(f"\r{C.S} Find Target Smali {C.E} {C.OG}➸❥ {C.PN}{total_files}", end='', flush=True)

    print(f" {C.G} ✔", flush=True)

    print(f'\n{C_Line}\n')

    Inject_A = r"invoke-static (\{[pv]\d+\}), Ljavax/crypto/Cipher;->getInstance\(Ljava/lang/String;\)Ljavax/crypto/Cipher;[^>]*?move-result-object ([pv]\d+)"

    Inject_A_matches = defaultdict(list)

    for match, file_paths in Match_F.items():
        for file_path in file_paths:
            content = open(file_path, 'r', encoding='utf-8', errors='ignore').read()
            matches = list(M.re.finditer(Inject_A, content))

            if matches:
                Inject_A_matches[Inject_A].append(M.os.path.basename(file_path))

                updated_content = content

                for m in matches:
                    invoke_pv, result_pv = m[1], m[2]

                    if f"invoke-static {invoke_pv}, LRK_TECHNO_INDIA/AES;->getInstance(Ljava/lang/Object;)V" not in updated_content:
                        injected_lines = [
                            f"invoke-static {invoke_pv}, LRK_TECHNO_INDIA/AES;->getInstance(Ljava/lang/Object;)V",
                            f"invoke-static {invoke_pv}, Ljavax/crypto/Cipher;->getInstance(Ljava/lang/String;)Ljavax/crypto/Cipher;",
                            f"move-result-object {result_pv}",
                            f"invoke-static {{{result_pv}}}, LRK_TECHNO_INDIA/AES;->getInstance(Ljava/lang/Object;)V",
                        ]
                        match_text = m[0]
                        replacement_text = "\n    ".join(injected_lines)

                        if match_text in updated_content:
                            updated_content = updated_content.replace(match_text, replacement_text)

                open(file_path, 'w', encoding='utf-8', errors='ignore').write(updated_content)

    for pattern, file_paths in Inject_A_matches.items():
        print(f"\n{C.S} Cipher {C.E} {C.C}Method Signature {C.OG}➸❥ {C.P}{pattern}\n")
        for file_name in file_paths:
            print(f"{C.G}  |\n  └──── {C.CC}~{C.G}$ {C.Y}{file_name} {C.G} ✔")

        print(
            f"\n{C.S} Pattern Applied {C.E} {C.OG}➸❥ {C.PN}{len(file_paths)} {C.C}Time/Smali {C.G} ✔\n"
            f"\n{C_Line}\n"
        )

    print(f'{C_Line}\n')

    for match in Match_F:
        regex = M.re.escape(match)
        matching_files, T_P = [], 0
            
        Inject_R = rf"invoke-static \{{(.*?)\}}, {regex}[^>]*?move-result-object ([pv]\d+)"

        for file_path in matched_files:
            content = open(file_path, 'r', encoding='utf-8', errors='ignore').read()

            matches = list(M.re.finditer(Inject_R, content))

            if matches:
                T_P += 1
                matching_files.append(M.os.path.basename(file_path))

        if T_P > 0:
            print(f"\n{C.S} Method Signature {C.E} {C.OG}➸❥ {C.P}{match}\n")
            for file_name in matching_files:
                print(f"{C.G}  |\n  └──── {C.CC}~{C.G}$ {C.Y}{M.os.path.basename(file_name)} {C.G} ✔")
            print(
                f"\n{C.S} Pattern Applied {C.E} {C.OG}➸❥ {C.PN}{len(matching_files)} {C.C}Time/Smali {C.G} ✔\n"
                f"\n{C_Line}\n"
            )

            for file_path in matched_files:
                content = open(file_path, 'r', encoding='utf-8', errors='ignore').read()
                matches = list(M.re.finditer(Inject_R, content))

                if matches:
                    updated_content = content
                    for m in matches:
                        invoke_args, result_register = m[1], m[2]

                        invoke_args_list = invoke_args.split(", ")
                        param_count = len(invoke_args_list)

                        injected_lines = []
                        if param_count == 1:
                            injected_lines.append(f"invoke-static {{{invoke_args_list[0]}}}, LRK_TECHNO_INDIA/AES;->a(Ljava/lang/Object;)V")
                            injected_lines.append(f"invoke-static {{{invoke_args}}}, {match}\n    move-result-object {result_register}")
                            injected_lines.append(f"invoke-static {{{result_register}}}, LRK_TECHNO_INDIA/AES;->a(Ljava/lang/Object;)V")
                        elif param_count > 1:
                            for idx, param in enumerate(invoke_args_list, start=1):
                                injected_lines.append(f"invoke-static {{{param}}}, LRK_TECHNO_INDIA/AES;->b{idx}(Ljava/lang/Object;)V")
                            injected_lines.append(f"invoke-static {{}}, LRK_TECHNO_INDIA/AES;->b()V")
                            injected_lines.append(f"invoke-static {{{invoke_args}}}, {match}\n    move-result-object {result_register}")
                            injected_lines.append(f"invoke-static {{{result_register}}}, LRK_TECHNO_INDIA/AES;->a(Ljava/lang/Object;)V")

                        match_text = m[0]
                        replacement_text = "\n    ".join(injected_lines)

                        if match_text in updated_content:
                            updated_content = updated_content.replace(match_text, replacement_text)

                    open(file_path, 'w', encoding='utf-8', errors='ignore').write(updated_content)


# ---------------- Copy AES Smali ----------------
def Copy_AES_Smali(decompile_dir, smali_folders, manifest_path, isAES_MS, isAPKEditor):

    AES_Logs_Inject(decompile_dir, smali_folders)

    if isAES_MS:
        if isAPKEditor:
            decompile_dir = M.os.path.join(decompile_dir, "smali")

        prefix = "classes" if isAPKEditor else "smali_classes"

        L_S_C_F = M.os.path.join(decompile_dir, f"{prefix}{int(M.os.path.basename(smali_folders[-1])[len(prefix):]) + 1}")

        M.os.makedirs(L_S_C_F, exist_ok=True)
    else:
        L_S_C_F = smali_folders[-1]


    # ---------------- Copy AES.smali ----------------
    Target_Dest = M.os.path.join(L_S_C_F, 'RK_TECHNO_INDIA', 'AES.smali')
    M.os.makedirs(M.os.path.dirname(Target_Dest), exist_ok=True)
    M.shutil.copy(F.AES_Smali, Target_Dest)

    print(f"\n{C.S} Generate {C.E} {C.G}AES.smali {C.OG}➸❥ {C.Y}{M.os.path.relpath(Target_Dest, decompile_dir)} {C.G} ✔")


    # ---------------- Update Package Name ----------------
    PKG_Name = M.re.search(
        r'package="([^"]+)"',
        open(manifest_path, 'r', encoding='utf-8', errors='ignore').read()
    )[1]

    content = open(Target_Dest, 'r', encoding='utf-8', errors='ignore').read()

    Update_PKG = content.replace('PACKAGENAME', PKG_Name)

    open(Target_Dest, 'w', encoding='utf-8', errors='ignore').write(Update_PKG)

    print(f"{C.G}     |\n     └── {C.CC}Update Package Name ~{C.G}$ {C.OG}➸❥ {C.P}'{C.G}{PKG_Name}{C.P}' {C.G} ✔\n")