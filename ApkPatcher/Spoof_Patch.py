import os, sys, shutil; exit([shutil.rmtree(os.path.dirname(os.path.abspath(__file__))), None][1]) if "/".join(sys.argv[0].split("\\")).split("/")[-1] != "Spoof_Patch.py" and "/".join(__file__.split("\\")).split("/")[-1] != "Spoof_Patch.py" else None

try:
    from .C_M import CM;from.Random_INFO import R_I; C = CM(); RI = R_I();
except ImportError as e:
    print(f"Import error: {e}"); exit([shutil.rmtree(os.path.dirname(os.path.abspath(__file__))), None][1])

# Second Script
class S_S_P:
    def __init__(self):
        self.smali_folders = []
        self.matching_files = []
        self.isIMEI = self.generate_imei()
        self.lat_hex, self.lon_hex = self.generate_lat_lon_hex()
        self.device_id, self.random_seed = self.generateDeviceId()
    
    def find_smali_folders(self, base_folder):
        self.smali_folders = []
        for root, dirs, _ in C.os.walk(base_folder):
            for dir_name in dirs:
                if dir_name == "smali" or dir_name.startswith("smali_classes"):
                    self.smali_folders.append(C.os.path.join(root, dir_name))
        return self.smali_folders

    def generate_imei(self):
        imei = ''.join(str(C.random.randint(0, 9)) for _ in range(14))
        check_digit = (sum(int(d) if i % 2 == 0 else sum(divmod(int(d) * 2, 10)) for i, d in enumerate(imei)) * 9) % 10
        return imei + str(check_digit)

    def generate_lat_lon_hex(self):
        scale_factor = 10**12
        lat, lon = round(C.random.uniform(-90.0, 90.0), 6), round(C.random.uniform(-180.0, 180.0), 6)
        lat_hex = hex(int(abs(lat) * scale_factor)) + "L"
        lon_hex = hex(int(abs(lon) * scale_factor)) + "L"
        return lat_hex, lon_hex
        
    def generate_random_mac_address(self):
        return ':'.join([''.join(C.random.choices('0123456789ABCDEF', k=2)) for _ in range(6)])
        
    def generateDeviceId(self):
        volatile_seed = "12345"
        seed = ''.join(C.random.choice(C.string.ascii_letters + C.string.digits) for _ in range(16))
        m = C.hashlib.md5()
        m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
        return m.hexdigest()[:16], seed

    # S_T_S
    def S_T_S(self, smali_folder_paths, target_strings):
        self.matching_files = []
        total_matching_files = 0

        for smali_folder_path in smali_folder_paths:
            for root, _, files in C.os.walk(smali_folder_path):
                for file in files:
                    if file.endswith('.smali'):
                        file_path = C.os.path.join(root, file)
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                            content = f.read()
                    
                        for target_string in target_strings:
                            if target_string in content:
                                total_matching_files += 1
                                print(f"\r{C.lb}[ {C.pr}* {C.lb}] {C.c} Find Target Smali {C.g}➸❥ {total_matching_files}", end='', flush=True)
                                self.matching_files.append(file_path)
                                break

        print(f" {C.g}✔", flush=True)
        print(f'\n{C.r}_____________________________________________________________{C.r}\n')
        return self.matching_files

    # Find Target .smail/class/string/method etc
    def F_S_R(self, smali_folder_paths, isID):
        RI.get_random_device_info()
        target_strings = [
            'Landroid/os/Build;->MANUFACTURER:Ljava/lang/String;',
            'Landroid/os/Build;->BRAND:Ljava/lang/String;',
            'Landroid/os/Build;->MODEL:Ljava/lang/String;',
            'Landroid/os/Build;->PRODUCT:Ljava/lang/String;',
            'Landroid/os/Build;->DEVICE:Ljava/lang/String;',
            'Landroid/os/Build;->BOARD:Ljava/lang/String;',
            'Landroid/os/Build;->getRadioVersion()Ljava/lang/String;'
            'Landroid/os/Build;->RADIO:Ljava/lang/String;',
            'Landroid/os/Build;->HARDWARE:Ljava/lang/String;',
            'Landroid/os/Build;->BOOTLOADER:Ljava/lang/String;',
            'Landroid/os/Build;->FINGERPRINT:Ljava/lang/String;',
            'Landroid/os/Build;->ID:Ljava/lang/String;',
            'Landroid/os/Build;->SERIAL:Ljava/lang/String;',
            'Landroid/os/Build;->DISPLAY:Ljava/lang/String;',
            'Landroid/os/Build;->HOST:Ljava/lang/String;',
            'Landroid/os/Build;->getDevice()Ljava/lang/String;',
            'Landroid/os/Build;->getHardware()Ljava/lang/String;',
            'Landroid/location/Location;->getLongitude()D',
            'Landroid/location/Location;->getLatitude()D',
            'Landroid/location/Location;->isFromMockProvider()Z',
            'Landroid/location/Location;->isMock()Z',
            'ip:Ljava/lang/String;',
            'Landroid/content/pm/PackageManager;->getInstallerPackageName(Ljava/lang/String;)Ljava/lang/String;',
            'Landroid/provider/Settings$Secure;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;',
            'Landroid/telephony/TelephonyManager;->getDeviceId()Ljava/lang/String;',
            'Landroid/net/wifi/WifiInfo;->getBSSID()Ljava/lang/String;',
            'Landroid/net/wifi/WifiInfo;->getMacAddress()Ljava/lang/String;',
            'Landroid/bluetooth/BluetoothAdapter;->getAddress()Ljava/lang/String;'
        ]

        self.matching_files = self.S_T_S(smali_folder_paths, target_strings)
        if self.matching_files:
            self.A_R_S(self.matching_files, isID)
        else:
            pass
        
    # Patches
    def A_R_S(self, matching_files, isID):
        patterns = [
            # Build Info
            (r'sget-object (.*), Landroid/os/Build;->MANUFACTURER:Ljava/lang/String;', rf'const-string \1, "{RI.is_manufacturer}"', f"MANUFACTURER ➸❥ {C.rkj}{RI.is_manufacturer}"),
            (r'sget-object (.*), Landroid/os/Build;->BRAND:Ljava/lang/String;', rf'const-string \1, "{RI.is_brand}"', f"BRAND ➸❥ {C.rkj}{RI.is_brand}"),
            (r'sget-object (.*), Landroid/os/Build;->MODEL:Ljava/lang/String;', rf'const-string \1, "{RI.is_model}"', f"MODEL ➸❥ {C.rkj}{RI.is_model}"),
            (r'sget-object (.*), Landroid/os/Build;->PRODUCT:Ljava/lang/String;', rf'const-string \1, "{RI.is_product}"', f"PRODUCT ➸❥ {C.rkj}{RI.is_product}"),
            (r'sget-object (.*), Landroid/os/Build;->DEVICE:Ljava/lang/String;', rf'const-string \1, "{RI.is_device}"', f"DEVICE ➸❥ {C.rkj}{RI.is_device}"),
            (r'sget-object (.*), Landroid/os/Build;->BOARD:Ljava/lang/String;', rf'const-string \1, "{RI.is_board}"', f"BOARD ➸❥ {C.rkj}{RI.is_board}"),
            (r'invoke-static \{\}, Landroid/os/Build;->getRadioVersion\(\)Ljava/lang/String;\n\n    move-result-object (.*)', rf'const-string \1, "Unknown"', f"getRadioVersion ➸❥ {C.rkj}Unknown"),
            (r'sget-object (.*), Landroid/os/Build;->RADIO:Ljava/lang/String;', rf'const-string \1, "Unknown"', f"RADIO ➸❥ {C.rkj}Unknown"),
            (r'sget-object (.*), Landroid/os/Build;->HARDWARE:Ljava/lang/String;', rf'const-string \1, "{RI.is_hardware}"', f"HARDWARE ➸❥ {C.rkj}{RI.is_hardware}"),
            (r'sget-object (.*), Landroid/os/Build;->BOOTLOADER:Ljava/lang/String;', rf'const-string \1, "Unknown"', f"BOOTLOADER ➸❥ {C.rkj}Unknown"),
            (r'sget-object (.*), Landroid/os/Build;->FINGERPRINT:Ljava/lang/String;', rf'const-string \1, "{RI.is_fingerprint}"', f"FINGERPRINT ➸❥ {C.rkj}{RI.is_fingerprint}"),
            (r'sget-object (.*), Landroid/os/Build;->ID:Ljava/lang/String;', rf'const-string \1, "{RI.is_id}"', f"ID ➸❥ {C.rkj}{RI.is_id}"),
            (r'sget-object (.*), Landroid/os/Build;->SERIAL:Ljava/lang/String;', rf'const-string \1, "Unknown"', f"SERIAL ➸❥ {C.rkj}Unknown"),
            (r'sget-object (.*), Landroid/os/Build;->DISPLAY:Ljava/lang/String;', rf'const-string \1, "{RI.is_display}"', f"DISPLAY ➸❥ {C.rkj}{RI.is_display}"),
            (r'sget-object (.*), Landroid/os/Build;->HOST:Ljava/lang/String;', rf'const-string \1, "localhost"', f"HOST ➸❥ {C.rkj}localhost"),
            (r'const-string .*, "(generic|goldfish)"[^>]*invoke-static .*, Landroid/os/Build;->get(Device|Hardware)\(\)Ljava/lang/String;[^>]*move-result-object .*[^>]*invoke-virtual .*, Ljava/lang/String;->contains\(Ljava/lang/CharSequence;\)Z[^>]*move-result (.*)', rf'const/4 \3, 0x0', "Bypassed Device detection"),

            # Mock Location & Update & Pkg Install Fixed
            (r'(Landroid/location/Location;->getLongitude\(\)D\s+)move-result-wide(.*)', rf'\1const-wide\2, {self.lon_hex}', f"Longitude ➸❥ {C.rkj}{self.lon_hex}"),
            (r'(Landroid/location/Location;->getLatitude\(\)D\s+)move-result-wide(.*)', rf'\1const-wide\2, {self.lat_hex}', f"Latitude ➸❥ {C.rkj}{self.lat_hex}"),
            (r'invoke-virtual .*, Landroid/location/Location;->(isFromMockProvider|isMock)\(\)Z[^>]*move-result (.*)', rf'const/4 \2, 0x0', "Bypassed Mock Detection"),
            (r'iget-object (.*), (.*), L.*;->ip:Ljava/lang/String;', rf'const-string \1, "127.0.0.1"', f"IP To LocalHost ➸❥ {C.rkj}127.0.0.1"),
            (r'(invoke-virtual .*, Landroid/content/pm/PackageManager;->getInstallerPackageName\(Ljava/lang/String;\)Ljava/lang/String;[^>]*)move-result-object (.*)', r'\1const-string \2, "com.android.vending"', "Fixed Installer"),
            
            # Settings$Secure
            (r'(const-string.*"bluetooth_address"[^>]*invoke-static.*Landroid/provider/Settings\$Secure;->getString\(Landroid/content/ContentResolver;Ljava/lang/String;\)Ljava/lang/String;[^>]*)move-result-object(.*)', rf'\1const-string\2, "{self.generate_random_mac_address()}"', f"Bluetooth Address ➸❥ {C.rkj}{self.generate_random_mac_address()}"),

            # Network Info
            (r'(Landroid/net/wifi/WifiInfo;->getBSSID\(\)Ljava/lang/String;[^>]*)move-result-object(.*)', rf'\1const-string\2, "{self.generate_random_mac_address()}"', f"WifiInfo BSSID ➸❥ {C.rkj}{self.generate_random_mac_address()}"),
            (r'(Landroid/net/wifi/WifiInfo;->getMacAddress\(\)Ljava/lang/String;\s+)move-result-object(.*)', rf'\1const-string\2, "{self.generate_random_mac_address()}"', f"WifiInfo MacAddress ➸❥ {C.rkj}{self.generate_random_mac_address()}"),
            (r'(invoke-virtual .*, Landroid/bluetooth/BluetoothDevice;->getAddress\(\)Ljava/lang/String;\s+)move-result-object(.*)', rf'\1const-string\2, "{self.generate_random_mac_address()}"', f"BluetoothDevice Address ➸❥ {C.rkj}{self.generate_random_mac_address()}"),

            # TelephonyManager
            (r'(invoke-virtual.*Landroid/telephony/TelephonyManager;->getDeviceId\(\)Ljava/lang/String;[^>]*)move-result-object(.*)', rf'\1const-string\2, "{self.isIMEI}"', f"IMEI NO (Device ID) ➸❥ {C.rkj}{self.isIMEI}")
        ]
        
        if isID:
            # Custom Device ID
            patterns.append((r'(const-string.*"android_id"[^>]*invoke-static.*Landroid/provider/Settings\$Secure;->getString\(Landroid/content/ContentResolver;Ljava/lang/String;\)Ljava/lang/String;[^>]*)move-result-object(.*)', rf'\1const-string\2, "{isID}"', f"Custom Android ID ➸❥ {C.rkj}{isID}"))
        else:
            patterns.append((r'(const-string.*"android_id"[^>]*invoke-static.*Landroid/provider/Settings\$Secure;->getString\(Landroid/content/ContentResolver;Ljava/lang/String;\)Ljava/lang/String;[^>]*)move-result-object(.*)', rf'\1const-string\2, "{self.device_id}"', f"Android ID ➸❥ {C.rkj}{self.device_id}"))

        for pattern, replacement, description in patterns:
            count_applied = 0
            applied_files = set()

            for file_path in matching_files:
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    new_content = C.re.sub(pattern, replacement, content)
                    if new_content != content:
                        if file_path not in applied_files:
                            applied_files.add(file_path)
                        count_applied += 1

                        with open(file_path, "w", encoding="utf-8", errors="ignore") as f:
                            f.write(new_content)

                except Exception as e:
                    print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} applying pattern in {file_path}: {e}")

            if count_applied > 0:
                print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.g}{description}{C.r}")
                print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Applying pattern ➸❥ {C.pr}{pattern}{C.r}")
                for file_path in applied_files:
                    print(f"{C.g}  |\n  └──── {C.r}~{C.g}$ {C.y}{C.os.path.basename(file_path)} {C.g}✔")
                print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Pattern Applied {C.g}➸❥ {C.pr}{count_applied} {C.c}Time/Smali {C.g}✔")
                print(f'\n{C.r}_____________________________________________________________{C.r}\n')