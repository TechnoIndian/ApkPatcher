from.C_M import CM
C=CM()
class F_C_E:
	def set_paths(A):B=C.os.path.dirname(C.os.path.abspath(C.sys.argv[0]));A.apktool_path=C.os.path.join(B,'APKTool_OR.jar')
	def calculate_checksum(E,file_path):
		A=C.hashlib.sha256()
		try:
			with open(file_path,'rb')as B:
				for D in iter(lambda:B.read(4096),b''):A.update(D)
			return A.hexdigest()
		except FileNotFoundError:return
	def download_file(I,jar_urls_and_paths):
		import requests as G;S=set()
		for(J,A,K)in jar_urls_and_paths:
			B=C.os.path.basename(A)
			if C.os.path.exists(A):
				L=I.calculate_checksum(A)
				if L==K:continue
				else:print(f"{C.rd}[ {C.pr}File {C.rd}] {C.c}{B} {C.rd}is Corrupt (Checksum Mismatch).\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Re-Downloading, Need Internet Connection.{C.r}\n");C.os.remove(A)
			try:
				print(f"\n{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{B}",end='',flush=True);D=G.get(J,stream=True,timeout=10)
				if D.status_code==200:
					E=int(D.headers.get('content-length',0));M=1024;F=0
					with open(A,'wb')as N:
						for H in D.iter_content(M):F+=len(H);N.write(H);O=F/E*100 if E>0 else 0;P=F/(1024*1024);Q=E/(1024*1024)if E>0 else 0;R=f"\r{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{B} {C.g}➸❥ {O:.2f}% ({P:.2f}/{Q:.2f} MB)";print(R,end='\r')
					print(f"\n{C.g}       |\n       └──── {C.r}Downloaded ~{C.g}$ {B} Successfully. ✔\n")
				else:exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Failed to download {C.y}{B} {C.rd}Status Code: {D.status_code}\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Restart Script...{C.r}\n')
			except G.exceptions.RequestException:exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Got an error while Fetching {C.y}{A}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No internet Connection\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Internet Connection is Required to Download {C.y}{B}\n')
	def F_D(A,isEmulator):
		B=[]
		if isEmulator:B=[('https://github.com/TechnoIndian/RKPairip/releases/download/Editor/apktool.jar',A.apktool_path,'c0350abbab5314248dfe2ee0c907def4edd14f6faef1f5d372d3d4abd28f0431')]
		else:0
		A.download_file(B)