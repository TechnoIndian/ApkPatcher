from.C_M import CM
C=CM()
from.Files_Check import FileCheck
F=FileCheck()
F.set_paths()
def Anti_Split(apk_path,isMerge):
	G=isMerge;A=apk_path
	try:
		I,H=C.os.path.splitext(A);B=['.apks','.apkm','.xapk']
		if H in B:
			print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Anti-Split Start...");D=f"{I.replace(' ','_')}.apk";print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.APKEditor_Path)} m -i {A} -f -o {D}\n");print(f"{C.r}_____________________________________________________________{C.g}\n");J=['java','-jar',F.APKEditor_Path,'m','-i',A,'-f','-o',D]
			try:
				K=C.subprocess.run(J,check=True);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Anti-Split Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
				if G:exit()
				return D
			except C.subprocess.CalledProcessError as E:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Anti-Split Failed ! ✘{C.r}\n\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Error Output: {E.stderr}\n")
		if G and H not in B:exit(f"""\n{C.lb}[{C.c} Info {C.lb}] {C.rd}Split ✘{C.r}\n\n\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Only Supported Extensions {C.g}{B}\n""")
		return A
	except(FileNotFoundError,Exception)as E:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} {str(E)} ✘{C.r}\n")