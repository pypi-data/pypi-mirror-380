import os
from fmconsult.http.api import ApiBase

class RotasBrasilApi(ApiBase):
    
    def __init__(self):
        try:
            self.api_token = os.environ['rotasbrasil.api.token']
            self.base_url = 'https://rotasbrasil.com.br/apiRotas'
            self.headers = {}
        except:
            raise