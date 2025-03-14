_E=True
_D='-o'
_C='-f'
_B='-jar'
_A='java'
from.C_M import CM
C=CM()
from.Files_Check import FileCheck
F=FileCheck()
F.set_paths()
F.isEmulator()
class De_Compiler:
	def decompile_apk(H,apk_path,decompile_dir,isEmulator,isAPKEditor):
		D=isAPKEditor;B=decompile_dir;A=apk_path;E=F.apktool_path_e if isEmulator else F.apktool_path;print(f"\n{C.r}_____________________________________________________________\n")
		if D:G=[_A,_B,F.apkeditor_path,'d',_C,'-no-dex-debug','-i',A,_D,B];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile with APKEditor...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.apkeditor_path)} d -f -no-dex-debug -i {A} -o {C.os.path.basename(B)}\n")
		else:G=[_A,_B,E,'d',_C,'--only-main-classes',A,_D,B,'-p',B];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompiling APK...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(E)} d -f {A} -o {C.os.path.basename(B)}\n")
		print(f"{C.r}_____________________________________________________________{C.g}\n")
		try:C.subprocess.run(G,check=_E);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n\n")
		except C.subprocess.CalledProcessError:
			if not D:print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Decompile Failed ! ✘{C.r}\n");print(f"{C.r}_____________________________________________________________\n");exit(f"\n{C.lb}[ {C.y}Suggest ! {C.lb}]{C.c} Try With APKEditor, Flag {C.g}-a\n     |\n     └──── {C.r}~ Ex. {C.g}$ {C.rkj}ApkPatcher -i {C.y}{A} {C.g}-a\n")
			exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Decompile Failed ! ✘{C.r}\n");return None,None
	def recompile_apk(H,decompile_dir,apk_path,build_dir,isEmulator,isAPKEditor):
		G='b';B=decompile_dir;A=build_dir;E=F.apktool_path_e if isEmulator else F.apktool_path
		if isAPKEditor:
			D=[_A,_B,F.apkeditor_path,G,'-i',B,_D,A,_C];print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(F.apkeditor_path)} b -i {C.os.path.basename(B)} -o {C.os.path.basename(A)} -f\n");print(f"{C.r}_____________________________________________________________{C.g}\n")
			try:C.subprocess.run(D,check=_E);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
			except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with APKEditor ! ✘{C.r}\n")
		else:
			D=[_A,_B,E,G,_C,B,_D,A,'-p',B];print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(E)} b -f {C.os.path.basename(B)} -o {C.os.path.basename(A)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool Default...{C.g}\n")
			try:C.subprocess.run(D,check=_E);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
			except C.subprocess.CalledProcessError:
				print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Default Recompile Failed! ✘{C.r}\n");D=[_A,_B,E,G,_C,'-use-aapt2',B,_D,A,'-p',B];print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt2 ~{C.g}$ java -jar {C.os.path.basename(E)} b -f -use-aapt2 {C.os.path.basename(B)} -o {C.os.path.basename(A)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool AAPT2...{C.g}\n")
				try:C.subprocess.run(D,check=_E);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful with aapt2 {C.g} ✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
				except C.subprocess.CalledProcessError:print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} AAPT2 Recompile Failed! ✘{C.r}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with both Default & aapt2 ! ✘{C.r}\n");print(f"{C.r}_____________________________________________________________\n");exit(f"\n{C.lb}[ {C.y}Suggest ! {C.lb}]{C.c} Try With APKEditor, Flag {C.g}-a\n     |\n     └──── {C.r}~ Ex. {C.g}$ {C.rkj}ApkPatcher -i {C.y}{apk_path} {C.g}-a\n")
		if C.os.path.exists(A):print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} APK Successfully Created {C.g}➸❥ {C.y}{A} {C.g}✔{C.r}\n")
		else:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Failed to Create APK at: {A} ! ✘{C.r}\n")
		print(f"{C.r}_____________________________________________________________\n")
	def sign_apk(E,build_dir):
		A=build_dir;D=[_A,_B,F.Sign_Jar,'--overwrite','-a',A];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Signing APK...");print(f"{C.g}  |\n  └──── {C.r}Signing ~{C.g}$ java -jar {C.os.path.basename(F.Sign_Jar)} --overwrite -a {A}\n");print(f"{C.r}_____________________________________________________________{C.g}\n")
		try:
			C.subprocess.run(D,check=_E);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Sign Successful  {C.g}✔{C.r}\n");B=A+'.idsig'
			if C.os.path.exists(B):C.os.remove(B)
			print(f"{C.r}_____________________________________________________________\n\n")
		except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Sign Failed ! ✘{C.r}\n")