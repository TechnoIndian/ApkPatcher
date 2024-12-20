# -* coding: utf-8 *-
# @auhtor: AbhiTheModder
_B='x86'
_A='arm'
from.C_M import CM
C=CM()
class F_P:
	patterns={'arm64':['F. 0F 1C F8 F. 5. 01 A9 F. 5. 02 A9 F. .. 03 A9 .. .. .. .. 68 1A 40 F9','F. 43 01 D1 FE 67 01 A9 F8 5F 02 A9 F6 57 03 A9 F4 4F 04 A9 13 00 40 F9 F4 03 00 AA 68 1A 40 F9','FF 43 01 D1 FE 67 01 A9 .. .. 06 94 .. 7. 06 94 68 1A 40 F9 15 15 41 F9 B5 00 00 B4 B6 4A 40 F9'],_A:['2D E9 F. 4. D0 F8 00 80 81 46 D8 F8 18 00 D0 F8'],_B:['55 41 57 41 56 41 55 41 54 53 50 49 89 f. 4c 8b 37 49 8b 46 30 4c 8b a. .. 0. 00 00 4d 85 e. 74 1. 4d 8b','55 41 57 41 56 41 55 41 54 53 48 83 EC 18 49 89 FF 48 8B 1F 48 8B 43 30 4C 8B A0 28 02 00 00 4D 85 E4 74','55 41 57 41 56 41 55 41 54 53 48 83 EC 38 C6 02 50 48 8B AF A. 00 00 00 48 85 ED 74 7. 48 83 7D 00 00 74']}
	def get_r2_version(E):
		B=True
		try:
			A=C.subprocess.run(['r2','-V'],capture_output=B,text=B,check=B);D=A.stdout.strip().split()
			for A in D:
				if A.startswith('5.'):A=A.split('-')[0];return A
			return
		except(C.subprocess.CalledProcessError,FileNotFoundError):return
	def find_offset(J,r2,patterns,is_iA=False):
		H='bins';E=patterns
		if is_iA:A=C.json.loads(r2.cmd('iAj'))
		else:A=C.json.loads(r2.cmd('iaj'))
		D=A[H][0]['arch'];F=A[H][0]['bits']
		if D==_A and F==64:A='arm64'
		elif D==_A and F==16:A=_A
		elif D==_B and F==64:A=_B
		else:print(f"\n{C.lb}[ {C.rd}Error {C.lb}]{C.rd} Unsupported architecture: {D}{C.r}\n");return
		if A in E:
			for A in E:
				for I in E[A]:
					B=r2.cmd(f"/x {I}");B=B.strip().split(' ')[0]
					if B:G=r2.cmd(f"{B};afl.").strip().split(' ')[0];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ssl_verify_peer_cert found at: {C.lb}{B}{C.r}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} function at: {C.y}{G}{C.r}\n");return G