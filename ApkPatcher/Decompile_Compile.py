_C=True
_B='-jar'
_A='java'
from.C_M import CM
C=CM()
from.Files_Check import FileCheck
F=FileCheck()
F.set_paths()
F.isEmulator()
class De_Compiler:
	def decompile_apk(G,apk_path,decompile_dir,isEmulator):
		B=apk_path;A=decompile_dir;D=F.apktool_path_e if isEmulator else F.apktool_path;print(f"\n{C.r}_____________________________________________________________\n");E=[_A,_B,D,'d','-f','--only-main-classes',B,'-o',A,'-p',A];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompiling APK...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(D)} d -f {B} -o {C.os.path.basename(A)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n")
		try:C.subprocess.run(E,check=_C);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n\n")
		except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Decompile Failed ! ✘{C.r}\n")
	def recompile_apk(G,decompile_dir,build_dir,isEmulator):
		B=build_dir;A=decompile_dir;D=F.apktool_path_e if isEmulator else F.apktool_path;E=[_A,_B,D,'b','-f',A,'-o',B,'-p',A];print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(D)} b -f {C.os.path.basename(A)} -o {C.os.path.basename(B)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool Default...{C.g}\n")
		try:C.subprocess.run(E,check=_C);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
		except C.subprocess.CalledProcessError:
			print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Default Recompile Failed! ✘{C.r}\n");E=[_A,_B,D,'b','-f','-use-aapt2',A,'-o',B,'-p',A];print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt2 ~{C.g}$ java -jar {C.os.path.basename(D)} b -f -use-aapt2 {C.os.path.basename(A)} -o {C.os.path.basename(B)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool AAPT2...{C.g}\n")
			try:C.subprocess.run(E,check=_C);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful with aapt2 {C.g} ✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
			except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} AAPT2 Recompile Failed! ✘{C.r}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with both Default & aapt2 ! ✘{C.r}\n")
	def sign_apk(E,build_dir):
		A=build_dir;D=[_A,_B,F.Sign_Jar,'--overwrite','-a',A];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Signing APK...");print(f"{C.g}  |\n  └──── {C.r}Signing ~{C.g}$ java -jar {C.os.path.basename(F.Sign_Jar)} --overwrite -a {A}\n");print(f"{C.r}_____________________________________________________________{C.g}\n")
		try:
			C.subprocess.run(D,check=_C);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Sign Successful  {C.g}✔{C.r}\n");B=A+'.idsig'
			if C.os.path.exists(B):C.os.remove(B)
			print(f"{C.r}_____________________________________________________________\n\n")
		except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Sign Failed ! ✘{C.r}\n")