# Author: Junior Tada
import redis

db = redis.Redis(host='localhost', port=6379, db=0)

# dados temporários teste
db.set('ultima_consulta','10/06/2018')
db.set('movimentacao','1500.00')
db.set('ultima_compra_valor','300.00')
db.set('ultima_compra_data','10/06/2018')