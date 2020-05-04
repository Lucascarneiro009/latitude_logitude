# Testando a conversão do CEP e número 

from LatLong.LatLongApi import LatLongApi

ll = LatLongApi()
lat, lon = ll.consultar(cep = 60160150, numero = 156)

print('A latitude é {0} e a longitude é {1}!'.format(lat, lon))