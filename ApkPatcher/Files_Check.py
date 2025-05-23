_B='56d59c524fc764263ba8d345754d8daf55b1887818b15cd3b594f555d249e2db'
_A='nt'
from.C_M import CM
C=CM()
class FileCheck:
	def set_paths(A):B=C.os.path.dirname(C.os.path.abspath(C.sys.argv[0]));A.APKEditor_Path=C.os.path.join(B,'APKEditor.jar');A.APKTool_Path=C.os.path.join(B,'APKTool_AP.jar');A.Sign_Jar=C.os.path.join(B,'Uber-Apk-Signer.jar');A.AES_P=C.os.path.join(C.os.path.dirname(C.os.path.abspath(__file__)),'AES.smali')
	def isEmulator(A):B=C.os.path.dirname(C.os.path.abspath(C.sys.argv[0]));A.APKTool_Path_E=C.os.path.join(B,'APKTool_OR.jar')
	def calculate_checksum(E,file_path):
		A=C.hashlib.sha256()
		try:
			with open(file_path,'rb')as B:
				for D in iter(lambda:B.read(4096),b''):A.update(D)
			return A.hexdigest()
		except FileNotFoundError:return
	def download_file(K,Jar_Files):
		H=True;import requests as F;Z=set()
		for(L,A,M)in Jar_Files:
			B=C.os.path.basename(A)
			if C.os.path.exists(A):
				N=K.calculate_checksum(A)
				if N==M:continue
				else:print(f"{C.rd}[ {C.pr}File {C.rd}] {C.c}{B} {C.rd}is Corrupt (Checksum Mismatch).\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Re-Downloading, Need Internet Connection.{C.r}\n");C.os.remove(A)
			try:
				O='2.0';P='https://raw.githubusercontent.com/TechnoIndian/ApkPatcher/main/setup.py'
				if(Q:=F.get(P)).status_code==200 and(R:=C.re.search('version="(.*?)"',Q.text)):
					if(S:=R.group(1))!=O:print(f"\n{C.lb}[ {C.y}Update {C.lb}]{C.c} Updating ApkPatcher to {C.g}{S}...\n\n");I=['pip','install','git+https://github.com/TechnoIndian/ApkPatcher.git']if C.os.name==_A else'curl -L -o ApkPatcher.sh https://github.com/TechnoIndian/ApkPatcher/releases/download/ApkPatcher/ApkPatcher.sh && chmod +x ApkPatcher.sh && ./ApkPatcher.sh';C.subprocess.run(I,shell=isinstance(I,str),check=H)
				print(f"\n{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{B}",end='',flush=H);D=F.get(L,stream=H,timeout=10)
				if D.status_code==200:
					E=int(D.headers.get('content-length',0));T=1024;G=0
					with open(A,'wb')as U:
						for J in D.iter_content(T):G+=len(J);U.write(J);V=G/E*100 if E>0 else 0;W=G/(1024*1024);X=E/(1024*1024)if E>0 else 0;Y=f"\r{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{B} {C.g}➸❥ {V:.2f}% ({W:.2f}/{X:.2f} MB)";print(Y,end='\r')
					print(f"\n{C.g}       |\n       └──── {C.r}Downloaded ~{C.g}$ {B} Successfully. ✔\n")
				else:exit(f"""\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Failed to download {C.y}{B} {C.rd}Status Code: {D.status_code}\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Restart Script...{C.r}\n""")
			except F.exceptions.RequestException:exit(f"""\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Got an error while Fetching {C.y}{A}\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No internet Connection\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Internet Connection is Required to Download {C.y}{B}\n""")
	def F_D(A):B=[('https://github.com/TechnoIndian/Tools/releases/download/Tools/APKEditor.jar',A.APKEditor_Path,'d4280b36fc78ba1f11c04a8a9d91fa8646cf4c41e96fd0addc9afb81b78dcbe9'),('https://github.com/TechnoIndian/Tools/releases/download/Tools/apktool.jar'if C.os.name==_A else'https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool_Modified.jar',A.APKTool_Path,_B if C.os.name==_A else'6ca32ba4e21db3229a7947adfb388cbec6234f4d9c34461741199a3c96e2a857'),('https://github.com/TechnoIndian/Tools/releases/download/Tools/Uber-Apk-Signer.jar',A.Sign_Jar,'e1299fd6fcf4da527dd53735b56127e8ea922a321128123b9c32d619bba1d835'),('https://raw.githubusercontent.com/TechnoIndian/Objectlogger/refs/heads/main/AES.smali',A.AES_P,'09db8c8d1b08ec3a2680d2dc096db4aa8dd303e36d0e3c2357ef33226a5e5e52')];A.download_file(B);C.os.system('cls'if C.os.name==_A else'clear')
	def F_D_A(B,isEmulator):
		A=[]
		if isEmulator:A.append(('https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool.jar',B.APKTool_Path_E,_B))
		if A:B.download_file(A)