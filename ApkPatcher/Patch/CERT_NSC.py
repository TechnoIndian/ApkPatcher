from ..ANSI_COLORS import ANSI; C = ANSI()
from ..MODULES import IMPORT; M = IMPORT()


# ---------------- Write RAW CERT ----------------
def Write_CERT(decompile_dir, isAPKEditor, CA_Cert):

    if isAPKEditor:
        decompile_dir = M.os.path.join(decompile_dir, 'resources', 'package_1')

    Default_CERT = """\
-----BEGIN CERTIFICATE-----
MIIDczCCAlugAwIBAgIHALdlRG+pDzANBgkqhkiG9w0BAQ0FADBHMRswGQYDVQQD
DBJIdHRwQ2FuYXJ5IFJvb3QgQ0ExEzARBgNVBAoMCkh0dHBDYW5hcnkxEzARBgNV
BAsMCkh0dHBDYW5hcnkwHhcNMjIwMzA2MTIxMTAxWhcNMzMwMzAzMTIxMTAxWjBH
MRswGQYDVQQDDBJIdHRwQ2FuYXJ5IFJvb3QgQ0ExEzARBgNVBAoMCkh0dHBDYW5h
cnkxEzARBgNVBAsMCkh0dHBDYW5hcnkwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
ggEKAoIBAQCrzm03w7mMvHujpl0IMb/jgxEwJdUsfpazdgUVdsq+7T/Ks8O3NMFP
d4hl6sUgRbaMx3Uz8WolEtz/wu/fdGnrUVDcdWXiJKfhLUUP3KuYwE9tahrfRf14
Yg/xGoA8Pz1BEaUnsJSt6RB5qm5fwn2O8QRykAbgr11or2rr8KQWMaoeciN04tjd
kkcWmPWNSytwea7l1LOrolUXGcbFlpXpGY1cTCoB1RZJe7HkUd1zdYhKUlhHZo3P
in9FhGa/UJGlyWXmT3ybY0nuPtIvqJ3Ao4FwP1zkrrqvS0UCi3QvJZrZ8EEju0U9
NM009njCT6sX56TUG189Dk1uettEiTtlAgMBAAGjZDBiMB0GA1UdDgQWBBT0yJzC
NcHzwIVXMTnvgPp74q1KWjAPBgNVHRMBAf8EBTADAQH/MAsGA1UdDwQEAwIBtjAj
BgNVHSUEHDAaBggrBgEFBQcDAQYIKwYBBQUHAwIGBFUdJQAwDQYJKoZIhvcNAQEN
BQADggEBAA9H0nWzKUKKfgu6RI657wVgSONymRRnpzQ+GNjbDoi6CR3QWL8SvPe8
s61nM8xUP0aMFv0VYrd80sICTQXAEld+/eXoDib7qxg1I2I9v+FkLwPSN2FaJRkv
GKxfki4s6kpNNvmO5X+1eR1fK7Y/lrlp9V7zP8oMbcBuNkiWO6UYNGGGuqxFr3H4
f4LRvODZks/aGea2E0pdiAnAZCIGZS3Mg5cS7wA5vUSkKwpBIcYFVdYTF/xblJfX
OBoyS7CMCG66aSfs3zk4lT8fVwtFJjvkM01gH3A4q6T78rZ/Nkx01GC90Y1+xDAW
0o1SBaeL3tulFzqhMkl5KW0F3vYpP8k=
-----END CERTIFICATE-----"""

    raw_dir = M.os.path.join(decompile_dir, 'res', 'raw')

    M.os.makedirs(raw_dir, exist_ok=True)

    addCERT = []

    if CA_Cert:
        for idx, cert_path in enumerate(CA_Cert, start=1):
            raw_file = f'Techno_India_{idx}.pem' if idx > 1 else 'Techno_India.pem'
            M.shutil.copy(cert_path, M.os.path.join(raw_dir, raw_file))

            addCERT.append(raw_file)

        print(
            f"\n{C.S} Certificate {C.E}{C.C} Your Certificate Path...\n"
            f"{C.G}       |\n       |\n       └──── {C.CC}Input ~{C.G}#{C.Y} {', '.join(CA_Cert)} {C.G} ✔\n"
        )

        print(f"\n{C.S} Write Certificate {C.E} {C.OG}➸❥ {C.Y}raw/{', '.join(addCERT)} {C.G} ✔\n")

    else:
        raw_path = M.os.path.join(raw_dir, 'Techno_India.pem')

        open(raw_path, 'w', encoding='utf-8', errors='ignore').write(Default_CERT)

        print(f"\n{C.S} Certificate {C.E}{C.G} The default certificate is from TechnoIndia's Modded HttpCanary... ✔\n")

        print(f"\n{C.S} Write Default Certificate {C.E} {C.OG}➸❥ {C.Y}{M.os.path.basename(raw_dir)}/Techno_India.pem {C.G} ✔\n")


