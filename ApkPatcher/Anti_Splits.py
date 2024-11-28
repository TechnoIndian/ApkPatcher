from.C_M import CM
C=CM()
from.Files_Check import FileCheck
F=FileCheck()
F.set_paths()
apkeditor_path=F.apkeditor_path
def Anti_Split(input_path):
	A=input_path
	try:
		D,E=C.os.path.splitext(A)
		if E in['.apks','.apkm','.xapk']:print(f"\n{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Anti-Split Start...");B=f"{D.replace(' ','_')}.apk";print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(apkeditor_path)} m -i {A} -f -o {B}\n");print(f"{C.r}_____________________________________________________________{C.g}\n");C.os.system(f"java -jar {apkeditor_path} m -i '{A}' -f -o '{B}'");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Anti-Split Done {C.g} ✔{C.r}");return B
		else:print(f"\n{C.lb}[{C.c} Info {C.lb}] {C.rd}Split ✘{C.r}\n")
		return A
	except Exception as F:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} {str(F)} ✘{C.r}\n")