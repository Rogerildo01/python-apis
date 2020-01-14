import flask 
import requests
import json
from ConsultarCep import ConsultaCep


cep = input('digite um cep: ')
retorno = ConsultaCep().Cep(cep)

print(retorno)