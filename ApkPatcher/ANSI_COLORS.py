# ————— 𝐀𝐍𝐒𝐈 𝐂𝐎𝐋𝐎𝐑𝐒 —————

class ANSI:
    def __init__(self):

        # =====🔸𝐀𝐍𝐒𝐈 𝐂𝐎𝐋𝐎𝐑𝐒🔸=====

        self.ESC = '\033' # ( Octal )

        # 𝐀𝐍𝐒𝐈 𝐂𝐎𝐋𝐎𝐑 ( 𝐁𝐎𝐋𝐃 = 𝟏𝐦 | 𝐃𝐀𝐑𝐊 = 𝟐𝐦 )

        self.R  = self.ESC + '[31;1m'  # RED
        self.G  = self.ESC + '[32;1m'  # GREEN
        self.Y  = self.ESC + '[33;1m'  # YELLOW
        self.B  = self.ESC + '[34;1m'  # BLUE
        self.P  = self.ESC + '[35;1m'  # PURPLE
        self.C  = self.ESC + '[36;1m'  # CYAN
        self.W  = self.ESC + '[37;1m'  # WHITE

        # 𝐁𝐑𝐈𝐆𝐇𝐓 𝐂𝐎𝐋𝐎𝐑

        self.BR = self.ESC + '[91;1m'  # BRIGHT RED
        self.BG = self.ESC + '[92;1m'  # BRIGHT GREEN
        self.BY = self.ESC + '[93;1m'  # BRIGHT YELLOW
        self.BB = self.ESC + '[94;1m'  # BRIGHT BLUE
        self.BP = self.ESC + '[95;1m'  # BRIGHT PURPLE
        self.BC = self.ESC + '[96;1m'  # BRIGHT CYAN
        self.BW = self.ESC + '[97;1m'  # BRIGHT WHITE

        # 𝐎𝐓𝐇𝐄𝐑 𝐂𝐎𝐋𝐎𝐑

        self.DG = self.ESC + '[32;2m'  # DARK GREEN
        self.GR = self.ESC + '[90;1m'  # GRAY

        # 𝟐𝟓𝟔 𝐂𝐨𝐥𝐨𝐫𝐬 ( 𝐄𝐒𝐂 + '[𝟑𝟖;𝟓;{𝐈𝐃}𝐦' ) [ 𝐈𝐃 - https://user-images.githubusercontent.com/995050/47952855-ecb12480-df75-11e8-89d4-ac26c50e80b9.png ]

        self.PN = self.ESC + '[38;5;213;1m'  # PINK
        self.OG = self.ESC + '[38;5;202;1m'  # ORANGE

        # 𝐂𝐋𝐄𝐀𝐑 𝐂𝐎𝐃𝐄𝐒

        self.CL  = self.ESC + '[2K'  # CLEAR LINE
        self.CC  = self.ESC + '[0m'  # CLEAR COLOR

        # 𝐌𝐎𝐑𝐄 𝐈𝐍𝐅𝐎 [ 𝐋𝐈𝐍𝐊 - https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797 ]

        # =====🔹𝐓𝐀𝐆🔹=====

        self.S = f'{self.B}[{self.C}'
        self.E = f'{self.B}]'
        self.X = f'{self.B}[ {self.P}* {self.B}]'
        self.FYI = f'{self.B}[ {self.P}FYI {self.B}]'
        self.INFO = f'{self.B}[ {self.Y}INFO {self.B}]{self.C}'
        self.WARN = f'{self.B}[ {self.Y}WARN {self.B}]{self.B}'
        self.ERROR = f'{self.B}[ {self.R}ERROR {self.B}]{self.R}'
        self.SUGGEST = f'{self.B}[ {self.Y}SUGGEST {self.B}]{self.C}'