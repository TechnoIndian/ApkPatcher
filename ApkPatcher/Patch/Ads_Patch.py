from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()

C_Line = f"{C.CC}{'_' * 61}"


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


# ---------------- Ads Smali Patch ----------------
def Ads_Smali_Patch(smali_folders):

    Smali_Paths, matching_files = [], []

    patterns = [
        (
            r'"(com.google.android.play.core.appupdate.protocol.IAppUpdateService|Theme.Dialog.Alert|com.google.android.play.core.install.BIND_UPDATE_SERVICE)"',
            r'""',
            "Update Disable"
        ),
        (
            r'(invoke(?!.*(close|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/[^;]+;->(.*(load|show).*)\([^)]*\)V)|(invoke(?!.*(close|Deactiv|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop|Throw)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/[^;]+;->(request.*|(.*(activat|Banner|build|Event|exec|header|html|initAd|initi|JavaScript|Interstitial|load|log|MetaData|metri|Native|onAd|propert|report|response|Rewarded|show|trac|url|(fetch|refresh|render|video)Ad).*)|.*Request)\([^)]*\)V)|(invoke(?!.*(close|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/[^;]+;->((.*(Banner|initAd|Interstitial|load|Native|onAd|Rewarded|show|(fetch|refresh|render|request|video)Ad).*))\([^)]*\)V)|invoke-.*\{.*\}, L[^;]+;->(loadAd|requestNativeAd|showInterstitial|fetchad|fetchads|onadloaded|requestInterstitialAd|showAd|loadAds|AdRequest|requestBannerAd|loadNextAd|createInterstitialAd|setNativeAd|loadBannerAd|loadNativeAd|loadRewardedAd|loadRewardedInterstitialAd|loadAds|loadAdViewAd|showInterstitialAd|shownativead|showbannerad|showvideoad|onAdFailedToLoad)\([^)]*\)V|invoke-[^{]+ \{[^\}]*\}, Lcom[^;]+;->requestInterstitialAd\([^)]*\)V|invoke-[^{]+ \{[^\}]*\}, Lcom[^;]+;->loadAds\([^)]*\)V|invoke-[^{]+ \{[^\}]*\}, Lcom[^;]+;->loadAd\([^)]*\)V|invoke-[^{]+ \{[^\}]*\}, Lcom[^;]+;->requestBannerAd\([^)]*\)V|invoke-[^{]+ \{[pv]\d\}, Lcom/facebook[^;]+;->show\([^)]*\)V|invoke-[^{]+ \{[pv]\d\}, Lcom/google[^;]+;->show\([^)]*\)V',
            r'nop',
            "Ads Regex 1"
        ),
        (
            r'(invoke(?!.*(close|Deactiv|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop|Throw)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/[^;]+;->(request.*|(.*(activat|Banner|build|Event|exec|header|html|initAd|initi|JavaScript|Interstitial|load|log|MetaData|metri|Native|(can|get|is|has|was)Ad|propert|report|response|Rewarded|show|trac|url|(fetch|refresh|render|video)Ad).*)|.*Request)\([^)]*\)Z[^>]*?)move-result ([pv]\d+)|(invoke(?!.*(close|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/[^;]+;->((.*(Banner|initAd|Interstitial|load|Native|(can|get|has|is|was)Ad|Rewarded|show|(fetch|refresh|render|request|video)Ad).*))\([^)]*\)Z[^>]*?)move-result ([pv]\d+)',
            r'const/4 \9, 0x0',
            "Ads Regex 2"
        ),
        (
            r'(invoke(?!.*(close|Destroy|Dismiss|Disabl|error|player|remov|expir|fail|hide|skip|stop)).*/(adcolony|admob|ads|adsdk|aerserv|appbrain|applovin|appodeal|appodealx|appsflyer|bytedance/sdk/openadsdk|chartboost|flurry|fyber|hyprmx|inmobi|ironsource|mbrg|mbridge|mintegral|moat|mobfox|mobilefuse|mopub|my/target|ogury|Omid|onesignal|presage|smaato|smartadserver|snap/adkit|snap/appadskit|startapp|taboola|tapjoy|tappx|vungle)/[^;]+;->(.*(load|show).*)\([^)]*\)Z[^>]*?)move-result ([pv]\d+)',
            r'const/4 \6, 0x0',
            "Ads Regex 3"
        ),
        (
            r'(\.method\s(public|private|static)\s\b(?!\babstract|native\b)[^(]*?loadAd\([^)]*\)V)',
            r'\1\n\treturn-void',
            "Ads Regex 4"
        ),
        (
            r'(\.method\s(public|private|static)\s\b(?!\babstract|native\b)[^(]*?loadAd\([^)]*\)Z)',
            r'\1\n\tconst/4 v0, 0x0\n\treturn v0',
            "Ads Regex 5"
        ),
        (
            r'(invoke[^{]+ \{[^\}]*\}, L[^(]*loadAd\([^)]*\)[VZ])|(invoke[^{]+ \{[^\}]*\}, L[^(]*gms.*\>(loadUrl|loadDataWithBaseURL|requestInterstitialAd|showInterstitial|showVideo|showAd|loadData|onAdClicked|onAdLoaded|isLoading|loadAds|AdLoader|AdRequest|AdListener|AdView)\([^)]*\)V)',
            r'#',
            "Ads Regex 6"
        ),
        (
            r'\.method [^(]*(loadAd|requestNativeAd|showInterstitial|fetchad|fetchads|onadloaded|requestInterstitialAd|showAd|loadAds|AdRequest|requestBannerAd|loadNextAd|createInterstitialAd|setNativeAd|loadBannerAd|loadNativeAd|loadRewardedAd|loadRewardedInterstitialAd|loadAds|loadAdViewAd|showInterstitialAd|shownativead|showbannerad|showvideoad|onAdFailedToLoad)\([^)]*\)V\s+\.locals \d+[\s\S]*?\.end method',
            r'#',
            "Ads Regex 7"
        ),
        (
            r'"ca-app-pub-\d{16}/\d{10}"',
            r'"ca-app-pub-0000000000000000/0000000000"',
            "Ads Regex 8"
        ),
        (
            r'"(http.*|//.*)(61.145.124.238|-ads.|.ad.|.ads.|.analytics.localytics.com|.mobfox.com|.mp.mydas.mobi|.plus1.wapstart.ru|.scorecardresearch.com|.startappservice.com|/ad.|/ads|ad-mail|ad.*_logging|ad.api.kaffnet.com|adc3-launch|adcolony|adinformation|adkmob|admax|admob|admost|adsafeprotected|adservice|adtag|advert|adwhirl|adz.wattpad.com|alta.eqmob.com|amazon-*ads|amazon.*ads|amobee|analytics|applovin|applvn|appnext|appodeal|appsdt|appsflyer|burstly|cauly|cloudfront|com.google.android.gms.ads.identifier.service.START|crashlytics|crispwireless|doubleclick|dsp.batmobil.net|duapps|dummy|flurry|gad|getads|google.com/dfp|googleAds|googleads|googleapis.*.ad-*|googlesyndication|googletagmanager|greystripe|gstatic|inmobi|inneractive|jumptag|live.chartboost.com|madnet|millennialmedia|moatads|mopub|native_ads|pagead|pubnative|smaato|supersonicads|tapas|tapjoy|unityads|vungle|zucks).*"',
            r'"="',
            "Ads Regex 9"
        ),
        (
            r'"(http.*|//.*)(61\.145\.124\.238|/2mdn\.net|-ads\.|\.5rocks\.io|\.ad\.|\.adadapted|\.admitad\.|\.admost\.|\.ads\.|\.aerserv\.|\.airpush\.|\.batmobil\.|\.chartboost\.|\.cloudmobi\.|\.conviva\.|\.dov-e\.com|\.fyber\.|\.mng-ads\|\.mydas\.|\.predic\.|\.talkingdata\.|\.tapdaq\.|\.tele\.fm|\.unity3d\.|\.unity\.|\.wapstart\.|\.xdrig\.|\.zapr\.|\/ad\.|\/ads|a4\.tl|accengage|ad4push|ad4screen|ad-mail|ad\..*_logging|ad\.api\.kaffnet\.|ad\.cauly\.co\.|adbuddiz|adc3-launch|adcolony|adfurikun|adincube|adinformation|adkmob|admax\.|admixer|admob|admost|ads\.mdotm\.|adsafeprotected|adservice|adsmogo|adsrvr|adswizz|adtag|adtech\.de|advert|adwhirl|adz\.wattpad\.|alimama\.|alta\.eqmob\.|amazon-.*ads|amazon\..*ads|amobee|analytics|anvato|appboy|appbrain|applovin|applvn|appmetrica|appnext|appodeal|appsdt|appsflyer|apsalar|avocarrot|axonix|banners-slb\.mobile\.yandex\.net|banners\.mobile\.yandex\.net|brightcove\.|burstly|cauly|cloudfront|cmcm\.|com\.google\.android\.gms\.ads\.identifier\.service\.START|comscore|contextual\.media\.net|crashlytics|crispwireless|criteo\.|dmtry\.|doubleclick|duapps|dummy|flurry|fwmrm|gad|getads|gimbal|glispa|google\.com\/dfp|googleAds|googleads|googleapis\..*\.ad-.*|googlesyndication|googletagmanager|greystripe|gstatic|heyzap|hyprmx|iasds01|inmobi|inneractive|instreamatic|integralads|jumptag|jwpcdn|jwpltx|jwpsrv|kochava|localytics|madnet|mapbox|mc\.yandex\.ru|media\.net|metrics\.|millennialmedia|mixpanel|mng-ads\.com|moat\.|moatads|mobclix|mobfox|mobpowertech|moodpresence|mopub|native_ads|nativex\.|nexage\.|ooyala|openx\.|pagead|pingstart|prebid|presage\.io|pubmatic|pubnative|rayjump|saspreview|scorecardresearch|smaato|smartadserver|sponsorpay|startappservice|startup\.mobile\.yandex\.net|statistics\.videofarm\.daum\.net|supersonicads|taboola|tapas|tapjoy|tapylitics|target\.my\.com|teads\.|umeng|unityads|vungle|zucks).*"',
            r'"127.0.0.1"',
            "Ads Regex 10"
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

    Target_Regex = [p[0] for p in patterns]

    for smali_folder in smali_folders:
        for root, _, files in M.os.walk(smali_folder):
            for file in files:
                if file.endswith('.smali'):
                    Smali_Paths.append(M.os.path.join(root, file))

    try:
        # ---------------- Multiple Threading ----------------
        with M.Manager() as MT:
            Count = MT.Value('i', 0); Lock = MT.Lock()
            with M.Pool(M.cpu_count()) as PL:
                matching_files = [path for path in PL.starmap(Regex_Scan, [(Smali_Path, Target_Regex, Count, Lock) for Smali_Path in Smali_Paths]) if path]

    except Exception:
        # ---------------- Single Threading ----------------
        Count = [0]
        for Smali_Path in Smali_Paths:
            result = Regex_Scan(Smali_Path, Target_Regex, Count, None)

            if result:
                matching_files.append(result)

    print(f" {C.G} ✔", flush=True)

    print(f'\n{C_Line}\n')

    if matching_files:
        for pattern, replacement, description in patterns:
            count_applied, applied_files = 0, set()

            for file_path in matching_files:
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