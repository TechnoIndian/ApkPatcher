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

    termux-setup-storage && pkg update -y && pkg upgrade -y && pkg install python -y

**👉🏻 To install ApkPatcher, Run only any one cmd from the Installation Method**

**💢 PYPI ( Just Testing ) 💢**

    pip install ApkPatcherX

[![PyPI](https://img.shields.io/badge/pypi-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)](https://pypi.org/project/ApkPatcherX) [![Version](https://img.shields.io/pypi/v/ApkPatcherX?label=&style=for-the-badge&color=FF8C00&labelColor=FF8C00)](https://pypi.org/project/ApkPatcherX)


**1st. Method**

`💢 For Latest Commit ( From Main  Branch )  💢`

    pip install --force-reinstall https://github.com/TechnoIndian/ApkPatcher/archive/refs/heads/main.zip

`Or`

    pip install --force-reinstall https://github.com/TechnoIndian/ApkPatcher/archive/refs/heads/main.tar.gz

`Or`

    curl -Ls https://github.com/TechnoIndian/Tools/releases/download/Tools/ApkPatcher.sh | bash

**2nd. Method**

    pkg install python git && pip install git+https://github.com/TechnoIndian/ApkPatcher.git


Uninstall ApkPatcher
-----

    pip uninstall ApkPatcherX


Usage
-----

**ApkPatcher**

**Mode -i ➸ Smali Patcher (Input Your Apk Path)**

    ApkPatcher -i YourApkPath.apk
    
`With Your Certificate ( Input Your pem/ crt / cert Path )`

    ApkPatcher -i YourApkPath.apk -c YourCertificatePath.cert

`Multiple Certificate`

    ApkPatcher -i YourApkPath.apk -c /sdcard/HttpCanary/certs/HttpCanary.pem /sdcard/Download/Reqable/reqable-ca.crt /sdcard/Download/ProxyPinCA.crt

`If using emulator on PC then use Flag: -e`

    ApkPatcher -i YourApkPath.apk -e -c YourCertificatePath.cert

**Mode -i & -f / -p ➸ Flutter & Pairip SSL Bypass**

    ApkPatcher -i YourApkPath.apk -f

`For Pairip`

    ApkPatcher -i YourApkPath.apk -p

`With Your Certificate ( Input Your pem / crt / cert Path )`

    ApkPatcher -i YourApkPath.apk -f -p -c YourCertificatePath.cert

**Mode -i & -D ➸ Android ID & Smali Patcher**

`With Your Android ID ( Input Your Custom 16 Digit Android ID )`

    ApkPatcher -i YourApkPath.apk -D 7e9f51f096bd5c83

**Mode -i & -pkg Spoof Package Detection (Dex/Manifest/Res)**

    ApkPatcher -i YourApkPath.apk -pkg

**Mode -i & -P ➸ Purchase/Paid/Price**

    ApkPatcher -i YourApkPath.apk -P

**Mode -i & --rmads / rmsc / -rmu ➸ Bypass Ads & Screenshot / USB Restriction**

`Remove Ads Flag: -rmads`

    ApkPatcher -i YourApkPath.apk -rmads

`Bypass Screenshot Restriction Flag: -rmsc`

    ApkPatcher -i YourApkPath.apk -rmsc

`Bypass USB Debugging Permission Flag: -rmu`

    ApkPatcher -i YourApkPath.apk -rmu

**Mode -i & -skip ➸ Skip Patch (e.g., getAcceptedIssuers)**

    ApkPatcher -i YourApkPath.apk -skip getAcceptedIssuers

**Mode -i & -A ➸ AES Logs Inject**

`AES MT Logs Inject`

    ApkPatcher -i YourApkPath.apk -A

`Do U Want Separate AES.smali Dex`

    ApkPatcher -i YourApkPath.apk -A -s

**Mode i & -r ➸ Random/Fake Device Info**

`Random/Fake Device Info`

    ApkPatcher -i YourApkPath.apk -r

`With Your Android ID ( Input Your Custom 16 Digit Android ID )`

    ApkPatcher -i YourApkPath.apk -r -D 7e9f51f096bd5c83

**Mode -m ➸ Only Merge Apk**

    ApkPatcher -m YourApkPath.apk

**Mode -C ➸ Credits & Instruction**

    ApkPatcher -C
    
**Mode -h ➸ Help**

    ApkPatcher -h

**Mode -O ➸ Other Patch Flags**

    ApkPatcher -O

Note
----

## 🇮🇳 Welcome By Techno India 🇮🇳

[![Telegram](https://img.shields.io/badge/TELEGRAM-CHANNEL-red?style=for-the-badge&logo=telegram)](https://t.me/rktechnoindians)
  </a><p>
[![Telegram](https://img.shields.io/badge/TELEGRAM-OWNER-red?style=for-the-badge&logo=telegram)](https://t.me/RK_TECHNO_INDIA)
</p>
