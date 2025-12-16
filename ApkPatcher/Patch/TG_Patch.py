# TG Patch Inspired By AbhiTheM0dder Script

# Link - https://github.com/AbhiTheModder/termux-scripts/blob/main/tgpatcher.py

from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()
from ApkPatcher.Utils.Files_Check import FileCheck

F = FileCheck(); F.Set_Path()

C_Line = f"{C.CC}{'_' * 61}"


# ---------------- Regex Scan ----------------
def Regex_Scan(Smali_Path, Target_Regex, Count, Lock):

    Smali = open(Smali_Path, 'r', encoding='utf-8', errors='ignore').read()

    Regexs = [M.re.compile(r) for r in Target_Regex]

    matched_idx = []

    for idx, Regex in enumerate(Regexs):
        if Regex.search(Smali):
            matched_idx.append(idx)

    if matched_idx:
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

        return (Smali_Path, matched_idx)


# ---------------- TG Smali Patch ----------------
def TG_Smali_Patch(decompile_dir, smali_folders, isAPKEditor):

    Smali_Paths, Smali_Files, Match_Smali = [], [], []

    Target_Smali = [
        "TextCell.smali",
        "UserConfig.smali",
        "StoryViewer.smali",
        "PhotoViewer.smali",
        "AndroidUtilities.smali",
        "TranslateAlert2.smali",
        "MessageObject.smali",
        "StoriesController.smali",
        "MessagesStorage.smali",
        "FileLoadOperation.smali",
        "FlagSecureReason.smali",
        "SecretMediaViewer.smali",
        "MessagesController.smali",
        "PaymentFormActivity.smali",
        "PremiumPreviewFragment.smali",
        "ProfileActivity$SearchAdapter.smali",
        "PremiumPreviewFragment$Adapter.smali",
        "ConnectionsManager$GoogleDnsLoadTask.smali",
        "ConnectionsManager$ResolveHostByNameTask.smali"
    ]


    # ---------------- is scan Patterns ----------------
    scanPatterns = [
        # ---------------- Bypass SS ----------------
        (
            r'(iget-boolean ([pv]\d+), [pv]\d+, Lorg/telegram/ui/[^;]+;->allowScreenshots:Z)',
            r'\1\nconst \2, 0x1',
            "Bypass Anti-Screen <allowScreenshots>",
            []
        ),
        (
            r'(sget-boolean ([pv]\d+), Lorg/telegram/messenger/SharedConfig;->allowScreenCapture:Z)',
            r'\1\nconst \2, 0x1',
            "Bypass Anti-Screen <allowScreenCapture>",
            []
        ),

        # ---------------- Access Banned Channels [Related] ----------------
        (
            r'(iget-boolean ([pv]\d+), [pv]\d+, Lorg/telegram/[^;]+;->isRestrictedMessage:Z)',
            r'\1\n\tconst \2, 0x0',
            "Access Banned Channels [Related]",
            []
        ),

        # ---------------- Enabling Saving Media Everywhere ----------------
        (
            r'(iget-boolean ([pv]\d+), [pv]\d+, Lorg/telegram/[^;]+;->noforwards:Z)',
            r'\1\n\tconst \2, 0x0',
            "enableSavingMedia",
            []
        ),

        # ---------------- make premiumLocked bool false ----------------
        (
            r'(iget-boolean ([pv]\d+), [pv]\d+, Lorg/telegram/[^;]+;->premiumLocked:Z)',
            r'\1\n\tconst \2, 0x0',
            "premiumLocked ➢ False",
            []
        )
    ]


    # ---------------- is smali Patterns ( only For Target_Smali ) ----------------
    smaliPatterns = [
        # ---------------- Bypass SS ----------------
        (
            r'(const/16 [pv]\d+, 0x)200(0\s+(.line \d+\s+)*?invoke-virtual \{[^\}]*\}, Landroid/view/Window;->(?:add|set|clear)Flags\((?:I|II)\)V)',
            r'\1\2',
            "Bypass Anti-Screen <(add|set|clear)Flags>",
            None
        ),
        (
            r'(const/16 [pv]\d+, 0x)200(0\n)',
            r'\1\2',
            "Bypass Anti-Screen <0x2000>",
            ["AndroidUtilities.smali", "TranslateAlert2.smali", "StoryViewer.smali", "PaymentFormActivity.smali"]
        ),
        (
            r'(invoke-static \{[^\}]*\}, L[^\(]+;->isSecuredNow\(Landroid/view/Window;\)Z\s+(.line \d+\s+)*?move-result [pv]\d+\s+(.line \d+\s+)*?const/16 ([pv]\d+),) 0x2000',
            r'\1 0x0',
            "Bypass Anti-Screen <isSecuredNow>",
            "FlagSecureReason.smali"
        ),
        (
            r'(\s+or-int/lit16 [pv]\d+, [pv]\d+,) 0x2000',
            r'\1 0x0',
            "Bypass Anti-Screen <PhotoViewer|SecretMediaViewer>",
            ["PhotoViewer.smali", "SecretMediaViewer.smali"]
        ),
        (
            r'(invoke-virtual \{([pv]\d+), ([pv]\d+)\}, Landroid/view/SurfaceView;->setSecure\(Z\)V)',
            r'const/4 \3, 0x0\n\n\t\1',
            "Bypass Anti-Screen <setSecure>",
            "StoryViewer.smali"
        ),

        # ---------------- Disable Signature Verification ----------------
        (
            r'(\.method public static getCertificateSHA256Fingerprint\(\)Ljava/lang/String;\n)[\S\s+]*?(\n.end method)',
            r'\1\t.locals 1\n'
            r'    const-string v0, "49C1522548EBACD46CE322B6FD47F6092BB745D0F88082145CAF35E14DCC38E1"\n'
            r'    return-object v0\2',
            "Disable Signature Verification",
            "AndroidUtilities.smali"
        ),

        # ---------------- markStoryAsRead ----------------
        (
            r'(\.method public markStoryAsRead\((JLorg/telegram/tgnet/tl/TL_stories\$StoryItem;|Lorg/telegram/tgnet/tl/TL_stories\$PeerStories;Lorg/telegram/tgnet/tl/TL_stories\$StoryItem;Z)\)Z\n)[\S\s+]*?(\s+return ([pv]\d+)\n.end method)',
            r'\1\t.locals 4\n\tconst/4 \4, 0x0\3',
            "markStoryAsRead",
            "StoriesController.smali"
        ),

        # ---------------- Premium ----------------
        (
            r'(\.method (?:private|public final) isPremium\(J\)Z\n)[\S\s+]*?(\n.end method)',
            r'\1\t.locals 3\n\tconst/4 p1, 0x1\n\treturn p1\2',
            "isPremium ➢ StoriesController",
            "StoriesController.smali"
        ),
        (
            r'(\.method public isPremium\(\)Z\n)[\S\s]*?(\n.end method)',
            r'\1\t.locals 1\n\tconst/4 v0, 0x1\n\treturn v0\2',
            "isPremium ➢ UserConfig",
            "UserConfig.smali"
        ),
        (
            r'(\.method (?:private|public final) isPremiumFeatureAvailable\(I\)Z\n(?:(?!\.end method)[\s\S])*?const/4 v1,) 0x0([\S\s+]*?\n.end method)',
            r'\1 0x1\2',
            "isPremiumFeatureAvailable",
            "ProfileActivity$SearchAdapter.smali"
        ),
        (
            r'(\.method static synthetic access\$3000\(Lorg/telegram/ui/PremiumPreviewFragment;\)Z\n)(?:(?!\.end method)[\s\S])*?iget-boolean [pv]\d+, [pv]\d+, Lorg/telegram/ui/PremiumPreviewFragment;->forcePremium:Z[\S\s+]*?(\s+return ([pv]\d+)\n.end method)',
            r'\1\t.locals 1\n\tconst/4 \3, 0x1\2',
            "forcePremium",
            "PremiumPreviewFragment.smali"
        ),

        # ---------------- Secret Media Enable ----------------
        (
            r'(\.method public getSecretTimeLeft\(\)I\n(?:(?!\.end method)[\s\S])*?const/4 v1,) 0x0([\S\s+]*?\n.end method)',
            r'\1 0x1\2',
            "Secret Media Enable",
            "MessageObject.smali"
        ),
        (
            r'(\.method public isSecretMedia\(\)Z\n(?:(?!\.end method)[\s\S])*?iget-object [pv]\d+, [pv]\d+, Lorg/telegram/messenger/MessageObject;->messageOwner:Lorg/telegram/tgnet/TLRPC\$Message;\s+instance-of [pv]\d+, [pv]\d+, Lorg/telegram/tgnet/TLRPC\$TL_message_secret;\s+)[\S\s+]*?(\n.end method)',
            r'\1const/4 v3, 0x0\n\treturn v3\2',
            "Secret Media Enable",
            "MessageObject.smali"
        ),
        (
            r'(\.method public static isSecretPhotoOrVideo\(Lorg/telegram/tgnet/TLRPC\$Message;\)Z\n(?:(?!\.end method)[\s\S])*?instance-of [pv]\d+, [pv]\d+, Lorg/telegram/tgnet/TLRPC\$TL_message_secret;\s+)[\S\s+]*?(\n.end method)',
            r'\1const/4 v2, 0x0\n\treturn v2\2',
            "Secret Media Enable",
            "MessageObject.smali"
        ),
        (
            r'(\.method public static isSecretMedia\(Lorg/telegram/tgnet/TLRPC\$Message;\)Z\n(?:(?!\.end method)[\s\S])*?instance-of [pv]\d+, [pv]\d+, Lorg/telegram/tgnet/TLRPC\$TL_message_secret;\s+)[\S\s+]*?(\n.end method)',
            r'\1const/4 v2, 0x0\n\treturn v2\2',
            "Secret Media Enable",
            "MessageObject.smali"
        ),

        # ---------------- isSponsored Check ----------------
        (
            r'(\.method public isSponsored\(\)Z\n)[\S\s]*?(\n.end method)',
            r'\1\t.locals 3\n\tconst/4 v0, 0x0\n\treturn v0\2',
            "isSponsored ➢ False",
            "MessageObject.smali"
        ),
        (
            r'(\.method public isSponsoredDisabled\(\)Z\n)[\S\s]*?(\n.end method)',
            r'\1\t.locals 3\n\tconst/4 v0, 0x1\n\treturn v0\2',
            "isSponsoredDisabled ➢ True",
            "MessagesController.smali"
        ),
        (
            r'(\.method private checkPromoInfoInternal\(Z\)V\n)[\S\s]*?(\n.end method)',
            r'\1\t.locals 2\n\treturn-void\2',
            "Remove Proxy Sponsored Channels",
            "MessagesController.smali"
        ),

        # ---------------- isChatNoForwards ----------------
        (
            r'(\.method public isChatNoForwards\((?:J|Lorg/telegram/tgnet/TLRPC\$Chat;)\)Z\n)[\S\s+]*?(\n.end method)',
            r'\1\t.locals 3\n\tconst/4 p1, 0x0\n\treturn p1\2',
            "isChatNoForwards ➢ forceForward",
            "MessagesController.smali"
        ),

        # ---------------- Access Banned Channels [Main] ----------------
        (
            r'(\.method public checkCanOpenChat\(Landroid/os/Bundle;Lorg/telegram/ui/ActionBar/BaseFragment;.*\)Z\n)[\S\s]*?(\n.end method)',
            r'\1\t.locals 3\n\tconst/4 p1, 0x1\n\treturn p1\2',
            "Access Banned Channels [Main]",
            "MessagesController.smali"
        ),

        # ---------------- dnsBooster ( ResolveHostByNameTask ) ----------------
        (
            r'"dns.google.com"',
            r'"one.one.one.one"',
            "+ CloudFlare DNS",
            "ConnectionsManager$ResolveHostByNameTask.smali"
        ),
        (
            r'"https://www.google.com/resolve\?name="',
            r'"https://cloudflare-dns.com/dns-query?name="',
            "+ CloudFlare DNS Resolver",
            "ConnectionsManager$ResolveHostByNameTask.smali"
        ),
        (
            r'(invoke-virtual \{[pv]\d+, ([pv]\d+), ([pv]\d+)\}, Ljava/net/URLConnection;->addRequestProperty\(Ljava/lang/String;Ljava/lang/String;\)V)(\s+(.line \d+\s+)*?const/16 [pv]\d+, 0x3e8)',
            r'\1\n'
            r'    const-string \2, "accept"\n'
            r'    const-string \3, "application/dns-json"\n'
            r'    \1'
            r'    \4',
            "+ CloudFlare Header",
            "ConnectionsManager$ResolveHostByNameTask.smali"
        ),

        # ---------------- dnsBooster ( GoogleDnsLoadTask ) ----------------
        (
            r'"https://dns.google.com/resolve\?name="',
            r'"https://cloudflare-dns.com/dns-query?name="',
            "+ CloudFlare DNS Resolver",
            "ConnectionsManager$GoogleDnsLoadTask.smali"
        ),
        (
            r'("&type=)ANY(&random_padding=")',
            r'\1TXT\2',
            "DNS Type ANY To TXT",
            "ConnectionsManager$GoogleDnsLoadTask.smali"
        ),
        (
            r'(invoke-virtual \{[pv]\d+, ([pv]\d+), ([pv]\d+)\}, Ljava/net/URLConnection;->addRequestProperty\(Ljava/lang/String;Ljava/lang/String;\)V)',
            r'\1\n'
            r'    const-string \2, "accept"\n'
            r'    const-string \3, "application/dns-json"\n'
            r'    \1',
            "+ CloudFlare Header",
            "ConnectionsManager$GoogleDnsLoadTask.smali"
        ),

        # ---------------- updateParams ----------------
        (
            r'(\.method private updateParams\(\)V\n(?:(?!\.end method)[\s\S])*?const/high16 v0,) 0x20000((?:(?!\.end method)[\s\S])*?)const/4 v0, 0x4([\S\s+]*?\n.end method)',
            r'\1 0x80000\2const/16 v0, 0x8\3',
            "updateParams ➢ SpeedBoost",
            "FileLoadOperation.smali"
        ),

        # ---------------- markMessagesAsDeleted ----------------
        (
            r'(\.method public markMessagesAsDeleted\(JIZZ\)Ljava/util/ArrayList;\s+\.locals \d+(\s+\.annotation[\s\S]*?.end annotation)?)',
            r'\1\n'
            r'    sget-boolean v0, Lorg/telegram/abhi/Hook;->candelMessages:Z\n'
            r'    if-eqz v0, :cond_7\n'
            r'    const/4 p1, 0x0\n'
            r'    return-object p1\n'
            r'    :cond_7',
            "markMessagesAsDeleted",
            "MessagesStorage.smali"
        ),
        (
            r'(\.method public markMessagesAsDeleted\(JLjava/util/ArrayList;ZZII\)Ljava/util/ArrayList;\s+\.locals \d+(\s+\.annotation[\s\S]*?.end annotation)?)',
            r'\1\n'
            r'    sget-boolean v0, Lorg/telegram/abhi/Hook;->candelMessages:Z\n'
            r'    if-eqz v0, :cond_7\n'
            r'    const/4 v1, 0x0\n'
            r'    return-object v1\n'
            r'    :cond_7',
            "markMessagesAsDeleted",
            "MessagesStorage.smali"
        ),

        # ---------------- add setTextAndCheck_2 Method ----------------
        (
            r'((\.method public setTextAndCheck)(\(Ljava/lang/CharSequence;ZZ\)V[\S\s]*?)(\s+return-void\n.end method\n))',
            r'\1\n\2_2\3\n'
            r'    invoke-virtual {p0}, Landroid/view/View;->getContext()Landroid/content/Context;\n'
            r'    move-result-object v1\n'
            r'    const-string v0, "Turned off"\n'
            r'    if-eqz p2, :cond_48\n'
            r'    const-string v0, "Turned on"\n'
            r'    :cond_48\n'
            r'    invoke-static {v1, v0, v2}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;\n'
            r'    move-result-object v0\n'
            r'    invoke-virtual {v0}, Landroid/widget/Toast;->show()V\n'
            r'    if-eqz p2, :cond_55\n'
            r'    invoke-static {}, Lorg/telegram/abhi/Hook;->hook()V\n'
            r'    goto :goto_58\n'
            r'    :cond_55\n'
            r'    invoke-static {}, Lorg/telegram/abhi/Hook;->unhook()V\n'
            r'    :goto_58\n\4',
            "add setTextAndCheck_2 Method",
            "TextCell.smali"
        ),
        
        # ---------------- Anti-Delete Messages ----------------
        (
            r'(invoke-virtual \{.*\}, Lorg/telegram/ui/Cells/TextCell;->setTextAndCheck)(\(Ljava/lang/CharSequence;ZZ\)V)',
            r'\1_2\2',
            "Rename setTextAndCheck_2",
            "PremiumPreviewFragment$Adapter.smali"
        ),
        (
            r'sget ([pv]\d+), Lorg/telegram/messenger/R\$string;->ShowAds:I\s+(invoke-static \{.*\}, Lorg/telegram/messenger/LocaleController;->getString\(I\)Ljava/lang/String;\s+move-result-object [pv]\d+)',
            r'const-string \1, "Do Not Delete Messages"',
            "Do Not Delete Messages",
            "PremiumPreviewFragment$Adapter.smali"
        ),
        (
            r'sget ([pv]\d+), Lorg/telegram/messenger/R\$string;->ShowAdsInfo:I\s+(invoke-static \{.*\}, Lorg/telegram/messenger/LocaleController;->getString\(I\)Ljava/lang/String;\s+move-result-object [pv]\d+)',
            r'const-string \1, "After enabling or disabling the feature, ensure you revisit this page for the changes to take effect.\\nMod by Abhi"',
            "Mod by Abhi",
            "PremiumPreviewFragment$Adapter.smali"
        ),
        (
            r'sget ([pv]\d+), Lorg/telegram/messenger/R\$string;->ShowAdsTitle:I\s+(invoke-static \{.*\}, Lorg/telegram/messenger/LocaleController;->getString\(I\)Ljava/lang/String;\s+move-result-object [pv]\d+)',
            r'const-string \1, "Anti-Delete Messages"\n'
            r'    invoke-virtual {v1, \1}, Lorg/telegram/ui/Cells/HeaderCell;->setText(Ljava/lang/CharSequence;)V\n'
            r'    return-void',
            "Anti-Delete Messages",
            "PremiumPreviewFragment$Adapter.smali"
        )
    ]

    Target_Regex = [p[0] for p in scanPatterns]

    for smali_folder in smali_folders:
        for root, _, files in M.os.walk(smali_folder):
            for file in files:
                full_path = M.os.path.join(root, file)
                if file.endswith('.smali'):
                    Smali_Paths.append(full_path)
                if file in Target_Smali:
                    Smali_Files.append(full_path)

    try:
        # ---------------- Multiple Threading ----------------
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

    print(f" {C.G} ✔\n", flush=True)

    print(f"\n{C.X}{C.C} TG Patch, Script by {C.OG}🇮🇳 AbhiTheM0dder 🇮🇳")

    print(f'\n{C_Line}\n')

    allPatterns = scanPatterns + smaliPatterns

    isMatched = {}

    for is_Path, is_idx in Match_Smali:
        if isinstance(is_idx, list):  # Multi Match in Single Smali
            for index in is_idx:
                isMatched.setdefault(index, set()).add(is_Path)
        else:
            isMatched.setdefault(is_idx, set()).add(is_Path)

    for idx, (pattern, replacement, description, target_files) in enumerate(allPatterns):
  
        count_applied = 0
        applied_files= set()

        if target_files:
            Map_Smali = set()
            for Path in Smali_Files:
                if isinstance(target_files, list): # Multi Smali
                    if M.os.path.basename(Path) in target_files:
                        Map_Smali.add(Path)
                else:
                    if M.os.path.basename(Path) == target_files:
                        Map_Smali.add(Path)
        else:
            
            if target_files is None:
                Map_Smali = {X for X, _ in Match_Smali}
            else:
                Map_Smali = isMatched.get(idx, set())

        for File_Path in Map_Smali:
            content = open(File_Path, 'r', encoding='utf-8', errors='ignore').read()

            new_content = M.re.sub(pattern, replacement, content)

            if new_content != content:
                applied_files.add(File_Path)

                count_applied += 1

                open(File_Path, 'w', encoding='utf-8', errors='ignore').write(new_content)

        if count_applied > 0:
            print(f"\n{C.S} Tag {C.E} {C.G}{description}")
            print(f"\n{C.S} Pattern {C.E} {C.OG}➸❥ {C.P}{pattern}")

            for File_Path in applied_files:
                print(f"{C.G}  |\n  └──── {C.CC}~{C.G}$ {C.Y}{M.os.path.basename(File_Path)} {C.G} ✔")

            print(
                f"\n{C.S} Pattern Applied {C.E} {C.OG}➸❥ {C.PN}{count_applied} {C.C}Time/Smali {C.G} ✔\n"
                f"\n{C_Line}\n"
            )

    Hook_Smali(decompile_dir, isAPKEditor)

        
# ---------------- Hook Smali ----------------
def Hook_Smali(decompile_dir, isAPKEditor):

    targetSmali_Dir = M.os.path.join(decompile_dir,
            *(
                ['smali', 'classes'] if isAPKEditor else ['smali']
            )
        )

    Target_Dest = M.os.path.join(targetSmali_Dir, "org", "telegram", "abhi", 'Hook.smali')

    M.os.makedirs(M.os.path.dirname(Target_Dest), exist_ok=True)

    M.shutil.copy(F.Hook_Smali, Target_Dest)
    
    print(f"\n{C.S} Generate {C.E} {C.G}Hook.smali {C.OG}➸❥ {C.Y}{M.os.path.relpath(Target_Dest, decompile_dir)} {C.G} ✔\n")