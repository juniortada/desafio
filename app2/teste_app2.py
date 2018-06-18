# Author: Junior Tada
import requests

# Define se o teste será realizado no servidor local ou no servidor AWS
_local = True

# Endereço dos webservices
LOCALHOST = 'http://0.0.0.0:8090/'
AWS = 'http://18.231.77.148:8090/'

if _local:
    SERVIDOR = LOCALHOST
else:
    SERVIDOR = AWS

# cliente
cliente = {'cpf':'123456789-01'}

# Teste Consultar Cliente pelo CPF
consulta = requests.post(SERVIDOR+'webservice/consultar_dados_cliente', json=cliente)
print(consulta.text)

# Teste Consultar Cliente pelo CPF
consulta = requests.post(SERVIDOR+'webservice/consultar_fonte_renda', json=cliente)
print(consulta.text)