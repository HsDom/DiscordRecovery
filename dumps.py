import requests,json,os,colorama,datetime
from json import loads
from colorama import Fore, init
from DiscordClass import Discord
colorama.init()


def AccountInfomation(token):
    Account = Discord(token)
    Info = Account.get_me()

    #Creating Folder and File
    if os.path.exists(f"{Account.get_username()}_{datetime.date.today()}"):
        if not os.path.exists(f"{Account.get_username()}_{datetime.date.today()}/Account Info"):
            os.mkdir(f"{Account.get_username()}_{datetime.date.today()}/Account Info")
    else:
        print(f'{Fore.RED}Folder does not exists')
        return

    print(f'{Fore.WHITE}[{Fore.LIGHTBLUE_EX}+{Fore.WHITE}] Dumping Account Info')
    #create txt using utf-8
    with open(f"{Account.get_username()}_{datetime.date.today()}/Account Info/Account Info.txt", "w", encoding='utf-8') as file:
        file.write(f"Username: {Info['username']}#{Info['discriminator']} \n")
        file.write(f'Bio: {Info["bio"]} \n')
        file.write(f'Email: {Info["email"]} \n')
        file.write(f'Phone: {Info["phone"]} \n')
        file.write(f'Nitro: {Info["premium_type"]} \n')
        file.write(f'2FA: {Info["mfa_enabled"]} \n')
        file.write(f'NSFW Enabled: {Info["nsfw_allowed"]} \n')
        
        file.close()
    
    print(f"{Fore.WHITE}Account Info saved to {Account.get_username()}_{datetime.date.today()}/Account Info/Account Info.txt")

    print(f'{Fore.WHITE}[{Fore.LIGHTBLUE_EX}+{Fore.WHITE}] Dumping Avatar')
    #Download Profile Picture and banner if exists
    with open(f"{Account.get_username()}_{datetime.date.today()}/Account Info/Avatar.png", "wb") as file:
        file.write(requests.get(f'https://cdn.discordapp.com/avatars/{Info["id"]}/{Info["avatar"]}.png?size=1024').content)
        file.close()

    print(f"{Fore.WHITE}Avatar saved to {Account.get_username()}_{datetime.date.today()}/Account Info/Avatar.png")

    if Info['banner'] != None:
        print(f'{Fore.WHITE}[{Fore.LIGHTBLUE_EX}+{Fore.WHITE}] Dumping Banner')
        with open(f"{Account.get_username()}_{datetime.date.today()}/Account Info/Banner.png", "wb") as file:
            file.write(requests.get(f'https://cdn.discordapp.com/banners/{Info["id"]}/{Info["banner"]}.png?size=1024').content)
            file.close()
    
        print(f"{Fore.WHITE}Banner saved to {Account.get_username()}_{datetime.date.today()}/Account Info/Banner.png")


        