# ---------------- Write NSC XML ----------------
def Write_NSC(decompile_dir, isAPKEditor, CA_Cert, xml_file='network_security_config.xml'):

    Write_CERT(decompile_dir, isAPKEditor, CA_Cert)

    if isAPKEditor:
        decompile_dir = M.os.path.join(decompile_dir, 'resources', 'package_1')

    NSC = """\
<?xml version="1.0" encoding="utf-8"?>
<network-security-config xmlns:android="http://schemas.android.com/apk/res/android">
    <domain-override host="*" domain-override-cleartext-traffic-permitted="true" />
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">*</domain>
        <domain includeSubdomains="true">0.0.0.0</domain>
        <domain includeSubdomains="true">127.0.0.1</domain>
        <trust-anchors>
            {cert_PlaceHolder}
            <certificates src="system" overridePins="true" />
            <certificates src="user" overridePins="true" />
        </trust-anchors>
    </domain-config>
    <base-config cleartextTrafficPermitted="true">
        <trust-anchors>
            {cert_PlaceHolder}
            <certificates src="system" overridePins="true" />
            <certificates src="user" overridePins="true" />
        </trust-anchors>
    </base-config>
    <debug-overrides cleartextTrafficPermitted="true">
        <trust-anchors>
            {cert_PlaceHolder}
            <certificates src="system" overridePins="true" />
            <certificates src="user" overridePins="true" />
        </trust-anchors>
    </debug-overrides>
</network-security-config>"""

    cert_Entries = ""

    if CA_Cert:
        for idx, _ in enumerate(CA_Cert, start=1):
            CERT_Name = f'Techno_India_{idx}' if idx > 1 else 'Techno_India'
            cert_Entries += f'            <certificates src="@raw/{CERT_Name}" overridePins="true" />\n'

    else:
        cert_Entries += '            <certificates src="@raw/Techno_India" overridePins="true" />\n'

    NSC_XML = NSC.format(cert_PlaceHolder = cert_Entries.strip())

    xml_dir = M.os.path.join(decompile_dir, 'res', 'xml')

    M.os.makedirs(xml_dir, exist_ok=True)

    xml_path = M.os.path.join(xml_dir, xml_file)

    open(xml_path, 'w', encoding='utf-8', errors='ignore').write(NSC_XML)

    print(f"\n{C.S} Write Network Config {C.E} {C.OG}➸❥ {C.Y}{M.os.path.basename(xml_dir)}/{xml_file} {C.G} ✔\n")

    if isAPKEditor:
        update_public_xml(decompile_dir, CA_Cert)


# ---------------- For isAPKEditor ----------------
def update_public_xml(decompile_dir, CA_Cert):

    public_xml_path = M.os.path.join(decompile_dir, 'res', 'values', 'public.xml')  

    public_xml = open(public_xml_path, 'r', encoding='utf-8', errors='ignore').readlines()

    raw_ids = []
    xml_ids = []

    raw_xml_regex = M.re.compile(r'<public id="(0x[0-9a-fA-F]+)" type="(raw|xml)" name="([^"]*)" />')

    raw_found = False
    xml_found = False

    for line in public_xml:
        for match in raw_xml_regex.findall(line):
            res_id = int(match[0], 16)
            res_type = match[1]
            res_name = match[2]

            if res_type == "raw" and res_name == "Techno_India":
                raw_found = True
            elif res_type == "xml" and res_name == "network_security_config":
                xml_found = True

            if res_type == "raw":
                raw_ids.append(res_id)
            elif res_type == "xml":
                xml_ids.append(res_id)

    if raw_found and xml_found:
        return

    new_raw_id = max(raw_ids) + 1 if raw_ids else 0x7fffff01
    new_xml_id = max(xml_ids) + 1 if xml_ids else 0x7ffffff1

    new_entries = []

    if not raw_found:
        if CA_Cert:
            for idx, _ in enumerate(CA_Cert, start=1):
                CERT_Name = f'Techno_India_{idx}' if idx > 1 else 'Techno_India'
                new_entries.append(f'  <public id="0x{new_raw_id:08X}" type="raw" name="{CERT_Name}" />\n')
                new_raw_id += 1

        else:
            new_entries.append(f'  <public id="0x{new_raw_id:08X}" type="raw" name="Techno_India" />\n')

    if not xml_found:
        new_entries.append(f'  <public id="0x{new_xml_id:08X}" type="xml" name="network_security_config" />\n')

    for idx in range(len(public_xml)):
        if "</resources>" in public_xml[idx]:
            public_xml[idx:idx] = new_entries
            break

    open(public_xml_path, 'w', encoding='utf-8', errors='ignore').writelines(public_xml)

    print(f"\n{C.S} Write New Entries {C.E} {C.OG}➸❥ {C.G}public.xml\n\n{C.OG}{''.join(new_entries).strip()}\n")