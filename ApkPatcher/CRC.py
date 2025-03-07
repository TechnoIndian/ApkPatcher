from.C_M import CM
C=CM()
class CRC:
	def format_time(A,timestamp):return C.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
	def process_apks(I,apk_path,build_dir,file_types):
		P='little';O='.apk';J=apk_path;D=file_types;B=build_dir;E=B.replace(O,O);K=0;L=[]
		try:
			with C.zipfile.ZipFile(J)as M,C.zipfile.ZipFile(B)as N:Q={A.filename:A.CRC for A in M.infolist()if any(B in A.filename for B in D)};F={A.filename:A.CRC for A in N.infolist()if any(B in A.filename for B in D)};R={A.filename:A.date_time for A in M.infolist()if any(B in A.filename for B in D)};S={A.filename:A.date_time for A in N.infolist()if any(B in A.filename for B in D)}
			for(A,H)in Q.items():
				if A in F and H!=F[A]:
					T=H.to_bytes(4,P);U=F[A].to_bytes(4,P);K+=1;V=I.format_time(C.datetime(*R[A]).timestamp());W=I.format_time(C.datetime(*S[A]).timestamp());L.append((A,f"{H:08x}",f"{F[A]:08x}",V,W))
					with open(B,'rb')as X:Y=X.read()
					Z=Y.replace(U,T)
					with open(E,'wb')as a:a.write(Z)
					B=E
		except Exception as b:print(f"{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} processing APKs: {b} ! ✘{C.r}\n");return
		print(f"\n                    ✨ {C.g}CRCFix by Kirlif ✨\n");print(f"{C.c}File Name              CRC         FIX         Modified       ")
		for G in L:print(f"\n{C.g}{G[0]:<22} {G[1]}    {G[2]}    {G[4]}\n")
		print(f"\n{C.lb}[{C.c}  INPUT  {C.lb}] {C.g}➸❥ {C.y}{J}\n");print(f"{C.lb}[{C.c}  OUTPUT  {C.lb}] {C.g}➸❥ {C.y}{E}\n");print(f"\n{C.lb}[{C.c}  CRCFix  {C.lb}] {C.g}➸❥ {C.pr}{K}{C.r}\n\n");return E