def AccountBilling(token):
    Account = Discord(token)
    Info = Account.get_billing()
    Payments = Account.get_payment()

    #Creating Folder and File
    if os.path.exists(f"{Account.get_username()}_{datetime.date.today()}"):
        if not os.path.exists(f"{Account.get_username()}_{datetime.date.today()}/Account Billing"):
            os.mkdir(f"{Account.get_username()}_{datetime.date.today()}/Account Billing")
    else:
        print(f'{Fore.RED}Folder does not exists')
        return

    print(f'{Fore.WHITE}[{Fore.LIGHTBLUE_EX}+{Fore.WHITE}] Dumping Billing Info')
    #create txt using utf-8
    with open(f"{Account.get_username()}_{datetime.date.today()}/Account Billing/Account Billing.txt", "w", encoding='utf-8') as file:
        for item in Info:
            file.write(f"Type: {item['type']} \n")
            if item['type'] == 1:
                file.write(f'Brand: Visa \n')
            elif item['type'] == 2:
                file.write(f'Brand: Paypal \n')
            else:
                file.write(f'Brand: Unknown \n')
            
            try:
                file.write(f'Last 4: {item["last_4"]} \n')
                file.write(f'Expire: {item["expires_month"]}/{item["expires_year"]} \n')
            except:
                pass

            try:
                file.write(f'Email: {item["email"]} \n')
            except:
                pass

            file.write(f'Address: {item["billing_address"]["line_1"]} \n')
            file.write(f'City: {item["billing_address"]["city"]} \n')
            file.write(f'State: {item["billing_address"]["state"]} \n')
            file.write(f'Country: {item["billing_address"]["country"]} \n')
            file.write(f'Zip: {item["billing_address"]["postal_code"]} \n')


            file.write(f' \n')
    
        file.close()
    
    print(f"{Fore.WHITE}Account Billing saved to {Account.get_username()}_{datetime.date.today()}/Account Billing/Account Billing.txt")

    #get payments 
    print(f'{Fore.WHITE}[{Fore.LIGHTBLUE_EX}+{Fore.WHITE}] Dumping Payments')
    #create txt using utf-8
    with open(f"{Account.get_username()}_{datetime.date.today()}/Account Billing/Payments.txt", "w", encoding='utf-8') as file:
        for item in Payments:
            if item['status'] == 1:
                file.write(f"Payment SUCCESSFUL!\n")
            elif item['status'] == 2:
                file.write(f"Payment FAILED!\n")
            else:
                file.write(f"Payment UNKNOWN!\n")
            file.write(f"Product: {item['description']} \n")
            file.write(f'Price: ${item["amount"]/100} \n')
            file.write(f'Currency: {item["currency"]} \n')
            file.write(f'Payment Date: {item["created_at"]} \n')
            try:
                if item['payment_source']['payment_gateway'] == 1:
                    file.write(f'Payment Gateway: Visa \n')
                elif item['payment_source']['payment_gateway'] == 2:
                    file.write(f'Payment Gateway: Paypal \n')
                else:
                    file.write(f'Payment Gateway: Unknown \n')
            except:
                pass

            file.write(f' \n')

        file.close()

    print(f"{Fore.WHITE}Payments saved to {Account.get_username()}_{datetime.date.today()}/Account Billing/Payments.txt")


def AccountGifts(token):
    Account = Discord(token)
    Info = Account.get_gifts()

    #Creating Folder and File
    if os.path.exists(f"{Account.get_username()}_{datetime.date.today()}"):
        if not os.path.exists(f"{Account.get_username()}_{datetime.date.today()}/Account Gifts"):
            os.mkdir(f"{Account.get_username()}_{datetime.date.today()}/Account Gifts")
    else:
        print(f'{Fore.RED}Folder does not exists')
        return

    print(f'{Fore.WHITE}[{Fore.LIGHTBLUE_EX}+{Fore.WHITE}] Dumping Gifts')
    #create txt using utf-8
    with open(f"{Account.get_username()}_{datetime.date.today()}/Account Gifts/Gifts.txt", "w", encoding='utf-8') as file:
        for item in Info:
            file.write(f"Title: {item['promotion']['outbound_title']} \n")
            try:
                file.write(f"Redemption Link: {item['promotion']['outbound_redemption_page_link']} \n")
            except:
                pass

            try:
                file.write(f"Code: {item['promotion']['outbound_redemption_url_format']} \n")
            except:
                pass
            file.write(f"Terms and Conditions: {item['promotion']['outbound_terms_and_conditions']}\n")
            file.write(f"Code: {item['code']} \n")
            file.write(f" \n")
    
        file.close()

    print(f"{Fore.WHITE}Gifts saved to {Account.get_username()}_{datetime.date.today()}/Account Gifts/Gifts.txt")

def AccountRelationships(token):
    Account = Discord(token)
    Info = Account.get_friends()

    #Creating Folder and File
    if os.path.exists(f"{Account.get_username()}_{datetime.date.today()}"):
        if not os.path.exists(f"{Account.get_username()}_{datetime.date.today()}/Account Friends"):
            os.mkdir(f"{Account.get_username()}_{datetime.date.today()}/Account Friends")
    else:
        print(f'{Fore.RED}Folder does not exists')
        return

    print(f'{Fore.WHITE}[{Fore.LIGHTBLUE_EX}+{Fore.WHITE}] Dumping Friends')
    #create txt using utf-8
    with open(f"{Account.get_username()}_{datetime.date.today()}/Account Friends/Friends.txt", "w", encoding='utf-8') as file:
        for item in Info:
            file.write(f"Username: {item['user']['username']}#Discriminator: {item['user']['discriminator']} \n")
            file.write(f"ID: {item['id']} \n")
            file.write(f" \n")
    
        file.close()
    print(f"{Fore.WHITE}Friends saved to {Account.get_username()}_{datetime.date.today()}/Account Friends/Friends.txt")

    #folder for friends avatars
    if not os.path.exists(f"{Account.get_username()}_{datetime.date.today()}/Account Friends/Avatars"):
        if not os.path.exists(f"{Account.get_username()}_{datetime.date.today()}/Account Friends/Avatars"):
            os.mkdir(f"{Account.get_username()}_{datetime.date.today()}/Account Friends/Avatars")

    #get friends avatars
    print(f'{Fore.WHITE}[{Fore.LIGHTBLUE_EX}+{Fore.WHITE}] Dumping Friends Avatars')
    for item in Info:
        try:
            r = requests.get(f"https://cdn.discordapp.com/avatars/{item['user']['id']}/{item['user']['avatar']}.png")
            with open(f"{Account.get_username()}_{datetime.date.today()}/Account Friends/Avatars/{item['user']['username']}#{item['user']['discriminator']}.png", "wb") as file:
                file.write(r.content)
        except:
            pass

    print(f"{Fore.WHITE}Friends avatars saved to {Account.get_username()}_{datetime.date.today()}/Account Friends/Avatars")
    


