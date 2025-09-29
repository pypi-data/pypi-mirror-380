import logging, jsonpickle
from http import HTTPMethod
from typing import List
from fmconsult.utils.url import UrlUtil
from rotasbrasil.api import RotasBrasilApi
from rotasbrasil.dtos.rota import Coordenada, Veiculo

class Rotas(RotasBrasilApi):

    def __init__(self):
        super().__init__()

    def get_by_coordenadas(
        self, 
        pontos: List[Coordenada], 
        veiculo: Veiculo = Veiculo.AUTO, 
        eixo=2, 
        tabela='a', 
        paradas=False
    ):
        try:
            logging.info(f'get route by coordinates...')
            self.endpoint_url = UrlUtil().make_url(self.base_url, ['coordenadas'])
            res = self.call_request(
                http_method=HTTPMethod.GET,
                request_url=self.endpoint_url,
                params={
                    'pontos': ";".join(f"{p['longitude']},{p['latitude']}" for p in pontos),
                    'veiculo': veiculo.value,
                    'eixo': eixo,
                    'tabela': tabela,
                    'paradas': paradas,
                    'token': self.api_token
                }
            )
            return jsonpickle.decode(res)
        except:
            raise