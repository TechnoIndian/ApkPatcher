# ————— 𝐈𝐌𝐏𝐎𝐑𝐓 𝐌𝐎𝐃𝐔𝐋𝐄𝐒 —————

class IMPORT:
    def __init__(self):

        # ---------------- 𝐌𝐮𝐥𝐭𝐢𝐏𝐫𝐨𝐜𝐞𝐬𝐬 / 𝐌𝐮𝐥𝐭𝐢𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 ----------------
        try:
            mp = __import__('multiprocess')
        except ImportError:
            mp = __import__('multiprocessing')

        # ————— 𝐋𝐢𝐛𝐫𝐚𝐫𝐢𝐞𝐬 𝐈𝐦𝐩𝐨𝐫𝐭 —————
        self.re = __import__('re')
        self.os = __import__('os')
        self.sys = __import__('sys')
        self.zlib = __import__('zlib')
        self.json = __import__('json')
        self.time = __import__('time')
        self.shutil = __import__('shutil')
        self.string = __import__('string')
        self.zipfile = __import__('zipfile')
        self.hashlib = __import__('hashlib')
        self.base64 = __import__('base64')
        self.binascii = __import__('binascii')
        self.random = __import__('random')
        self.argparse = __import__('argparse')
        self.subprocess = __import__('subprocess')

        # ————— 𝐄𝐱𝐭𝐫𝐚 𝐋𝐢𝐛𝐫𝐚𝐫𝐢𝐞𝐬 —————
        self.Pool = mp.Pool
        self.Manager = mp.Manager
        self.cpu_count = mp.cpu_count
        self.datetime = __import__('datetime').datetime
        