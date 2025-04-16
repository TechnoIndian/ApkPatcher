<p align="center">
<a href="https://t.me/rktechnoindians"><img title="Made in INDIA" src="https://img.shields.io/badge/MADE%20IN-INDIA-SCRIPT?colorA=%23ff8100&colorB=%23017e40&colorC=%23ff0000&style=for-the-badge"></a>
</p>

<a name="readme-top"></a>


# ApkPatcher


<p align="center"> 
<a href="https://t.me/rktechnoindians"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=800&size=35&pause=1000&color=F74848&center=true&vCenter=true&random=false&width=435&lines=ApkPatcher" /></a>
 </p>

Install
-------

**ApkPatcher Method 1**

    curl -L -o ApkPatcher.sh https://github.com/TechnoIndian/ApkPatcher/releases/download/ApkPatcher/ApkPatcher.sh && chmod +x ApkPatcher.sh && ./ApkPatcher.sh

**ApkPatcher Method 2**

    pkg install python git && pip install git+https://github.com/TechnoIndian/ApkPatcher.git


Usage
-----

**ApkPatcher**

**Mode -i ➸ Smali Patcher (Input Your Apk Path)**

    ApkPatcher -i YourApkPath.apk
    
`With Your Certificate ( Input Your pem/ crt / cert Path )`

    ApkPatcher -i YourApkPath.apk -c certificate.cert

`Multiple Certificate`

    ApkPatcher -i YourApkPath.apk -c /sdcard/HttpCanary/certs/HttpCanary.pem /sdcard/Download/Reqable/reqable-ca.crt /sdcard/Download/ProxyPinCA.crt

`If you are using an emulator then use it the '-e' additional flag  👉 Note, you can place '-e' flag anywhere behind your apk path and if you are using any flags like '-A', '-a', '-r' and if you are using emulator then you have to use -e flag along with these too.`

    ApkPatcher -i YourApkPath.apk -e -c certificate.cert

**Mode -i & -f ➸ Flutter SSL & Smali Patcher**

    ApkPatcher -i YourApkPath.apk -f

`With Your Certificate ( Input Your pem/ crt / cert Path )`

    ApkPatcher -i YourApkPath.apk -f -c certificate.cert

**Mode -i & -D ➸ Android ID & Smali Patcher**

`With Your Android ID ( Input Your Custom 16 Digit Android ID )`

    ApkPatcher -i YourApkPath.apk -D 7e9f51f096bd5c83

**Mode -i & -c -D -f ➸ Smali Patcher**

    ApkPatcher -i YourApkPath.apk -D 7e9f51f096bd5c83 -c /sdcard/certificate.cert -f

**Mode -i & -p Pairip SSL Bypass**

    ApkPatcher -i YourApkPath.apk -p

**Mode -i & -P ➸ Purchase/Paid/Price**

    ApkPatcher -i YourApkPath.apk -P

**Mode -i & -skip ➸ Skip Patch (e.g., getAcceptedIssuers)**

    ApkPatcher -i YourApkPath.apk -skip getAcceptedIssuers

**Mode -m ➸ Only Merge Apk**

    ApkPatcher -m YourApkPath.apk

**Mode -L ➸ AES Logs Inject**

`AES MT Logs Inject`

    ApkPatcher -L YourApkPath.apk

`Do U Want Separate AES.smali Dex`

    ApkPatcher -L YourApkPath.apk -S

**Mode -a ➸ Ads Remove/Patching**

`Ads Remove/Patching`

    ApkPatcher -rm YourApkPath.apk

**Mode -r ➸ Random/Fake Device Info**

`Random/Fake Device Info`

    ApkPatcher -r YourApkPath.apk

`With Your Android ID ( Input Your Custom 16 Digit Android ID )`

    ApkPatcher -r YourApkPath.apk -D 7e9f51f096bd5c83

**Mode -C ➸ Credits & Instruction**

    ApkPatcher -C
    
**Mode -h ➸ Help**

    ApkPatcher -h

Note
----

## 🇮🇳 Welcome By Techno India 🇮🇳

[![Telegram](https://img.shields.io/badge/TELEGRAM-CHANNEL-red?style=for-the-badge&logo=telegram)](https://t.me/rktechnoindians)
  </a><p>
[![Telegram](https://img.shields.io/badge/TELEGRAM-OWNER-red?style=for-the-badge&logo=telegram)](https://t.me/RK_TECHNO_INDIA)
</p>
