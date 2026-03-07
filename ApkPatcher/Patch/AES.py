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
        if "Ljavax/crypto/Cipher;->doFinal([B)[B" in content and (
            "Ljavax/crypto/spec/SecretKeySpec;" in content or 
            "Ljavax/crypto/spec/IvParameterSpec;" in content
        ):

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
                            injected_lines += [
                                f"invoke-static {{{invoke_args_list[0]}}}, LRK_TECHNO_INDIA/AES;->a(Ljava/lang/Object;)V"
                                f"invoke-static {{{invoke_args}}}, {match}\n    move-result-object {result_register}"
                                f"invoke-static {{{result_register}}}, LRK_TECHNO_INDIA/AES;->a(Ljava/lang/Object;)V"
                            ]
                        elif param_count > 1:
                            for idx, param in enumerate(invoke_args_list, start=1):
                                injected_lines += [
                                    f"invoke-static {{{param}}}, LRK_TECHNO_INDIA/AES;->b{idx}(Ljava/lang/Object;)V"
                                ]

                            injected_lines += [
                                f"invoke-static {{}}, LRK_TECHNO_INDIA/AES;->b()V",

                                f"invoke-static {{{invoke_args}}}, {match}",
                                f"move-result-object {result_register}",

                                f"invoke-static {{{result_register}}}, LRK_TECHNO_INDIA/AES;->a(Ljava/lang/Object;)V"
                            ]

                        match_text = m[0]
                        replacement_text = "\n    ".join(injected_lines)

                        if match_text in updated_content:
                            updated_content = updated_content.replace(match_text, replacement_text)

                    open(file_path, 'w', encoding='utf-8', errors='ignore').write(updated_content)


# ---------------- Copy AES Smali ----------------
def Copy_AES_Smali(decompile_dir, smali_folders, manifest_path, isAES_MS, isAlgorithm, isAPKEditor):

    if isAlgorithm:
        Patch_Algorithm(smali_folders)
    else:
        AES_Logs_Inject(decompile_dir, smali_folders)

    if isAPKEditor:
        decompile_dir = M.os.path.join(
            decompile_dir,
            "root" if isAlgorithm else "smali" 
        )

    prefix = "classes" if isAPKEditor else "smali_classes"

    name = M.os.path.basename(smali_folders[-1])[len(prefix):]

    idx = int(name) + 1 if name.isdigit() else 2

    if isAES_MS:

        lastSmaliFolder = M.os.path.join(
            decompile_dir,
            f"{prefix}{idx}"
        )

        M.os.makedirs(lastSmaliFolder, exist_ok=True)
    else:
        lastSmaliFolder = smali_folders[-1]


    # ---------------- Copy Dex & Smali ----------------
    if isAlgorithm:
        dex_name = f"classes{idx}.dex"

        dest_path = M.os.path.join(decompile_dir, dex_name)

        M.shutil.copy(F.Algorithm_Dex, dest_path)

        print(f"\n{C.S} Generate {C.E} {C.G}{dex_name} {C.OG}➸❥ {C.Y}{M.os.path.relpath(dest_path, decompile_dir)} {C.G} ✔")

    else:
        Target_Dest = M.os.path.join(lastSmaliFolder, "RK_TECHNO_INDIA", "AES.smali")

        M.os.makedirs(M.os.path.dirname(Target_Dest), exist_ok=True)

        M.shutil.copy(F.AES_Smali, Target_Dest)

        print(f"\n{C.S} Generate {C.E} {C.G}AES.smali {C.OG}➸❥ {C.Y}{M.os.path.relpath(Target_Dest, decompile_dir)} {C.G} ✔")


    if not isAlgorithm:
        # ---------------- Update Package Name ----------------
        PKG_Name = M.re.search(
            r'package="([^"]+)"',
            open(manifest_path, 'r', encoding='utf-8', errors='ignore').read()
        )[1]

        content = open(Target_Dest, 'r', encoding='utf-8', errors='ignore').read()

        Update_PKG = content.replace('PACKAGENAME', PKG_Name)

        open(Target_Dest, 'w', encoding='utf-8', errors='ignore').write(Update_PKG)

        print(f"{C.G}     |\n     └── {C.CC}Update Package Name ~{C.G}$ {C.OG}➸❥ {C.P}'{C.G}{PKG_Name}{C.P}' {C.G} ✔\n")



# ---------------- Regex Scan ----------------
def Regex_Scan(Smali_Path, Target_Regex, Count, Lock):

    Smali = open(Smali_Path, 'r', encoding='utf-8', errors='ignore').read()

    Regexs = [M.re.compile(r) for r in Target_Regex]

    for Regex in Regexs:
        if Regex.search(Smali):

            if Lock:
                try:
                    with Lock:
                        Count.value += 1

                        print(f"\r{C.S} Find Target Smali {C.E} {C.OG}➸❥ {C.PN}{Count.value}", end='', flush=True)

                except Exception:
                    return None

            else:
                Count[0] += 1

                print(f"\r{C.S} Find Target Smali {C.E} {C.OG}➸❥ {C.PN}{Count[0]}", end='', flush=True)

            return Smali_Path


