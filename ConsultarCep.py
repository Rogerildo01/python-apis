import requests 
import json

class ConsultaCep:

    def Cep(self, cep):
        # erro = None
        # req = None
        try:
            # print('====================')
            # print('Consuta CEP')
            # print('====================')
            # cep = input('Digite o CEP desejado: ')
            cep = cep.replace('-','')

            if len(cep)!= 8:
                erro = 'Foi digitado quantidade errada de caracteres do CEP.'
                exit()

            req = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            req = req.json()
            retorno = {
                'Endereço':req['logradouro'],
                'Bairro':req['bairro'],
                'Cidade':req['localidade'],
                'UF':req['uf']
            }

            # print('\n')
            # print(f'Endereço: '+req['logradouro'])
            # print(f'Bairro: '+req['bairro'])
            # print(f'Cidade: '+req['localidade'])
            # print(f'UF: '+req['uf']+'\n')

            return retorno
        except:
            print(erro)
            exit()
    
