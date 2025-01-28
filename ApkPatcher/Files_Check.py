from.C_M import CM
C=CM()
class FileCheck:
	def set_paths(A):B=C.os.path.dirname(C.os.path.abspath(C.sys.argv[0]));A.apkeditor_path=C.os.path.join(B,'APKEditor.jar');A.apktool_path=C.os.path.join(B,'APKTool_AP.jar');A.Sign_Jar=C.os.path.join(B,'Uber-Apk-Signer.jar');A.AES_P=C.os.path.join(C.os.path.dirname(C.os.path.abspath(__file__)),'AES.smali')
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
	def F_D(A):B='nt';D=[('https://github.com/TechnoIndian/ApkTool_Framwork/releases/download/APKTool_2.10.0/APKEditor.jar',A.apkeditor_path,'758f2f9153fff96c20260b177f025a3ca3cecc9777abdd43139a17e225724612'),('https://github.com/TechnoIndian/ApkTool_Framwork/releases/download/APKTool_2.10.0/apktool.jar'if C.os.name==B else'https://github.com/TechnoIndian/ApkTool_Framwork/releases/download/APKTool_2.10.0/apktool_modified.jar',A.apktool_path,'8fdc17c6fe2e6d80d71b8718eb2a5d0379f1cc7139ae777f6a499ce397b26f54'if C.os.name==B else'62a156f9ccd626a625d18884061b30d073f2b1cac45c3ee9cd67ec504eed8669'),('https://github.com/TechnoIndian/ApkTool_Framwork/releases/download/APKTool_2.10.0/Uber-Apk-Signer.jar',A.Sign_Jar,'e1299fd6fcf4da527dd53735b56127e8ea922a321128123b9c32d619bba1d835'),('https://raw.githubusercontent.com/TechnoIndian/Objectlogger/refs/heads/main/AES.smali',A.AES_P,'09db8c8d1b08ec3a2680d2dc096db4aa8dd303e36d0e3c2357ef33226a5e5e52')];A.download_file(D);C.os.system('cls'if C.os.name==B else'clear')