# ---------------- Patch Algorithm ----------------
def Patch_Algorithm(smali_folders):

    Smali_Paths, Match_Smali = [], []

    patterns = [
        # ---------------- URL + Headers ----------------
        (
            r'invoke-virtual \{([pv]\d+)\}, Ljava/net/URL;->openConnection\(\)Ljava/net/URLConnection;',
            r'invoke-static {\1}, Lcom/algorithm/hook/URL;->openConnection(Ljava/net/URL;)Ljava/net/URLConnection;',
            f"URLConnection"
        ),
        (
            r'invoke-virtual \{([pv]\d+)\}, Ljava/net/HttpURLConnection;->connect\(\)V',
            r'invoke-static {\1}, Lcom/algorithm/hook/URL;->connect(Ljava/net/HttpURLConnection;)V',
            f"HttpURLConnection"
        ),
        (
            r'invoke-virtual \{([pv]\d+)\}, Lokhttp3/Request;->url\(\)Lokhttp3/HttpUrl;',
            r'invoke-static {\1}, Lcom/algorithm/hook/URL;->url(Lokhttp3/Request;)Lokhttp3/HttpUrl;',
            f"okhttp3.Request"
        ),
        (
            r'invoke-virtual \{([pv]\d+), ([pv]\d+)\}, Lokhttp3/OkHttpClient;->newCall\(Lokhttp3/Request;\)Lokhttp3/Call;',
            r'invoke-static {\1, \2}, Lcom/algorithm/hook/URL;->newCall(Lokhttp3/OkHttpClient;Lokhttp3/Request;)Lokhttp3/Call;',
            f"okhttp3.OkHttpClient"
        ),


        # ---------------- Algorithm ----------------
        (
            r'(invoke-direct \{([pv]\d+), ([pv]\d+), ([pv]\d+)\}, Ljavax/crypto/spec/SecretKeySpec;-><init>\(\[BLjava/lang/String;\)V)',
            r'\1\n'
            r'    invoke-static {\3, \4}, Lcom/algorithm/hook/AESHOOK;->SecretKeySpec([BLjava/lang/String;)V',
            f"SecretKeySpec"
        ),
        (
            r'(invoke-direct \{([pv]\d+), ([pv]\d+)\}, Ljavax/crypto/spec/IvParameterSpec;-><init>\(\[B\)V)',
            r'\1\n'
            r'    invoke-static {\3}, Lcom/algorithm/hook/AESHOOK;->IvParameterSpec([B)V',
            f"IvParameterSpec"
        ),
        (
            r'invoke-static \{([pv]\d+)\}, Ljavax/crypto/Cipher;->getInstance\(Ljava/lang/String;\)Ljavax/crypto/Cipher;',
            r'invoke-static {\1}, Lcom/algorithm/hook/AESHOOK;->getInstance(Ljava/lang/String;)Ljavax/crypto/Cipher;',
            f"Chiper Algorithm"
        ),
        (
            r'invoke-virtual \{([pv]\d+), ([pv]\d+), ([pv]\d+), ([pv]\d+)\}, Ljavax/crypto/Cipher;->init\(ILjava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;\)V',
            r'invoke-static {\1, \2, \3, \4}, Lcom/algorithm/hook/AESHOOK;->init(Ljavax/crypto/Cipher;ILjava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V',
            f"Chiper Mode, Key & IV"
        ),
        (
            r'invoke-virtual \{([pv]\d+), ([pv]\d+)\}, Ljavax/crypto/Cipher;->doFinal\(\[B\)\[B',
            r'invoke-static {\1, \2}, Lcom/algorithm/hook/AESHOOK;->doFinal(Ljavax/crypto/Cipher;[B)[B',
            f"doFinal"
        )
    ]

    Target_Regex = [p[0] for p in patterns]

    for smali_folder in smali_folders:
        for root, _, files in M.os.walk(smali_folder):
            for file in files:
                if file.endswith('.smali'):
                    Smali_Paths.append(M.os.path.join(root, file))

    try:
        # ---------------- Multi Threading ----------------
        with M.Manager() as MT:
            Count = MT.Value('i', 0); Lock = MT.Lock()
            with M.Pool(M.cpu_count()) as PL:
                Match_Smali = [path for path in PL.starmap(Regex_Scan, [(Smali_Path, Target_Regex, Count, Lock) for Smali_Path in Smali_Paths]) if path]

    except Exception:
        # ---------------- Single Threading ----------------
        Count = [0]
        for Smali_Path in Smali_Paths:
            result = Regex_Scan(Smali_Path, Target_Regex, Count, None)

            if result:
                Match_Smali.append(result)

    print(f" {C.G} ✔", flush=True)

    print(f'\n{C_Line}\n')

    if Match_Smali:
        for pattern, replacement, description in patterns:

            Count_Applied = 0

            Applied_Files = set()

            for file_path in Match_Smali:

                content = open(file_path, 'r', encoding='utf-8', errors='ignore').read()

                new_content = M.re.sub(pattern, replacement, content)

                if new_content != content:
                    if file_path not in Applied_Files:
                        Applied_Files.add(file_path)

                    Count_Applied += 1

                    open(file_path, 'w', encoding='utf-8', errors='ignore').write(new_content)

            if Count_Applied > 0:
                print(f"\n{C.S} Tag {C.E} {C.G}{description}")

                print(f"\n{C.S} Pattern {C.E} {C.OG}➸❥ {C.P}{pattern}")

                for file_path in Applied_Files:
                    print(f"{C.G}  |\n  └──── {C.CC}~{C.G}$ {C.Y}{M.os.path.basename(file_path)} {C.G} ✔")

                print(
                    f"\n{C.S} Pattern Applied {C.E} {C.OG}➸❥ {C.PN}{Count_Applied} {C.C}Time/Smali {C.G} ✔\n"
                    f"\n{C_Line}\n"
                )
