from .C_M import CM; C = CM()

class ArgumentParser:
    def parse_arguments(self):
        class CustomArgumentParser(C.argparse.ArgumentParser):
            def error(self, message):
                suggestion = ""
                for action in self._actions:
                    if action.option_strings and any(option in message for option in action.option_strings):
                        if action.dest == 'input':
                            suggestion = f'\n{C.lb}[ {C.y}FYI ! {C.lb}] {C.g}Make Sure There Is "No Extra Space" In The Folder/Apk Name In The Input Text. If Yes, Then Remove Extra Space & Correct It By Renaming It.\n\n\n{C.lb}[ {C.pr}* {C.lb}] {C.c}With Your Certificate ( Input Your pem/crt/cert Path )\n\n\n{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher -i YourApkPath.apk {C.rkj}-c {C.y}certificate.cert\n\n\n{C.lb}[ {C.pr}* {C.lb}] {C.c}If Apk is Flutter Then Use Additional Flag {C.rkj}-f\n\n\n{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher -i YourApkPath.apk -c certificate.cert {C.rkj}-f\n\n\n{C.lb}[ {C.pr}* {C.lb}] {C.c}Pairip CERT SSL Bypass ( Without Sign Apk Use Only in VM/Multi_App ){C.c}\n\n\n{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher -i YourApkPath.apk -c certificate.cert {C.rkj}-p\n\n\n{C.lb}[ {C.pr}* {C.lb}] {C.c}Hook Android ID For One Device Login Bypass Use {C.rkj}-D {C.c}Flag (Input Your Original 16 Digit Android ID)\n\n\n{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher -i YourApkPath.apk {C.rkj}-D {C.y}7e9f51f096bd5c83\n\n\n{C.lb}[ {C.pr}* {C.lb}] {C.c}If you are using an Emulator in PC Then Use Additional Flag {C.rkj}-e\n\n\n{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher -i YourApkPath.apk -c certificate.cert {C.rkj}-e\n\n\n{C.lb}[ {C.pr}* {C.lb}] {C.c}If Failed SigCopy Use Another Method ( default apksigcopier ) {C.rkj}-p {C.rkj}-s2\n\n\n{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher -i YourApkPath.apk -c certificate.cert {C.rkj}-p {C.rkj}-s2\n'
                        elif action.dest == 'Merge':
                            suggestion = f'\n{C.lb}[ {C.y}INFO {C.lb}] {C.c}Only Merge Apk\n\n\n{C.lb}[ {C.y}INFO {C.lb}] {C.c}Merge Extension {C.y}( .apks/.xapk/.apkm )\n\n\n{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher {C.rkj}-m {C.g}Your_Apk_Path.apks\n'
                        elif action.dest == 'AES':
                            suggestion = f'\n{C.lb}[ {C.y}INFO {C.lb}] {C.c}AES MT Logs Inject\n\n\n{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher -A Your_Apk_Path.apk\n\n\n{C.lb}[ {C.y}INFO {C.lb}] {C.c}Do U Want Separate AES.smali Dex Use Flags {C.rkj}-s\n\n\n{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher -A Your_Apk_Path.apk {C.rkj}-s\n'
                        elif action.dest == 'Ads':
                            suggestion = f'\n{C.lb}[ {C.y}INFO {C.lb}] {C.c}Ads Remove/Patching\n\n\n{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher -a Your_Apk_Path.apk\n'
                        elif action.dest == 'Random_Info':
                            suggestion = f'\n{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher -r Your_Apk_Path.apk\n\n\n{C.lb}[ {C.y}INFO {C.lb}] {C.c}Hook Android ID For One Device Login Bypass Use {C.rkj}-D {C.c}Flag (Input Your Original 16 Digit Android ID)\n\n\n{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher -A Your_Apk_Path.apk {C.rkj}-D {C.y}7e9f51f096bd5c83\n'
                        break

                exit(f'\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} {message}\n\n{suggestion}')

        parser = CustomArgumentParser(description=f'{C.c}ApkPatcher Script') if any(arg.startswith('-') for arg in C.sys.argv[1:]) else C.argparse.ArgumentParser(description=f'{C.c}ApkPatcher Script')
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-i', dest='input', help=f'{C.y}➸{C.g} Input APK Path...{C.c}')
        group.add_argument('-m', dest='Merge', help=f'{C.y}➸{C.g} Anti-Split ( Only Merge Apk ){C.c}')
        group.add_argument('-A', dest='AES', help=f'{C.y}➸{C.g} AES MT Logs Inject{C.c}')
        group.add_argument('-a', dest='Ads', help=f'{C.y}➸{C.g} Ads Remove/Patching{C.c}')
        group.add_argument('-r', dest='Random_Info', help=f'{C.y}➸{C.g} Random/Fake Device Info{C.c}')
        group.add_argument('-C', dest='Credits_Instruction', action='store_true', help=f'{C.y}➸{C.g} Show Instructions & Credits{C.c}')
    
        parser.add_argument('-c', dest='CA_Certificate', type=str, nargs='*', help=f"{C.y}➸{C.g} Input Your HttpCanary/Reqable/ProxyPin etc. Capture Apk's CA-Certificate{C.c}")
        parser.add_argument('-D', dest='Android_ID', type=str, help=f"{C.y}➸{C.g} Custom Android ID ( Input Your Android ID ){C.c}")
        parser.add_argument('-f', dest='Flutter', action='store_true', help=f'{C.y}➸{C.g} Flutter SSL Bypass ( With Smali Patch ){C.c}')
        parser.add_argument('-p', dest='Pairip', action='store_true', help=f'{C.y}➸{C.g} Pairip CERT SSL Bypass ( Without Sign Apk Use Only in VM/Multi_App ){C.c}')
        parser.add_argument('-S', dest='AES_MS', action='store_true', help=f'{C.y}➸{C.g} Do U Want Separate AES.smali Dex{C.c}')
        parser.add_argument('-e', dest='For_Emulator', action='store_true', help=f'{C.y}➸{C.g} If you are using an emulator in PC then use it the "-e" additional flag{C.c}')
        parser.add_argument('-s2', dest='SigCopy2', action='store_true', help=f'{C.y}➸{C.g} If Failed SigCopy Use Another Method ( default apksigcopier ){C.r}')

        return parser.parse_args()