import requests,json

class Discord:
    def __init__(self,token):
        self.token = token
        self.headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        self.USER_DATA_URL = 'https://discordapp.com/api/v9/users/@me'
        self.USER_BILLING_URL = 'https://discordapp.com/api/v9/users/@me/billing/payment-sources'
        self.USER_PAYMENT_URL = 'https://discord.com/api/v9/users/@me/billing/payments?limit=20'
        self.USER_GIFTS_URL = 'https://discord.com/api/v9/users/@me/outbound-promotions/codes'
        self.USER_FRIENDS = 'https://discord.com/api/v9/users/@me/relationships'
        self.USER_CHANNELS = 'https://discord.com/api/v9/users/@me/channels'
        self.USER_DATA = requests.get(self.USER_DATA_URL, headers=self.headers).text
        self.USER_DATA = json.loads(self.USER_DATA)
        self.USER_BILLING = requests.get(self.USER_BILLING_URL, headers=self.headers).text
        self.USER_BILLING = json.loads(self.USER_BILLING)
        self.USER_PAYMENT = requests.get(self.USER_PAYMENT_URL, headers=self.headers).text
        self.USER_PAYMENT = json.loads(self.USER_PAYMENT)
        self.USER_GIFTS = requests.get(self.USER_GIFTS_URL, headers=self.headers).text
        self.USER_GIFTS = json.loads(self.USER_GIFTS)
        self.USER_FRIENDS = requests.get(self.USER_FRIENDS, headers=self.headers).text
        self.USER_FRIENDS = json.loads(self.USER_FRIENDS)
        self.USER_CHANNELS = requests.get(self.USER_CHANNELS, headers=self.headers).text
        self.USER_CHANNELS = json.loads(self.USER_CHANNELS)

    def is_valid(self):
        try:
            self.USER_DATA['username']
            return True
        except:
            return False

    def get_username(self):
        return self.USER_DATA['username']

    def get_discriminator(self):
        return self.USER_DATA['discriminator']

    def get_me(self):
        return self.USER_DATA

    def get_billing(self):
        return self.USER_BILLING

    def get_payment(self):
        return self.USER_PAYMENT
    
    def get_gifts(self):
        return self.USER_GIFTS

    def get_friends(self):
        return self.USER_FRIENDS

    def get_channels(self):
        return self.USER_CHANNELS

