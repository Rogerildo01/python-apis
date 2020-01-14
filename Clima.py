import requests
import json


chave = '275f71ea'
cidade = input('digite a cidade:')
UF = input('digite UF da cidade:')
UF = UF.upper()
x = 0

clima = requests.get(f'https://api.hgbrasil.com/weather?key={chave}&city_name={cidade},{UF}')  
clima = clima.json()

#print(json.dumps(clima))

saida = (f'Cidade : {cidade}')

print(saida)

for k in clima['results']['forecast']:
    print(k)
    #print('data: '+ k["date"])



