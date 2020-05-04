# Converter CEP em Latitude e Longitude

Esse projeto tem como principal objetivo facilitar a conversão entre CEP e latitude e longitude.

OBS: Estamos utilizando como linguagem padrão python para essa primeira versão do projeto.

#### Bibliotecas necessários

- Requests
- Json
- Pandas

# Exemplos

#### Consulta via python

``` python
from LatLong.LatLongApi import LatLongApi

ll = LatLongApi()
lat, lon = ll.consultar(cep = 60160150, numero = 156)

print('A latitude é {0} e a longitude é {1}!'.format(lat, lon))
```
