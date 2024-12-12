from .C_M import CM
C = CM()
from .Files_Check import FileCheck;from.Files_Check_Emulator import F_C_E
F = FileCheck(); F.set_paths();
FE = F_C_E(); FE.set_paths();
# Decompile_Apk
class De_Compiler:
    def decompile_apk(self, apk_path, decompile_dir):
        print(f'\n{C.r}_____________________________________________________________\n')
        command = ["java", "-jar", F.apktool_path, "d", "-f", apk_path, "-o", decompile_dir, "-p", decompile_dir]
        print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompiling APK...")
        print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.apktool_path)} d -f {apk_path} -o {C.os.path.basename(decompile_dir)}\n")
        print(f'{C.r}_____________________________________________________________{C.g}\n')
        try:
            C.subprocess.run(command, check=True)
            print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile Successful  {C.g}✔{C.r}\n")
            print(f'{C.r}_____________________________________________________________\n\n')
        except C.subprocess.CalledProcessError:
            exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Decompile Failed ! ✘{C.r}\n")

    # Smaling
    def recompile_apk(self, decompile_dir, build_dir, isEmulator):
        if C.os.path.isfile(build_dir):
            print(f'{C.r}_____________________________________________________________\n')
            print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} APK Already Exists.\n{C.g}  |\n  └──── {C.g}Removed Old APK... {C.y}{build_dir} {C.g}✔{C.r}\n")
            C.os.remove(build_dir)
        if isEmulator:
            command = ["java", "-jar", FE.apktool_path, "b", decompile_dir, "-o", build_dir, "-p", decompile_dir]
        else:
            command = ["java", "-jar", F.apktool_path, "b", decompile_dir, "-o", build_dir, "-p", F.A_F_P]
        print(f'{C.r}_____________________________________________________________\n')
        print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...")
        if isEmulator:
            print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(FE.apktool_path)} b {C.os.path.basename(decompile_dir)} -o {C.os.path.basename(build_dir)}\n")
        else:
            print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(F.apktool_path)} b {C.os.path.basename(decompile_dir)} -o {C.os.path.basename(build_dir)}\n")
        print(f'{C.r}_____________________________________________________________{C.g}\n')
        print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool Default...{C.g}\n")
        try:
            C.subprocess.run(command, check=True)
            print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{C.r}\n")
            print(f'{C.r}_____________________________________________________________\n')
        except C.subprocess.CalledProcessError:
            print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Default Recompile Failed! ✘{C.r}\n")
            if isEmulator:
                command = ["java", "-jar", FE.apktool_path, "b", "-use-aapt2", decompile_dir, "-o", build_dir, "-p", decompile_dir]
            else:
                command = ["java", "-jar", F.apktool_path, "b", "-use-aapt2", decompile_dir, "-o", build_dir, "-p", F.A_F_P]
            print(f'{C.r}_____________________________________________________________\n')
            print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...")
            if isEmulator:
                print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt2 ~{C.g}$ java -jar {C.os.path.basename(FE.apktool_path)} b -use-aapt2 {C.os.path.basename(decompile_dir)} -o {C.os.path.basename(build_dir)}\n")
            else:
                print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt2 ~{C.g}$ java -jar {C.os.path.basename(F.apktool_path)} b -use-aapt2 {C.os.path.basename(decompile_dir)} -o {C.os.path.basename(build_dir)}\n")
            print(f'{C.r}_____________________________________________________________{C.g}\n')
            print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool AAPT2...{C.g}\n")
            try:
                C.subprocess.run(command, check=True)
                print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful with aapt2 {C.g} ✔{C.r}\n")
                print(f'{C.r}_____________________________________________________________\n')
            except C.subprocess.CalledProcessError:
                exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} AAPT2 Recompile Failed! ✘{C.r}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with both Default & aapt2 ! ✘{C.r}\n")
    
    # Sign Apk
    def align_apk(self, build_dir, out_dir):
        aligned_output = out_dir + "_aligned.apk"
        zipalign_cmd = ["zipalign", "-v", "4", build_dir, aligned_output]
        C.subprocess.run(zipalign_cmd, stdout=C.subprocess.DEVNULL, stderr=C.subprocess.DEVNULL, check=True)
        return aligned_output

    def sign_apk(self, build_dir, out_dir):
        aligned_output = self.align_apk(build_dir, out_dir)
        cmd = ["apksigner", "sign", "--key", F.key_path, "--cert", F.cert_path, "--out", out_dir, 
               "--v1-signing-enabled", "true", "--v2-signing-enabled", "true", "--v3-signing-enabled", "true", aligned_output]
        C.subprocess.run(cmd, check=True)
        C.os.remove(aligned_output)
        idsig_file = out_dir + ".idsig"
        if C.os.path.exists(idsig_file):
            C.os.remove(idsig_file)