from.Package import P

from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

C_Line = f"{C.CC}{'_' * 61}"


# ---------------- Scan Target Regex ----------------
def Regex_Scan(Smali_Path, Target_Regex, Count, Lock, isPKG, isCoreX):

    if isPKG:
        Target_Regex = [P.Match_Regex[1:-1]] if Smali_Path.endswith('.xml') else Target_Regex + [P.Match_Regex] if Smali_Path.endswith('.smali') else []

    if isCoreX:
        Target_Regex = Target_Regex + [ r'\.class public Lcom/pairip/VMRunner;\n']

    Smali = open(Smali_Path, 'r', encoding='utf-8', errors='ignore').read()

    Regexs = [M.re.compile(r) for r in Target_Regex]

    # ---------------- For Regex Scan ----------------
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

    # ---------------- For String Scan ( Without Regex ) ----------------
    #for String in Target_String:
        #if String in Smali:
            #with Lock:
                #Count.value += 1
                #print(f"\r[ Find Target Smali ] ➸❥ {Count.value}", end='', flush=True)
            #return Smali_Path


# ---------------- Apply Smali_Patch ----------------
def Smali_Patch(decompile_dir, smali_folders, isAPKEditor, CA_Cert, isID, isPairip, isPairip_lib, isPKG, isPurchased, isSC, Skip_Patch, isUSB, isCoreX):

    Smali_Paths, matching_files = [], []

    patterns = [
        # ---------------- VPN Bypass ----------------
        (
            r'(const/4 [pv]\d+, 0x4[^>]*?invoke-\w+ \{[^\}]*\}, Landroid/net/NetworkCapabilities;->hasTransport\(I\)Z[^>]*?)move-result ([pv]\d+)',
            r'\1const/4 \2, 0x0',
            "Bypassed Vpn/Proxy Detection NetworkCapabilities hasTransport"
        ),
        (
            r'(Ljava/net/NetworkInterface;->(?:isUp|isVirtual|isLoopback)\(\)Z[^>]*?)move-result ([pv]\d+)',
            r'\1const/4 \2, 0x0',
            "Bypassed Vpn/Proxy Detection NetworkInterface isUp"
        ),
        (
            r'(const-string [pv]\d+, "(tun|tunl0|tun0|utun0|utun1|utun2|utun3|utun4|pptp|ppp|pp0|ppp0|p2p0|ccmni0|ipsec)"[^>]*?invoke-\w+ \{[^\}]*\}, L[^\(]+;->\S+\(Ljava/lang/CharSequence;\)Z[^>]*?)move-result ([pv]\d+)',
            r'\1const/4 \3, 0x0',
            "Bypassed Vpn/Proxy Detection NetworkInterface"
        ),

        # ---------------- Mock Location & Update & Pkg Install Fixed ----------------
        (
            r'(invoke-virtual \{[^\}]*\}, Landroid/location/Location;->(?:isFromMockProvider|isMock)\(\)Z[^>]*?)move-result ([pv]\d+)',
            r'\1const/4 \2, 0x0',
            "Bypassed Mock Detection"
        ),
        (
            r'(invoke-virtual \{[^\}]*\}, Landroid/content/pm/PackageManager;->getInstallerPackageName\(Ljava/lang/String;\)Ljava/lang/String;[^>]*?)move-result-object ([pv]\d+)',
            r'\1const-string \2, "com.android.vending"',
            "Fixed Installer"
        ),

        # ---------------- SSL BYPASS ( MITM ) ----------------
        (
            r'(\.method [^(]*verify\([^\)]*(?:Ljavax/net/ssl/SSLSession;|Ljava/security/cert/X509Certificate;)[^\)]*\)Z\s+.locals \d+)[\s\S]*?(\n.end method)',
            r'\1\n\tconst v0, 0x1\n\treturn v0\2',
            "Verify SSLSession & X509Certificate"
        ),
        (
            r'(\.method [^(]*checkServerTrusted\([^\)]*Ljava/security/cert/X509Certificate;[^\)]*\)Ljava/util/List;\s+.locals \d+)[\s\S]*?(\n.end method)',
            r'\1\n\tnew-instance v0, Ljava/util/ArrayList;\n\tinvoke-direct {v0}, Ljava/util/ArrayList;-><init>()V\n\treturn-object v0\2',
            "checkServerTrusted"
        ),
        (
            r'(\.method [^(]*check(?:Client|Server)Trusted\([^\)]*Ljava/security/cert/X509Certificate;[^\)]*\)V\s+.locals \d+)[\s\S]*?(\n.end method)',
            r'\1\n\treturn-void\2',
            "check(Client|Server)Trusted"
        ),
        (
            r'(\.method [^(]*check\(Ljava/lang/String;(?:Ljava/util/List;|\[Ljava/security/cert/Certificate;)\)V\s+.locals \d+)[\s\S]*?(\n.end method)',
            r'\1\n\treturn-void\2',
            "CertificatePinner & HostnameVerifier"
        ),
        (
            r'(\.method [^(]*check\$okhttp\(Ljava/lang/String;[^\)]*\)V\s+.locals \d+)[\s\S]*?(\n.end method)',
            r'\1\n\treturn-void\2',
            "check$okhttp"
        ),
        (
            r'(\.method [^(]*getAcceptedIssuers\(\)\[Ljava/security/cert/X509Certificate;\s+.locals \d+)[\s\S]*?(\n.end method)',
            r'\1\n\tconst/4 v0, 0x0\n\tnew-array v0, v0, [Ljava/security/cert/X509Certificate;\n\treturn-object v0\2',
            "getAcceptedIssuers"
        ),
        (
            r'(\.method [^(]*\S+\(Ljava/lang/String;[^\)]*\)V\s+.locals \d+)(?:(?!\.end method)[\s\S])*?(?:check-cast [pv]\d+, Ljava/security/cert/X509Certificate;|Ljavax/net/ssl/SSLPeerUnverifiedException;)(?:(?!\.end method)[\s\S])*?(\n.end method)',
            r'\1\n\treturn-void\2',
            "<okhttp3>"
        ),

        # ---------------- Fix Play ----------------
        (
            r'(invoke-interface \{[^\}]*\}, Lcom/google/android/vending/licensing/Policy;->allowAccess\(\)Z[^>]*?\s+)move-result ([pv]\d+)',
            r'\1const/4 \2, 0x1',
            "Bypass Client-Side LVL (allowAccess)"
        ),
        (
            r'(\.method [^(]*connectToLicensingService\(\)V\s+.locals \d+)[\s\S]*?(\s+return-void\n.end method)',
            r'\1\2',
            "connectToLicensingService"
        ),
        (
            r'(\.method [^(]*initializeLicenseCheck\(\)V\s+.locals \d+)[\s\S]*?(\s+return-void\n.end method)',
            r'\1\2',
            "initializeLicenseCheck"
        ),
        (
            r'(\.method [^(]*processResponse\(ILandroid/os/Bundle;\)V\s+.locals \d+)[\s\S]*?(\s+return-void\n.end method)',
            r'\1\2',
            "processResponse"
        )
    ]

    # if CA_Cert:
        # sha1, sha256 = P().Hash(CA_Cert[0])
        # ---------------- SHA-256 & SHA-1 ----------------
        # patterns.extend([
            # (r'(\.method [^(]*\S+\((?:Ljava/security/cert/X509Certificate;|[^)]*)\)Ljava/lang/String;\s+.locals \d+)(?:(?!\.end\smethod)[\s\S])*?"sha256/[^"]*"(?:(?!\.end\smethod)[\s\S])*?(([pv]\d+)\n.end method)', fr'\1\n\tconst-string \3, "sha256/{sha256}"\n\treturn-object \2', f"SHA-256 ➸❥ {C.OG}{sha256}"),
            # (r'(\.method public [^(]*\S+\((?:Ljava/security/cert/X509Certificate;|[^)]*)\)Ljava/lang/String;\s+.*\s+)(?:(?!\.end\smethod)[\s\S])*?"sha1/[^"]*"(?:(?!\.end\smethod)[\s\S])*?(([pv]\d+)\n.end method)', fr'\1\n\tconst-string \3, "sha1/{sha1}"\n\treturn-object \2', f"SHA-1 ➸❥ {C.OG}{sha1}")
        # ])


    # ---------------- Custom Device ID ----------------
    if isID:
        patterns.append(
            (
                r'(const-string [pv]\d+, "android_id"[^>]*?invoke-static \{[^\}]*\}, Landroid/provider/Settings\$Secure;->getString\(Landroid/content/ContentResolver;Ljava/lang/String;\)Ljava/lang/String;[^>]*?)move-result-object ([pv]\d+)',
                rf'\1const-string \2, "{isID}"',
                f"Custom Android ID ➸❥ {C.OG}{isID}"
            )
        )


    # ---------------- isPairip ----------------
    if isPairip and isPairip_lib:
        patterns.extend(
            [
                (
                    r'invoke-static \{[^\}]*\}, Lcom/pairip/SignatureCheck;->verifyIntegrity\(Landroid/content/Context;\)V',
                    r'#',
                    "VerifyIntegrity"
                ),
                (
                    r'(\.method [^(]*verifyIntegrity\(Landroid/content/Context;\)V\s+.locals \d+)[\s\S]*?(\s+return-void\n.end method)',
                    r'\1\2',
                    "VerifyIntegrity"
                ),
                (
                    r'(\.method [^(]*verifySignatureMatches\(Ljava/lang/String;\)Z\s+.locals \d+\s+)[\s\S]*?(\s+return ([pv]\d+)\n.end method)',
                    r'\1const/4 \3, 0x1\2',
                    "verifySignatureMatches"
                )
            ]
        )


    # ---------------- Bypass Package Detection ----------------
    if isPKG:
        patterns.extend(
            [
                # ---------------- Kill Process & Exit ----------------
                (
                    r'invoke-static \{[^\}]*\}, (?:Ljava/lang/System;->exit|Landroid/os/Process;->killProcess)\(I\)V',
                    'nop',
                    "Blocked System.exit & Process.killProcess"
                ),

                # ---------------- Xposed Bypass & Frida Bypass ----------------
                (
                    r'(const-string [pv]\d+, )"de.robv.android.xposed',
                    r'\1"com.Fuck.U',
                    "Bypassed Xposed Detection"
                ),
                (
                    r'const-string [pv]\d+, "(generic|goldfish)"[^>]*?invoke-static \{[^\}]*\}, Landroid/os/Build;->get(Device|Hardware)\(\)Ljava/lang/String;[^>]*?move-result-object [pv]\d+[^>]*?invoke-virtual \{[^\}]*\}, Ljava/lang/String;->contains\(Ljava/lang/CharSequence;\)Z[^>]*move-result ([pv]\d+)',
                    r'const/4 \3, 0x0',
                "Bypassed Device detection"
                 ),
                (
                    r'const-string [pv]\d+, "/data/local/tmp/(?:frida|frida-server)"[^>]*?invoke-static \{[^\}]*\}, Ljava/io/File;->exists\(\)Z[^>]*?move-result ([pv]\d+)',
                    r'const/4 \1, 0x0',
                    "Bypassed Frida Detection"
                )
            ]
        )


    # ---------------- Purchased Status ----------------
    if isPurchased:
        patterns.extend(
            [
                (
                    r'(\.method [^(]*(?:getPrice|getMrp|getPro_mrp|getTotal(?:_)?Price|getOffer(?:_)?price|getSub_pack_price|getSub_actual_price|getActual_price|getDiscount(?:_)?price|getRegistration_price|getProduct_amount|getIs_locked)\(\)Ljava/lang/String;(?:(?!const-string [pv]\d+, "0")[\s\S])*?)(return-object ([pv]\d+)\n.end method)',
                    r'\1const-string \3, "0"\n\t\2',
                    "Patch 1"
                ),
                (
                    r'(\.method [^(]*(?:is(?:_)?Paid|getIs(?:_)?Paid|is(?:_)?purchase(?:d)?|get(?:_)?Purchase(?:d)?|getIs(?:_)?purchase(?:d)?|getPurchaseStatus|getIs_pass|getIs_pro|getIs_pro_purchased|getIs_pro_content|isOwn|isLifetime|is(?:_)?Trial)\(.*\)(?:Ljava/lang/String;|Ljava/lang/Integer;)(?:(?!const-string [pv]\d+, "1")[\s\S])*?)(return-object ([pv]\d+)\n.end method)',
                    r'\1const-string \3, "1"\n\t\2',
                    "Patch 2"
                ),
                (
                    r'(\.method [^(]*(?:is(?:_)?Paid|getInsIspaid|is(?:_)?purchase(?:d)?|getUser_purchase_status|getPurchaseId|is(?:_)?Trial)\(\)(?:I|Z)(?:(?!const [pv]\d+, 0x1)[\s\S])*?)(return ([pv]\d+)\n.end method)',
                    r'\1const \3, 0x1\n\t\2',
                    "Patch 3"
                )
            ]
        )


    # ---------------- Bypass SS ----------------
    if isSC:
        patterns.extend(
            [
                (
                    r'(const/16 [pv]\d+, 0x)200(0\s+(.line \d+\s+)*?invoke-virtual \{[^\}]*\}, Landroid/view/Window;->(?:add|set)Flags\(II\)V)',
                    r'\1\2',
                    "Bypassed Anti-Screen Detection <(add|set)Flags>"
                ),
                (
                    r'(invoke-static \{[^\}]*\}, L[^\(]+;->isSecuredNow\(Landroid/view/Window;\)Z\s+(.line \d+\s+)*?move-result [pv]\d+\s+(.line \d+\s+)*?const/16 ([pv]\d+),) 0x2000',
                    r'\1 0x0',
                    "Bypassed Anti-Screen Detection <isSecuredNow>"
                ),
                (
                    r'(iget [pv]\d+, [pv]\d+, Landroid/view/WindowManager\$LayoutParams;->flags:I\s+(.line \d+\s+)*?or-int/lit16 [pv]\d+, [pv]\d+,) 0x2000',
                    r'\1 0x0',
                    "Bypassed Anti-Screen Detection <flags:I>"
                ),
                (
                    r'(invoke-virtual \{([pv]\d+), ([pv]\d+)\}, Landroid/view/SurfaceView;->setSecure\(Z\)V)',
                    r'const/4 \3, 0x0\n\n\t\1',
                    "Bypassed Anti-Screen Detection <setSecure>"
                )
            ]
        )


    # ---------------- Remove USB Debugging ----------------
    if isUSB:
        patterns.extend(
            [
                (
                    r'(const-string [pv]\d+, "development_settings_enabled"[^>]*invoke-static \{[^\}]*\}, L[^\(]+;->getInt\([^\)]*Ljava\/lang\/String;I\)I[^>]*)move-result ([pv]\d+)',
                    r'\1const/4 \2, 0x0',
                    'Remove USB Debugging <development_settings_enabled>'
                ),
                (
                    r'(const-string [pv]\d+, "adb_enabled"[^>]*invoke-static \{[^\}]*\}, L[^\(]+;->getInt\([^\(]*Ljava\/lang\/String;I\)I[^>]*)move-result ([pv]\d+)',
                    r'\1const/4 \2, 0x0',
                    'Remove USB Debugging <adb_enabled>'
                )
            ]
        )


    Target_Regex = [p[0] for p in patterns]


    # ---------------- Spoof Package Detection ----------------
    if isPKG:
        counter = [1]
        patterns.extend(
            [
                (
                    rf'{P.Match_Regex}', lambda m:
                    f'"com.Fuck.Me{(lambda x: counter.__setitem__(0, x+1) or x)(counter[0])}"',
                    'Spoof Package Detection in Dex'
                ),
                (
                    rf'{P.Match_Regex[1:-1]}', lambda m:
                    f'"com.Fuck.Me{(lambda x: counter.__setitem__(0, x+1) or x)(counter[0])}"',
                    'Spoof Package Detection in Res'
                )
            ]
        )


    # ---------------- loadLibrary ➢ '_Pairip_CoreX' ----------------
    if isCoreX:
        patterns.append(
            (
                r'(\.method [^<]*<clinit>\(\)V\s+.locals \d+\n)',
                r'\1\tconst-string v0, "_Pairip_CoreX"\n\tinvoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V\n',
                f'CoreX_Hook ➸❥ {C.OG}"lib_Pairip_CoreX.so"'
            )
        )

    if isPKG:
        smali_folders = [M.os.path.join(decompile_dir, 'resources' if isAPKEditor else 'res')] + smali_folders

    for smali_folder in smali_folders:
        for root, _, files in M.os.walk(smali_folder):
            for file in files:
                if file.endswith(('.xml', '.smali') if isPKG else ('.smali')):
                    Smali_Paths.append(M.os.path.join(root, file))

    try:
        # ---------------- Multi Threading ----------------
        with M.Manager() as MT:
            Count = MT.Value('i', 0); Lock = MT.Lock()
            with M.Pool(M.cpu_count()) as PL:
                matching_files = [path for path in PL.starmap(Regex_Scan, [(Smali_Path, Target_Regex, Count, Lock, isPKG, isCoreX) for Smali_Path in Smali_Paths]) if path]

    except Exception:
        # ---------------- Single Threading ----------------
        Count = [0]
        for Smali_Path in Smali_Paths:
            result = Regex_Scan(Smali_Path, Target_Regex, Count, None, isPKG, isCoreX)

            if result:
                matching_files.append(result)

    print(f" {C.G} ✔", flush=True)
    print(f'\n{C_Line}\n')

    if matching_files:
        for pattern, replacement, description in patterns:
            count_applied, applied_files = 0, set()

            if description in Skip_Patch:
                print(f"\n{C.S} Skip Patch {C.E} {C.OG}➸❥ {C.G}{description}\n")
                continue

            for file_path in matching_files:
                if description.startswith("CoreX_Hook") and not file_path.endswith("VMRunner.smali"): continue
                content = open(file_path, 'r', encoding='utf-8', errors='ignore').read()
                new_content = M.re.sub(pattern, replacement, content)

                if new_content != content:
                    if file_path not in applied_files:
                        applied_files.add(file_path)

                    count_applied += 1

                    open(file_path, 'w', encoding='utf-8', errors='ignore').write(new_content)

            if count_applied > 0:
                print(f"\n{C.S} Tag {C.E} {C.G}{description}")
                print(f"\n{C.S} Pattern {C.E} {C.OG}➸❥ {C.P}{pattern}")

                for file_path in applied_files:
                    print(f"{C.G}  |\n  └──── {C.CC}~{C.G}$ {C.Y}{M.os.path.basename(file_path)} {C.G} ✔")

                print(
                    f"\n{C.S} Pattern Applied {C.E} {C.OG}➸❥ {C.PN}{count_applied} {C.C}Time/Smali {C.G} ✔\n"
                    f"\n{C_Line}\n"
                )