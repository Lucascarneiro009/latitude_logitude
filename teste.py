# Testando a conversão do CEP e número 

# teste

from LatLong.LatLongApi import LatLongApi

ll = LatLongApi()
lat, lon = ll.consultar(cep = 99999999, numero = 111)

print('A latitude é {0} e a longitude é {1}!'.format(lat, lon))