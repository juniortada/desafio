# Author: Junior Tada
import requests

# Define se o teste será realizado no servidor local ou no servidor AWS
_local = True

# Endereço dos webservices
LOCALHOST = 'http://0.0.0.0:8070/'
AWS = 'http://18.231.77.148:8070/'

if _local:
    SERVIDOR = LOCALHOST
else:
    SERVIDOR = AWS

# Teste Consultar Cliente pelo CPF
consulta = requests.post(SERVIDOR+'webservice/ultima_consulta')
print(consulta.text)