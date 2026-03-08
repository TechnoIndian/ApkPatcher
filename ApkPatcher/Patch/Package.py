from ..MODULES import IMPORT; M = IMPORT()


class P:
    # ---------------- Spoof Package Detection ----------------
    Find_String = ['com.noshufou.android.su.elite', 'com.noshufou.android.su', 'eu.chainfire.supersu', 'com.koushikdutta.superuser', 'com.thirdparty.superuser', 'com.yellowes.su', 'com.topjohnwu.magisk', 'com.kingroot.kinguser', 'com.kingo.root', 'com.smedialink.oneclickroot', 'com.zhiqupk.root.global', 'com.alephzain.framaroot', 'com.koushikdutta.rommanager.license', 'com.koushikdutta.rommanager', 'com.dimonvideo.luckypatcher', 'com.chelpus.lackypatch', 'com.ramdroid.appquarantinepro', 'com.ramdroid.appquarantine', 'com.android.vending.billing.InAppBillingService.COIN', 'com.android.vending.billing.InAppBillingService.LUCK', 'com.chelpus.luckypatcher', 'com.blackmartalpha', 'org.blackmart.market', 'com.allinone.free', 'com.repodroid.app', 'org.creeplays.hack', 'com.baseappfull.fwd', 'com.zmapp', 'com.dv.marketmod.installer', 'org.mobilism.android', 'com.android.wp.net.log', 'com.android.camera.update', 'cc.madkite.freedom', 'com.solohsu.android.edxp.manager', 'org.meowcat.edxposed.manager', 'com.xmodgame', 'com.cih.game_cih', 'com.charles.lpoqasert', 'catch_.me_.if_.you_.can_', 'com.devadvance.rootcloakplus', 'com.devadvance.rootcloak', 'com.saurik.substrate', 'com.zachspong.temprootremovejb', 'com.amphoras.hidemyrootadfree', 'com.amphoras.hidemyroot', 'com.formyhm.hiderootPremium', 'com.formyhm.hideroot', 'me.weishu.exp', 'moe.shizuku.privileged.', 'com.guoshi.httpcanary.premium', 'com.guoshi.httpcanary', 'com.reqable.android', 'com.network.proxy', 'com.sniffer3', 'com.sniffer2', 'com.sniffer', 'com.datacapture.pro', 'com.black.canary', 'org.httpcanary.pro', 'app.greyshirts.sslcapture', 'com.evbadroid.proxymon', 'com.minhui.networkcapture.pro', 'com.minhui.networkcapture', 'com.minhui.wifianalyzer', 'com.packagesniffer.frtparlak', 'com.evbadroid.wicapdemo', 'jp.co.taosoftware.android.packetcapture', 'com.andriell.multicast_sniffer', 'com.emanuelef.remote_capture', 'de.stefanpledl.localcast', 'bin.mt.plus.canary', 'bin.mt.plus', 'ru.maximoff.apktool', 'idm.internet.download.manager.plus', 'idm.internet.download.manager', 'com.applisto.appcloner', 'org.lsposed.lspatch', 'me.jsonet.jshook', 'br.tiagohm.restler', 'com.replit.app', 'io.virtualapp', 'de.robv.android.xposed']

    Match_Regex = f'"({"|".join(Find_String[:-1])}|{Find_String[-1]}.*)"'

    Menifest_Regex = rf'(\s+<package[^>]*android:name={Match_Regex}[^>]*/>)'


    # ---------------- Generate Hash ----------------
    def Hash(self, CA_Cert):

        from asn1crypto import x509

        f = open(CA_Cert,'rb').read()

        if f.startswith(b'-----'): f = M.base64.b64decode(''.join(f.decode().splitlines()[1:-1]))
        CERT = x509.Certificate.load(f)['tbs_certificate']['subject_public_key_info'].dump()

        sha1 = M.base64.b64encode(M.hashlib.sha1(CERT).digest()).decode()
        sha256 = M.base64.b64encode(M.hashlib.sha256(CERT).digest()).decode()

        return sha1, sha256