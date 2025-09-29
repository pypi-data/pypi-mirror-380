from enum import Enum
from typing import TypedDict

class Coordenada(TypedDict):
    latitude: float
    longitude: float

class Veiculo(str, Enum):
    AUTO = 'auto'
    CARRO = 'carro'
    CAMINHAO = 'caminhao'
    ONIBUS = 'onibus'
    MOTO = 'moto'