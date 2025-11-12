from.Package import P

from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()


# ---------------- Fix Manifest ----------------
def Fix_Manifest(manifest_path, smali_folders, isPKG):

    isPC = bool(M.re.search('piracychecker', open(manifest_path).read(), M.re.I))

    patterns = [
        (
            r'\s+android:(splitTypes|requiredSplitTypes)="[^"]*?"',
            r'',
            'Splits'
        ),
        (
            r'(isSplitRequired=)"true"',
            r'\1"false"',
            'isSplitRequired'
        ),
        (
            r'\s+<meta-data[^>]*"com.android.(vending.|stamp.|dynamic.apk.)[^"]*"[^>]*/>',
            r'',
            '<meta-data>'
        ),
        (
            r'\s+<[^>]*"(com.pairip.licensecheck)[^"]*"[^>]*/>' if isPC else r'\s+<[^>]*"com.(pairip.licensecheck|android.vending.CHECK_LICENSE)[^"]*"[^>]*/>',
            r'',
            'CHECK_LICENSE'
        )
    ]

    if isPKG:
        patterns.extend(
            [
                (
                    rf'{P.Menifest_Regex}',
                    r'',
                    'Spoof Package Detection'
                )
            ]
        )

    for pattern, replacement, description in patterns:
        content = open(manifest_path, 'r', encoding='utf-8', errors='ignore').read()
        new_content = M.re.sub(pattern, replacement, content)

        if new_content != content:
            print(
                f"\n{C.S} Tag {C.E} {C.OG}{description}\n"
                f"\n{C.S} Applying Pattern {C.E} {C.OG}➸❥ {C.P}{pattern}\n"
                f"{C.G}  |\n  └──── {C.CC}Patch Cleaned Up ~{C.G}$  {C.P}'{C.G}{M.os.path.basename(manifest_path)}{C.P}' {C.G} ✔\n"
            )

        open(manifest_path, 'w', encoding='utf-8', errors='ignore').write(new_content)


# ---------------- Patch Manifest ----------------
def Patch_Manifest(decompile_dir, manifest_path):

    content = open(manifest_path, 'r', encoding='utf-8', errors='ignore').read()

    application_tag = M.re.search(r'<application\s+[^>]*>', content)[0]

    cleaned_tag = M.re.sub(
        r'\s+android:(usesCleartextTraffic|networkSecurityConfig)="[^"]*?"',
        '',
        application_tag
    )

    content = content.replace(application_tag,
        M.re.sub(
            r'>',
            '\n\tandroid:usesCleartextTraffic="true"\n\tandroid:networkSecurityConfig="@xml/network_security_config">',
            cleaned_tag
        )
    )

    open(manifest_path, 'w', encoding='utf-8', errors='ignore').write(content)

    print(f'\n{C.S} Updated {C.E}{C.C} android:networkSecurityConfig={C.P}"{C.G}@xml/network_security_config{C.P}" {C.OG}➸❥ {C.Y}{M.os.path.basename(manifest_path)} {C.G} ✔\n')

    print(f'\n{C.S} Updated {C.E}{C.C} android:usesCleartextTraffic={C.P}"{C.G}true{C.P}" {C.OG}➸❥ {C.Y}{M.os.path.basename(manifest_path)} {C.G} ✔\n')


# ---------------- Permission Manifest ----------------
def Permission_Manifest(decompile_dir, manifest_path, isAPKEditor):

    A_Y_P = M.os.path.join(decompile_dir, 'apktool.yml')

    content = open(manifest_path, 'r', encoding='utf-8', errors='ignore').read()

    new_permissions = '''\t<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>\n\t<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>\n\t<uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE"/>'''

    content = M.re.sub(
        r'\s+<uses-permission[^>]*android:name="(android.permission.((READ|WRITE|MANAGE)_EXTERNAL_STORAGE))"[^>]*>',
        '',
        content
    )
        
    content = M.re.sub(
        r'android:targetSdkVersion="\d+"',
        'android:targetSdkVersion="28"',
        content
    )

    content = M.re.sub(
        r'(<manifest\s+[^>]*>)',
        r'\1\n' + new_permissions,
        content
    )

    application_tag = M.re.search(r'<application\s+[^>]*>', content)[0]

    cleaned_tag = M.re.sub(
        r'\s+android:(request|preserve)LegacyExternalStorage="[^"]*?"',
        '',
        application_tag
    )

    content = content.replace(application_tag,
        M.re.sub(
            r'>',
            '\n\tandroid:requestLegacyExternalStorage="true"\n\tandroid:preserveLegacyExternalStorage="true">',
            cleaned_tag
        )
    )
        
    open(manifest_path, 'w', encoding='utf-8', errors='ignore').write(content)
        
    print(f"\n{C.S} Storage Permission {C.E} {C.OG}➸❥ {C.P}'{C.G}AndroidManifest.xml{C.P}' {C.G} ✔\n")

    if not isAPKEditor:
        yml = open(A_Y_P, 'r', encoding='utf-8', errors='ignore').read()

        update_yml = M.re.sub(
            r'(targetSdkVersion:) (\d+)',
            r'\1 28',
            yml
        )

        open(A_Y_P, 'w', encoding='utf-8', errors='ignore').write(update_yml)

        print(f"\n{C.S} targetSdkVersion {C.E} {C.PN}28 {C.OG}➸❥{C.G} apktool.yml\n")