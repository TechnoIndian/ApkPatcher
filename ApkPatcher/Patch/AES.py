from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

from collections import defaultdict
from ApkPatcher.Utils.Files_Check import FileCheck

F = FileCheck(); F.Set_Path()
C_Line = f"{C.CC}{'_' * 61}"


# ---------------- Regex Scan ----------------
def Regex_ScanX(smali_folders):

    for smali_folder in smali_folders:
        for root, _, files in M.os.walk(smali_folder):
            for file in files:
                file_path = M.os.path.join(root, file)
                yield file_path, open(file_path, 'r', encoding='utf-8', errors='ignore').read()


# ---------------- AES Logs Inject ----------------
def AES_Logs_Inject(decompile_dir, smali_folders):

    Algorithm_Regex = M.re.compile(r'"AES/[^/]+/[^"]+"')
    Method_Regex = M.re.compile(r'\.method.*?\s(\S+\(.*?\).*)')
    Class_Regex = M.re.compile(r'\.class[^;]* (L[^;]+;)')

    target_smali = defaultdict(list)

    matched_smali = []

    # -------- Scan Methods --------
    for file_path, content in Regex_ScanX(smali_folders):
        if "Ljavax/crypto/Cipher;->doFinal([B)[B" in content and (
            "Ljavax/crypto/spec/SecretKeySpec;" in content or 
            "Ljavax/crypto/spec/IvParameterSpec;" in content
        ):

            Class_Name = Class_Regex.search(content)[1]

            for block in content.split('.method')[1:]:

                if Algorithm_Regex.search(block):
                    method_sig = Method_Regex.search(".method" + block.split('\n', 1)[0])

                    if method_sig:

                        match = f"{Class_Name}->{method_sig[1]}"

                        target_smali[match].append(file_path)

                    print(
                        f"\r{C.S} Total Method Signature {C.E} {C.OG}➸❥ {C.PN}{len(target_smali)}",
                        end='', flush=True
                    )

    if not target_smali:
        M.shutil.rmtree(decompile_dir)

        exit(
            f"{C.ERROR} No Matching Patterns found !  ✘\n"
            f"\n{C.INFO} Sorry Bro Your Bad Luck !, Not Working MT Logs Method in This Apk, Try Another Method.\n"
        )

    print(f" {C.G} ✔\n\n", flush=True)


    # -------- Find Target Smali --------
    for file_path, content in Regex_ScanX(smali_folders):

        if any(match in content for match in target_smali):
            matched_smali.append(file_path)

        print(f"\r{C.S} Find Target Smali {C.E} {C.OG}➸❥ {C.PN}{len(matched_smali)}", end='', flush=True)

    print(f" {C.G} ✔", flush=True)

    print(f'\n{C_Line}\n')


    # -------- Cipher Algorithm Hook --------
    Chiper_Algorithm_Regex = r"invoke-static (\{[pv]\d+\}), Ljavax/crypto/Cipher;->getInstance\(Ljava/lang/String;\)Ljavax/crypto/Cipher;[^>]*?move-result-object ([pv]\d+)"

    targetSmali = defaultdict(list)

    for match, file_paths in target_smali.items():

        for file_path in file_paths:

            content = open(file_path, 'r', encoding='utf-8', errors='ignore').read()
            matches = list(M.re.finditer(Chiper_Algorithm_Regex, content))

            if matches:
                targetSmali[Chiper_Algorithm_Regex].append(M.os.path.basename(file_path))

                # -------- Injection --------
                for m in matches:

                    invoke_param = m[1]
                    return_param = m[2]

                    injected_lines = [
                        f"invoke-static {invoke_param}, LRK_TECHNO_INDIA/AES;->getInstance(Ljava/lang/Object;)V",
                        f"invoke-static {invoke_param}, Ljavax/crypto/Cipher;->getInstance(Ljava/lang/String;)Ljavax/crypto/Cipher;",
                        f"move-result-object {return_param}",
                        f"invoke-static {{{return_param}}}, LRK_TECHNO_INDIA/AES;->getInstance(Ljava/lang/Object;)V",
                    ]

                    match_text = m[0]
                    replacement_text = "\n    ".join(injected_lines)

                    content = content.replace(match_text, replacement_text)

                open(file_path, 'w', encoding='utf-8', errors='ignore').write(content)

    for pattern, file_paths in targetSmali.items():

        print(f"\n{C.S} Cipher {C.E} {C.C}Method Signature {C.OG}➸❥ {C.P}{pattern}\n")

        for file_name in file_paths:
            print(f"{C.G}  |\n  └──── {C.CC}~{C.G}$ {C.Y}{file_name} {C.G} ✔")

        print(
            f"\n{C.S} Pattern Applied {C.E} {C.OG}➸❥ {C.PN}{len(file_paths)} {C.C}Time/Smali {C.G} ✔\n"
            f"\n{C_Line}\n"
        )

    print(f'{C_Line}\n')


    # -------- Generic AES Method Hook --------
    for match in target_smali:

        regex = M.re.escape(match)

        AES_Regex = rf"invoke-static \{{(.*?)\}}, {regex}[^>]*?move-result-object ([pv]\d+)"

        file_matches = {}

        for file_path in matched_smali:

            content = open(file_path, 'r', encoding='utf-8', errors='ignore').read()

            matches = list(M.re.finditer(AES_Regex, content))

            if matches:
                file_matches[file_path] = (content, matches)

        if file_matches:

            print(f"\n{C.S} Method Signature {C.E} {C.OG}➸❥ {C.P}{match}\n")

            for file_path in file_matches:
                file_name = M.os.path.basename(file_path)

                print(f"{C.G}  |\n  └──── {C.CC}~{C.G}$ {C.Y}{file_name} {C.G} ✔")

            print(
                f"\n{C.S} Pattern Applied {C.E} {C.OG}➸❥ {C.PN}{len(file_matches)} {C.C}Time/Smali {C.G} ✔\n"
                f"\n{C_Line}\n"
            )

            # -------- Injection --------
            for file_path, (content, matches) in file_matches.items():

                for m in matches:

                    invoke_params = m[1]
                    return_param = m[2]

                    invoke_param = invoke_params.split(", ") if invoke_params else []
                    parameters = len(invoke_param)

                    injected_lines = []

                    # -------- Inject parameters --------
                    for idx, param in enumerate(invoke_param, start=1):

                        if idx == 1 and parameters == 1:
                            method_name = "a"
                        else:
                            method_name = f"b{idx}"

                        injected_lines += [
                            f"invoke-static {{{param}}}, LRK_TECHNO_INDIA/AES;->{method_name}(Ljava/lang/Object;)V"
                        ]

                    if parameters > 1:
                        injected_lines += [
                            "invoke-static {}, LRK_TECHNO_INDIA/AES;->b()V"
                        ]

                    injected_lines += [
                        f"invoke-static {{{invoke_params}}}, {match}",
                        f"move-result-object {return_param}",
                        f"invoke-static {{{return_param}}}, LRK_TECHNO_INDIA/AES;->a(Ljava/lang/Object;)V"
                    ]

                    match_text = m[0]
                    replacement_text = "\n    ".join(injected_lines)

                    content = content.replace(match_text, replacement_text)

                open(file_path, 'w', encoding='utf-8', errors='ignore').write(content)


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