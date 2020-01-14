import json
import requests
import unicodedata
from pprint import pprint
import pyodbc


nome = input('digite o artista:')
token_acesso = 'wuNJxmNuU0ekEGyVS82LuSVOXe9XAx2jyWBkAEek65SUxjun4pARmMXt4MFzby5u'

url = 'https://api.genius.com/search/'
nome = nome.replace (" ","-")

params = {'q': nome,
        'sort': "popularity",
        'per_page': "10",
        'text_format': "plain"}
headers = {'Authorization': 'Bearer {}'.format(token_acesso)}

rqst = requests.get(url,headers = headers,params = params)

load_json = json.loads(rqst.text)
#pprint(retorno)
#with open(f'{nome}.json','w') as file: 
#    file.write(rqst.text)
#   file.close()
#qtd = len(load_json["result"]["title"])
#print(qtd)
nome = (f'Artista : {nome}')
x = 0

while (x < 10):
        retorno = []
        retorno.append(nome.upper())
        for hits in load_json["response"]["hits"]:
                x += 1
                lista = {}
                lista['Top'] = x
                lista['Musica'] = hits["result"]["title"]
                lista['Visualizações'] = hits["result"]['stats']['pageviews']
                retorno.append(lista)
print(retorno)