def AccountMessages(token):
    Account = Discord(token)
    Info = Account.get_channels()

    #Creating Folder and File
    if os.path.exists(f"{Account.get_username()}_{datetime.date.today()}"):
        if not os.path.exists(f"{Account.get_username()}_{datetime.date.today()}/Private Messages"):
            os.mkdir(f"{Account.get_username()}_{datetime.date.today()}/Private Messages")
    else:
        print(f'{Fore.RED}Folder does not exists')
        return

    print(f'{Fore.WHITE}[{Fore.LIGHTBLUE_EX}+{Fore.WHITE}] Dumping Private Messages')
    print(f'{Fore.WHITE}[{Fore.LIGHTBLUE_EX}+{Fore.WHITE}] This may take a while')
    #create txt using utf-8
    for user in Info:
        #creat a folder for each user
        if not os.path.exists(f"{Account.get_username()}_{datetime.date.today()}/Private Messages/{user['recipients'][0]['username']}#{user['recipients'][0]['discriminator']}"):
            os.mkdir(f"{Account.get_username()}_{datetime.date.today()}/Private Messages/{user['recipients'][0]['username']}#{user['recipients'][0]['discriminator']}")
        if not os.path.exists(f"{Account.get_username()}_{datetime.date.today()}/Private Messages/{user['recipients'][0]['username']}#{user['recipients'][0]['discriminator']}/Attachments"):
            os.mkdir(f"{Account.get_username()}_{datetime.date.today()}/Private Messages/{user['recipients'][0]['username']}#{user['recipients'][0]['discriminator']}/Attachments")


        with open(f"{Account.get_username()}_{datetime.date.today()}/Private Messages/{user['recipients'][0]['username']}#{user['recipients'][0]['discriminator']}/{user['recipients'][0]['username']}#{user['recipients'][0]['discriminator']}.txt", "w", encoding='utf-8') as file:
            messages = requests.get(f"https://discord.com/api/v9/channels/{user['id']}/messages?limit=100", headers={'Authorization': token, 'Content-Type': 'application/json'})
            messages = json.loads(messages.text)
            for x in range(100):
                try:
                    if messages[x]['attachments'] != []:
                        file.write(f"{messages[x]['author']['username']}#{messages[x]['author']['discriminator']} : {messages[x]['content']}\n{messages[x]['attachments'][0]['url']} \n")
                    else:
                        file.write(f"{messages[x]['author']['username']}#{messages[x]['author']['discriminator']} : {messages[x]['content']} \n")
                except:
                    pass
            file.close()

        #download attachments
        for x in range(100):
            try:
                if messages[x]['attachments'] != []:
                    r = requests.get(messages[x]['attachments'][0]['url'])
                    with open(f"{Account.get_username()}_{datetime.date.today()}/Private Messages/{user['recipients'][0]['username']}#{user['recipients'][0]['discriminator']}/Attachments/{messages[x]['attachments'][0]['filename']}", "wb") as file:
                        file.write(r.content)
                    os.rename(f"{Account.get_username()}_{datetime.date.today()}/Private Messages/{user['recipients'][0]['username']}#{user['recipients'][0]['discriminator']}/Attachments/{messages[x]['attachments'][0]['filename']}", f"{Account.get_username()}_{datetime.date.today()}/Private Messages/{user['recipients'][0]['username']}#{user['recipients'][0]['discriminator']}/Attachments/{messages[x]['id']}.png")
            except:
                pass

    print(f"{Fore.WHITE}Private Messages saved to {Account.get_username()}_{datetime.date.today()}/Private Messages")

