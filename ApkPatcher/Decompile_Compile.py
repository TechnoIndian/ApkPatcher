_C='-jar'
_B='java'
_A=True
from.C_M import CM
C=CM()
from.Files_Check import FileCheck
F=FileCheck()
F.set_paths()
class De_Compiler:
	def decompile_apk(E,apk_path,decompile_dir):
		B=apk_path;A=decompile_dir;print(f"\n{C.r}_____________________________________________________________\n");D=[_B,_C,F.apktool_path,'d','-f',B,'-o',A,'-p',A];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompiling APK...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.apktool_path)} d -f {B} -o {C.os.path.basename(A)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n")
		try:C.subprocess.run(D,check=_A);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n\n")
		except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Decompile Failed ! ✘{C.r}\n")
	def recompile_apk(E,decompile_dir,build_dir):
		B=decompile_dir;A=build_dir
		if C.os.path.isfile(A):print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} APK Already Exists.\n{C.g}  |\n  └──── {C.g}Removed Old APK... {C.y}{A} {C.g}✔{C.r}\n");C.os.remove(A)
		D=[_B,_C,F.apktool_path,'b',B,'-o',A,'-p',F.A_F_P];print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(F.apktool_path)} b {C.os.path.basename(B)} -o {C.os.path.basename(A)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool Default...{C.g}\n")
		try:C.subprocess.run(D,check=_A);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
		except C.subprocess.CalledProcessError:
			print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Default Recompile Failed! ✘{C.r}\n");D=[_B,_C,F.apktool_path,'b','-use-aapt2',B,'-o',A,'-p',F.A_F_P];print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt2 ~{C.g}$ java -jar {C.os.path.basename(F.apktool_path)} b -use-aapt2 {C.os.path.basename(B)} -o {C.os.path.basename(A)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool AAPT2...{C.g}\n")
			try:C.subprocess.run(D,check=_A);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful with aapt2 {C.g} ✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
			except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} AAPT2 Recompile Failed! ✘{C.r}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with both Default & aapt2 ! ✘{C.r}\n")
	def align_apk(D,build_dir,out_dir):A=out_dir+'_aligned.apk';B=['zipalign','-v','4',build_dir,A];C.subprocess.run(B,stdout=C.subprocess.DEVNULL,stderr=C.subprocess.DEVNULL,check=_A);return A
	def sign_apk(G,build_dir,out_dir):
		B='true';A=out_dir;D=G.align_apk(build_dir,A);H=['apksigner','sign','--key',F.key_path,'--cert',F.cert_path,'--out',A,'--v1-signing-enabled',B,'--v2-signing-enabled',B,'--v3-signing-enabled',B,D];C.subprocess.run(H,check=_A);C.os.remove(D);E=A+'.idsig'
		if C.os.path.exists(E):C.os.remove(E)