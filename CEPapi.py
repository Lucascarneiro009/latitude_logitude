# Importando as Bibliotecas

import requests
import json

# Criando classe para consultar o CEP

class CEPapi:

    def __init__(self):

        self.url = 'http://www.viacep.com.br/ws/'

    def consultar(self, cep):
        
        if len(str(cep)) == 8:

            url = self.url + str(cep) + '/json'
            r = requests.get(url)

            if r.status_code == 200:

                return json.loads(r.text)

            else:

                print('Erro ao consultar a API!')

        else:

            print('Por favor, digite um CEP com 8 digitos!')

# Testando a Classe

if __name__ == '__main__':

    CEPapi = CEPapi()
    cep = CEPapi.consultar(cep = 60010030)

    print(cep)
