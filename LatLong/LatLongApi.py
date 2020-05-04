# Importando as Bibliotecas

from LatLong.AddressApi import AddressApi
import requests
import json
import pandas as pd

# Criando classe para consultar a Latitude e Longitude

class LatLongApi:

    def __init__(self):

        self.osm = {
            'url' : 'https://nominatim.openstreetmap.org/search?q=',
            'return_format' : '&format=' + 'json',
            'return_count' : '&addressdetails=' + '1'            
        }

        self.states = pd.read_csv('aux_bases/states.txt', sep = ";")

    def consultar(self, cep, numero):

        Add = AddressApi()
        Address = Add.consultar(cep = str(cep))

        states = self.states
        
        Address['estado'] = states.loc[states['Sigla'] == Address['uf'], 'Estado'].values[0]

        text = Address['logradouro'] + ', ' + str(numero) + ' - ' + Address['bairro'] + ', ' + Address['localidade'] + ', ' + Address['estado'] + ', Brasil'

        url = self.osm['url'] + text.replace(' ', '+') + self.osm['return_format'] + self.osm['return_count']

        r = requests.get(url)

        result = r.json()

        return result[0]['lat'], result[0]['lon']

# Testando a Classe

if __name__ == '__main__':

    ll = LatLongApi()
    lat, lon = ll.consultar(cep = 60175055, numero = 1500)

    print('A latitude é {0} e a longitude é {1}!'.format(lat, lon))