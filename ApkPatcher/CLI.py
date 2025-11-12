from .ANSI_COLORS import ANSI; C = ANSI()
from .MODULES import IMPORT; M = IMPORT()

from ApkPatcher.Utils.Files_Check import __version__


Tag = f"\n{C.CC}————|———————|————{C.G}•❀ {C.OG}Tag {C.G}❀•{C.CC}————|———————|————\n"

FE = f"{C.P}\n   |\n   ╰{C.CC}┈{C.OG}➢ {C.G}ApkPatcher"

EX = f"{FE} -i Your_Apk_Path.apk {C.OG}"


class CustomArgumentParser(M.argparse.ArgumentParser):
    # ---------------- Error Handling ----------------
    def error(self, message):
        suggestion = ""
        for action in self._actions:
            if action.option_strings and any(option in message for option in action.option_strings):
                if action.dest == 'input':
                    suggestion = (
                        f'\n{C.FYI}{C.G} Make Sure There Is "No Extra Space" In The Folder / APK Name In The Input Text. If Yes, Then Remove Extra Space & Correct It By Renaming It.\n\n'
                        f'\n{C.INFO} With Your Certificate Flag: {C.OG}-c {C.P}( Input Your pem/crt/cert Path ){EX}-c {C.Y}certificate.cert\n\n'
                        f'\n{C.INFO} If you are using an Emulator in PC Then Use Flag: {C.OG}-e{EX}-c {C.Y}certificate.cert {C.OG}-e\n'
                    )

                elif action.dest == 'Merge':
                    suggestion = (
                        f'\n{C.INFO} Only Merge APK\n\n'
                        f'\n{C.INFO} Merge Extension {C.Y}( .apks/.xapk/.apkm )'
                        f'\n{FE}{C.OG} -m {C.G}Your_Apk_Path.apks\n'
                    )

                break

        exit(
            f'\n{C.ERROR} {message}\n'
            f'\n{suggestion}'
        )

    # ---------------- Print Help ----------------
    def print_help(self):

        super().print_help()

        print(f"\n{C.INFO} ApkPatcher Default Patch is VPN & SSL Bypass, Show Other Patch Flags List with: {C.G}ApkPatcher -O{C.C}\n")

    # ---------------- Other Patch ----------------
    def Other_Patch(self):
        print(
            f"""\n{C.X}{C.C} Other Patch Flags Help ( Keep Sequence in Mind )

 <Flags>                 {C.G}─•❀•❀ {C.C}Info Patch {C.G}❀•❀•─ {C.OG}

  -A, {C.C}--AES_Logs        {C.Y} ➸ {C.G}AES Logs Inject {C.OG}
  -D, {C.C}--Android_ID      {C.Y} ➸ {C.G}Hook Android ID for One Device Login Bypass {C.OG}
  -f, {C.C}--Flutter         {C.Y} ➸ {C.G}Flutter SSL Bypass {C.OG}
  -p, {C.C}--Pairip          {C.Y} ➸ {C.G}Pairip CERT SSL Bypass {C.OG}
  -P, {C.C}--Purchase        {C.Y} ➸ {C.G}Purchase / Paid / Price {C.OG}
  -r, {C.C}--Random_Info     {C.Y} ➸ {C.G}Fake Device Info {C.OG}
  -rmads, {C.C}--Remove_Ads  {C.Y} ➸ {C.G}Bypass Ads {C.OG}
  -rmsc, {C.C}--Remove_SC    {C.Y} ➸ {C.G}Bypass Screenshot Restriction {C.OG}
  -rmusb, {C.C}--Remove_USB  {C.Y} ➸ {C.G}Bypass USB Debugging {C.OG}
  -pkg, {C.C}--Spoof_PKG     {C.Y} ➸ {C.G}Spoof Package Detection {C.OG}
  -skip {C.C}[Skip_Patch ...]{C.Y} ➸ {C.G}Skip Specific Patches {C.P}( e.g. getAcceptedIssuers ) {C.OG}
  -s, {C.C}--AES_S           {C.Y} ➸ {C.G}Do U Want Separate AES.smali Dex {C.OG}
  -x, {C.C}--Hook_CoreX      {C.Y} ➸ {C.G}Hook CoreX Flag: {C.OG}-p -x {C.P}( Only For [ arm64 ] )"""
        )

        user_input = input(f"\n\n{C.B}[ {C.P}* {C.B}] {C.C} Do See Example\n{C.G}  |\n  └──── {C.CC}~ y / Exit to Enter {C.G}$ : {C.Y}")

        if user_input.lower() == "y":
            print(
                f"""\n{Tag.replace("Tag", "AES Logs Inject")}

{C.INFO} AES MT Logs Inject Flag: {C.OG}-A{EX}-A


{C.INFO} Do U Want Separate AES.smali Dex Use Flag: {C.OG}-A -s{EX}-A -s

{Tag.replace("Tag", "Hook Android ID")}

{C.INFO} Hook Android ID For One Device Login Bypass Use Flag: {C.OG}-D {C.P}( Input Your Original 16 Digit Android ID ){EX}-D {C.Y}7e9f51f096bd5c83

{Tag.replace("Tag", "isFlutter / isPairip")}

{C.INFO} If APK is Flutter Then Use Additional Flag: {C.OG}-f{EX}-f {C.Y}-c certificate.cert


{C.INFO} If APK is Pairip Then Use Additional Flag: {C.OG}-p {C.P}( Without Sign APK Use Only in VM / Multi_App ){EX}-p {C.Y}-c certificate.cert


{C.INFO} If APK is Pairip Then Hook CoreX Use Additional Flag: {C.OG}-p -x {C.P}( Install Directly Only For [ arm64 ] ){EX}-p -x {C.Y}-c certificate.cert

{Tag.replace("Tag", "Spoof PKG / Device Info")}

{C.INFO} Spoof Package Detection Flag: {C.OG}-pkg {C.P}( Dex / Manifest / Res ){EX}-pkg


{C.INFO} Fake Device Info Flag: {C.OG}-r{EX}-r


{C.INFO} With Your Android ID Flag: {C.OG}-r -D {C.P}( Input Your Custom 16 Digit Android ID ){EX}-r -D {C.Y}7e9f51f096bd5c83

{Tag.replace("Tag", "Bypass Ads / SC / USB")}

{C.INFO} Bypass Ads Flag: {C.OG}-rmads{EX}-rmads


{C.INFO} Bypass Screenshot Restriction Flag: {C.OG}-rmsc{EX}-rmsc


{C.INFO} Bypass USB Debugging Flag: {C.OG}-rmusb{EX}-rmusb

{Tag.replace("Tag", "isPurchase / Skip Patch")}

{C.INFO} Purchase / Paid / Price Flag: {C.OG}-P{EX}-P


{C.INFO} Skip Patch Flag: {C.OG}-skip{EX}-skip {C.Y}getAcceptedIssuers\n"""
            )

        else:
            return


