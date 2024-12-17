_E=True
_D='-p'
_C='-o'
_B='-jar'
_A='java'
from.C_M import CM
C=CM()
from.Files_Check import FileCheck
from.Files_Check_Emulator import F_C_E
F=FileCheck()
F.set_paths()
FE=F_C_E()
FE.set_paths()
class De_Compiler:
	def decompile_apk(E,apk_path,decompile_dir):
		B=apk_path;A=decompile_dir;print(f"\n{C.r}_____________________________________________________________\n");D=[_A,_B,F.apktool_path,'d','-f',B,_C,A,_D,A];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompiling APK...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.apktool_path)} d -f {B} -o {C.os.path.basename(A)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n")
		try:C.subprocess.run(D,check=_E);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n\n")
		except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Decompile Failed ! ✘{C.r}\n")
	def recompile_apk(I,decompile_dir,build_dir,isEmulator):
		H='-use-aapt2';G='b';E=isEmulator;B=decompile_dir;A=build_dir
		if C.os.path.isfile(A):print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} APK Already Exists.\n{C.g}  |\n  └──── {C.g}Removed Old APK... {C.y}{A} {C.g}✔{C.r}\n");C.os.remove(A)
		if E:D=[_A,_B,FE.apktool_path,G,B,_C,A,_D,B]
		else:D=[_A,_B,F.apktool_path,G,B,_C,A,_D,F.A_F_P]
		print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...")
		if E:print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(FE.apktool_path)} b {C.os.path.basename(B)} -o {C.os.path.basename(A)}\n")
		else:print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(F.apktool_path)} b {C.os.path.basename(B)} -o {C.os.path.basename(A)}\n")
		print(f"{C.r}_____________________________________________________________{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool Default...{C.g}\n")
		try:C.subprocess.run(D,check=_E);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
		except C.subprocess.CalledProcessError:
			print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Default Recompile Failed! ✘{C.r}\n")
			if E:D=[_A,_B,FE.apktool_path,G,H,B,_C,A,_D,B]
			else:D=[_A,_B,F.apktool_path,G,H,B,_C,A,_D,F.A_F_P]
			print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...")
			if E:print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt2 ~{C.g}$ java -jar {C.os.path.basename(FE.apktool_path)} b -use-aapt2 {C.os.path.basename(B)} -o {C.os.path.basename(A)}\n")
			else:print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt2 ~{C.g}$ java -jar {C.os.path.basename(F.apktool_path)} b -use-aapt2 {C.os.path.basename(B)} -o {C.os.path.basename(A)}\n")
			print(f"{C.r}_____________________________________________________________{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool AAPT2...{C.g}\n")
			try:C.subprocess.run(D,check=_E);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful with aapt2 {C.g} ✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
			except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} AAPT2 Recompile Failed! ✘{C.r}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with both Default & aapt2 ! ✘{C.r}\n")
	def sign_apk(E,build_dir):
		A=build_dir;D=[_A,_B,F.Sign_Jar,'--overwrite','-a',A];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Signing APK...");print(f"{C.g}  |\n  └──── {C.r}Signing ~{C.g}$ java -jar {C.os.path.basename(F.Sign_Jar)} --overwrite -a {A}\n");print(f"{C.r}_____________________________________________________________{C.g}\n")
		try:
			C.subprocess.run(D,check=_E);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Sign Successful  {C.g}✔{C.r}\n");B=A+'.idsig'
			if C.os.path.exists(B):C.os.remove(B)
			print(f"{C.r}_____________________________________________________________\n\n")
		except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Sign Failed ! ✘{C.r}\n")