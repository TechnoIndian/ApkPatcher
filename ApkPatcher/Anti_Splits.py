from.C_M import CM
C=CM()
from.Files_Check import FileCheck
F=FileCheck()
F.set_paths()
def Anti_Split(input_path):
	A=input_path
	try:
		E,G=C.os.path.splitext(A)
		if G in['.apks','.apkm','.xapk']:
			print(f"\n{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Anti-Split Start...");B=f"{E.replace(' ','_')}.apk";print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.apkeditor_path)} m -i {A} -f -o {B}\n");print(f"{C.r}_____________________________________________________________{C.g}\n");H=['java','-jar',F.apkeditor_path,'m','-i',A,'-f','-o',B]
			try:I=C.subprocess.run(H,check=True);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Anti-Split Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________");return B
			except C.subprocess.CalledProcessError as D:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Anti-Split Failed ! ✘{C.r}\n\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Error Output: {D.stderr}\n")
		else:print(f"\n{C.lb}[{C.c} Info {C.lb}] {C.rd}Split ✘{C.r}\n")
		return A
	except(FileNotFoundError,Exception)as D:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} {str(D)} ✘{C.r}\n")