# ---------------- Parse Arguments ----------------
def parse_arguments():

    args = M.sys.argv[1:]

    if '-O' in args:
        exit(CustomArgumentParser().Other_Patch())

    if any(arg.startswith('-') for arg in args):
        parser = CustomArgumentParser(description=f'{C.C}ApkPatcher v{__version__}')
    else:
        parser = M.argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        '-i',
        dest='input',
        help=f'{C.Y}➸{C.G} Input APK Path...{C.C}'
    )

    group.add_argument(
        '-m',
        dest='Merge',
        help=f'{C.Y}➸{C.G} Anti-Split ( Only Merge APK ){C.C}'
    )

    group.add_argument(
        '-C',
        dest='Credits_Instruction',
        action='store_true',
        help=f'{C.Y}➸{C.G} Show Instructions & Credits{C.C}'
    )

    additional = parser.add_argument_group(f'{C.OG}[ * ] Additional Flags{C.C}')

    additional.add_argument(
        '-a',
        '--APKEditor',
        action='store_true',
        help=f'{C.Y}➸ {C.G}APKEditor ( Default APKTool ){C.C}'
    )

    additional.add_argument(
        '-e',
        '--For_Emulator',
        action='store_true',
        help=f'{C.Y}➸{C.G} If using emulator on PC then use -e flag{C.C}'
    )

    additional.add_argument(
        '-c',
        dest='CA_Certificate',
        type=str,
        nargs='*',
        help=f"{C.Y}➸{C.G} Input Your HttpCanary / Reqable / ProxyPin etc. Capture APK's CA-Certificate{C.C}"
    )

    additional.add_argument(
        '-u',
        dest='unsigned_apk',
        action='store_true',
        help=f"{C.Y}➸{C.G} Keep Unsigned APK{C.C}"
    )


    # ---------------- Other Patch Flags ----------------
    parser.add_argument(
        '-A',
        '--AES_Logs',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-D',
        '--Android_ID',
        type=str,
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-f',
        '--Flutter',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-p',
        '--Pairip',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-P',
        '--Purchase',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-r',
        '--Random_Info',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-rmads',
        '--Remove_Ads',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-rmsc',
        '--Remove_SC',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-rmusb',
        '--Remove_USB',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-pkg',
        '--Spoof_PKG',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-skip',
        dest='Skip_Patch',
        nargs='*',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-s',
        '--AES_S',
        action='store_true',
        help=M.argparse.SUPPRESS
    )

    parser.add_argument(
        '-x',
        '--Hook_CoreX',
        action='store_true',
        help=M.argparse.SUPPRESS
    )


    Ext = ('.apk', '.apks', '.apkm', '.xapk')

    fixed = []; start = None; Valid_Ext = False

    for index, option in enumerate(args):
        if option in ['-i', '-m', '-C']:
            start, fixed = index + 1, fixed + [option]
        elif start and (option.endswith(Ext) or M.os.path.isdir(option)):
            fixed, start = fixed + [' '.join(args[start:index+1])], None
            Valid_Ext = True
        elif not start:
            fixed.append(option)


    if not Valid_Ext and M.sys.argv[1:2] != ['-C']:
        print(f"\n{C.X}{C.C} Only Supported Extensions {C.G}{Ext}\n")

    print(f"\n{C.S} Input Path {C.E} {C.OG}➸❥{C.Y}", *fixed, f"{C.CC}\n")

    return parser.parse_args(fixed)