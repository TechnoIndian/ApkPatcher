<p align="center">
<a href="https://t.me/rktechnoindians"><img title="Made in INDIA" src="https://img.shields.io/badge/MADE%20IN-INDIA-SCRIPT?colorA=%23ff8100&colorB=%23017e40&colorC=%23ff0000&style=for-the-badge"></a>
</p>

<a name="readme-top"></a>


# ApkPatcher


<p align="center"> 
<a href="https://t.me/rktechnoindians"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=800&size=35&pause=1000&color=F74848&center=true&vCenter=true&random=false&width=435&lines=ApkPatcher" /></a>
 </p>


Installation Method
-------
**💢 Requirement PKG 💢**

```bash
termux-setup-storage
pkg update -y
pkg upgrade -y
pkg install python -y
```

**👉🏻 To install ApkPatcher, Run only any one cmd from the Installation Method**

**💢 PYPI ( Just Testing ) 💢**

    pip install ApkPatcherX

[![PyPI](https://img.shields.io/badge/pypi-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)](https://pypi.org/project/ApkPatcherX) [![Version](https://img.shields.io/pypi/v/ApkPatcherX?label=&style=for-the-badge&color=FF8C00&labelColor=FF8C00)](https://pypi.org/project/ApkPatcherX)


**1st. Method**

`💢 For Latest Commit ( From Main  Branch )  💢`

    pip install --force-reinstall https://github.com/TechnoIndian/ApkPatcher/archive/refs/heads/main.zip

`OR`

    pip install --force-reinstall https://github.com/TechnoIndian/ApkPatcher/archive/refs/heads/main.tar.gz

`OR`

    curl -Ls https://github.com/TechnoIndian/Tools/releases/download/Tools/ApkPatcher.sh | bash

**2nd. Method**

    pkg install python git && pip install git+https://github.com/TechnoIndian/ApkPatcher.git


Uninstall ApkPatcher
-----

    pip uninstall ApkPatcherX


# Usage Example


ApkPatcher ( Input Mode )
-----

**Mode `-i` ➸ Smali Patcher ( Input Your APK Path )**

`Default Patch is VPN & SSL Bypass`

    ApkPatcher -i YourApkPath.apk

**Flag: `-a` ➸ Try with APKEditor ( Default APKTool )**

    ApkPatcher -i YourApkPath.apk -a

**Flag: `-c` ➸ Embed Your Captural APK's Certificate**

`With Your Certificate ( Input Your .pem / .crt / .cert Path )`

`If you have already installed your certificate under CA Certificates in your device settings, then you don’t need to use the "-c YourCertificatePath.cert" parameter, because the user certificate is already trusted by network_security_config.xml`

    ApkPatcher -i YourApkPath.apk -c YourCertificatePath.cert

`Multiple Certificate`

    ApkPatcher -i YourApkPath.apk -c /sdcard/HttpCanary/certs/HttpCanary.pem /sdcard/Download/Reqable/reqable-ca.crt /sdcard/Download/ProxyPinCA.crt

**Flag: `-e` ➸ If using emulator on PC**

    ApkPatcher -i YourApkPath.apk -e

**Flag: `-u` ➸ Keep UnSigned APK**

    ApkPatcher -i YourApkPath.apk -u


Smali Patcher ( Additional Flags )
-----

**Flag: `-f` / `-p` / `-p -x` ➸ Flutter & Pairip SSL Bypass**

`For Flutter, Script By  🇮🇳 AbhiTheM0dder 🇮🇳`

    ApkPatcher -i YourApkPath.apk -f

`For Pairip ( UnSigned APK, Use Only in VM / Multi App )`

    ApkPatcher -i YourApkPath.apk -p

`CoreX HooK For Pairip ( Install Directly, Only For [ arm64 ] )`

    ApkPatcher -i YourApkPath.apk -p -x

**Flag: `-D` ➸ Hook Android ID For One Device Login Bypass**

`Input Your 16 Digit Android ID`

    ApkPatcher -i YourApkPath.apk -D 7e9f51f096bd5c83

**Flag: `-pkg` ➸ Spoof Package Detection ( Dex / Manifest / Res )**

    ApkPatcher -i YourApkPath.apk -pkg

**Flag: `-P` ➸ Purchase / Paid / Price**

    ApkPatcher -i YourApkPath.apk -P

**Flag: `-rmss` / `-rmusb` ➸ Bypass Screen / USB Restriction**

`Bypass Screenshot Restriction`

    ApkPatcher -i YourApkPath.apk -rmss

`Bypass USB Debugging`

    ApkPatcher -i YourApkPath.apk -rmusb

**Flag: `-skip` ➸ Skip Patch (e.g., getAcceptedIssuers)**

    ApkPatcher -i YourApkPath.apk -skip getAcceptedIssuers


AES Patcher ( Additional Flags )
-----

**Flag: `-A` ➸ AES MT Logs Inject**

    ApkPatcher -i YourApkPath.apk -A

`Do U Want Separate AES.smali Dex`

    ApkPatcher -i YourApkPath.apk -A -s

**Flag: `-A2` ➸ Algorithm Logs**

    ApkPatcher -i YourApkPath.apk -A2


Spoof Patcher ( Additional Flags )
-----

**Flag: `-r` ➸ Random / Fake / Spoof Device Info**

    ApkPatcher -i YourApkPath.apk -r

`Input Your 16 Digit Custom Android ID`

    ApkPatcher -i YourApkPath.apk -r -D 7e9f51f096bd5c83


Ads Patcher ( Additional Flags )
-----

**Flag: `-rmads` ➸ Remove Ads**

    ApkPatcher -i YourApkPath.apk -rmads


TG Patcher ( Additional Flags )
-----

**Flag: `-t` ➸ Telegram / Plus Patch, Script By  🇮🇳 AbhiTheM0dder 🇮🇳**

    ApkPatcher -i YourApkPath.apk -t


Pine Hook ( Additional Flags )
-----

**Flag: `-pine -l` ➸ Pine Hook ( Input Path of Xposed & LSP Module )**

`Mutil Path Supported, But module path should not contain space or symbols.`

    ApkPatcher -i YourApkPath.apk -pine -l NoVPNDetect.apk just.trust.me.apk


ApkPatcher ( Merge Mode )
-----

**Mode `-m` ➸ Anti-Split ( Only Merge APK )**

`Supported Extensions ( .apks / .apkm / .xapk )`

    ApkPatcher -m YourApkPath.apks


ApkPatcher ( Credits Mode )
-----

**Mode `-C` ➸ Credits**

    ApkPatcher -C


ApkPatcher Help
-----

    ApkPatcher -h


ApkPatcher Other Patch Flags
-----

    ApkPatcher -O


# NOTE


## 🇮🇳 Welcome By Techno India 🇮🇳

[![Telegram](https://img.shields.io/badge/TELEGRAM-CHANNEL-red?style=for-the-badge&logo=telegram)](https://t.me/rktechnoindians)
  </a><p>
[![Telegram](https://img.shields.io/badge/TELEGRAM-OWNER-red?style=for-the-badge&logo=telegram)](https://t.me/RK_TECHNO_INDIA)
</p>