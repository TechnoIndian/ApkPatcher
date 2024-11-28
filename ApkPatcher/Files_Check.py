from.C_M import CM
C=CM()
class FileCheck:
	def set_paths(A):B=C.os.path.dirname(C.os.path.abspath(C.sys.argv[0]));A.apkeditor_path=C.os.path.join(B,'APKEditor.jar');A.apktool_path=C.os.path.join(B,'APKTool_AP.jar');A.key_path=C.os.path.join(B,'testkey.pk8');A.cert_path=C.os.path.join(B,'testkey.x509.pem');A.apktool_framework_zip=C.os.path.join(C.os.path.expanduser('~'),'ApkTool_Framwork.zip');A.local_folder_path=C.os.path.join(C.os.path.expanduser('~'),'.local')
	def download_file(Q,jar_urls_and_paths):
		import requests as G;J=set()
		for(H,B)in jar_urls_and_paths:
			A=C.os.path.basename(B)
			if C.os.path.exists(B)or H in J:continue
			try:
				print(f"{C.lb}[ {C.pr}* {C.lb}] {C.c} Downloading {A}...",end='',flush=True);D=G.get(H,stream=True,timeout=10)
				if D.status_code==200:
					E=int(D.headers.get('content-length',0));K=1024;F=0
					with open(B,'wb')as L:
						for I in D.iter_content(K):F+=len(I);L.write(I);M=F/E*100 if E>0 else 0;N=F/(1024*1024);O=E/(1024*1024)if E>0 else 0;P=f"\r{C.lb}[ {C.pr}* {C.lb}] {C.c} Downloading {A}... {C.g}➸❥  {M:.2f}% ({N:.2f}/{O:.2f} MB)";print(P,end='\r')
					print(f"\n{C.g}  |\n  └──── {C.r}~{C.g}$ Downloaded {A} Successfully. ✔\n")
				else:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Failed to download {C.y}{A} {C.rd}Status Code: {D.status_code}\n\n{C.lb}[ {C.rd}INFO {C.lb}]{C.rd} Restart Script...{C.r}\n")
			except G.exceptions.RequestException:exit(f'\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Got an error while Fetching {C.y}{local_path}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No internet Connection\n\n{C.lb}[ {C.rd}INFO {C.lb}]{C.rd} Internet connection is required to download {C.y}{lo_path}\n')
	def unzip_apktool_framework(A):
		if C.os.path.exists(A.apktool_framework_zip):
			try:
				B=C.os.path.expanduser('~');C.os.makedirs(B,exist_ok=True)
				with C.zipfile.ZipFile(A.apktool_framework_zip,'r')as E:E.extractall(B);C.os.remove(A.apktool_framework_zip)
				D=C.os.path.join(B,'ApkTool_Framwork-main')
				if C.os.path.exists(D):C.os.rename(D,A.local_folder_path)
			except(C.zipfile.BadZipFile,Exception)as F:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Failed to unzip {C.y}{A.apktool_framework_zip}{C.r}\n")
	def F_D(A):
		D=[('https://github.com/TechnoIndian/RKPairip/releases/download/Editor/APKEditor.jar',A.apkeditor_path),('https://github.com/TechnoIndian/RKPairip/releases/download/Editor/apktool.jar'if C.os.name=='nt'else'https://github.com/TechnoIndian/RKPairip/releases/download/Editor/apktool_modified.jar',A.apktool_path),('https://github.com/TechnoIndian/ApkTool_Framwork/releases/download/ApkTool_2.10.0/testkey.pk8',A.key_path),('https://github.com/TechnoIndian/ApkTool_Framwork/releases/download/ApkTool_2.10.0/testkey.x509.pem',A.cert_path)];A.download_file(D);B=[]
		if not C.os.path.exists(A.local_folder_path):B.append(('https://github.com/TechnoIndian/ApkTool_Framwork/archive/refs/heads/main.zip',A.apktool_framework_zip))
		A.download_file(B);A.unzip_apktool_framework();C.os.system('cls'if C.os.name=='nt'else'clear')