# Author: Junior Tada
import requests

# Define se o teste será realizado no servidor local ou no servidor AWS
_local = True

# Endereço dos webservices
LOCALHOST = 'http://0.0.0.0:8080/'
AWS = 'http://54.233.92.199:8080/'

if _local:
    SERVIDOR = LOCALHOST
else:
    SERVIDOR = AWS

# cliente
cliente = {'cpf':'123456789-01'}

# Teste Consultar Cliente pelo CPF
consultar_cpf = requests.post(SERVIDOR+'webservice/consultar_cpf', json=cliente)
print(consultar_cpf.text)

# Teste Consultar Dividas
consultar_dividas = requests.post(SERVIDOR+'webservice/consultar_dividas', json=cliente)
print(consultar_dividas.text)