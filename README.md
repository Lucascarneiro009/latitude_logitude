# Converter CEP em Latitude e Longitude

Esse projeto tem como principal objetivo facilitar a conversão entre CEP e latitude e longitude.

OBS: Em desenvolvimento... porém, ja com uma primeira versão funcional!

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
A latitude é -3.7259426 e a longitude é -38.5203422!

