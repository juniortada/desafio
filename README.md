# Desafio
Os código dos servidores e os bancos de dados estão hospedados em serviços AWS.

## Instalação e Dependências

- AWS

Para rodar a consulta aos dados do webservice é necessário apenas
o python 3.6 e a lib requests.
Para Executar os testes:

```sh
python3 app1/teste_app1.py
python3 app2/teste_app2.py
python3 app3/teste_app3.py
```


- Servidor Local

Para rodar todos os aplicativos e servidores, além do python 3.6 
é necessário instalar flask, sanic, sqlalchemy, postgreSQL, requests, psycopg2 e redis.

PostgreSQL, psycopg2 e redis devem ser instalados pelo instalador de pacotes do sistema.
As outras dependências, podem ser instaladas por pip.

```sh
pip3 install -r dependencias.txt
```

Para Executar os servidores do webservices:

```sh
python3 app1/app/run.py
python3 app2/app/run.py
python3 app3/app/run.py
```

Agora é preciso editar o arquivo config de cada app,
com os dados do banco de dados.
Exemplo app1/app/config.json: 

```python
postgresql+psycopg2://nome_user_banco:senha_user_banco@localhost/base_a
```

Por fim, mude o conteúdo da variável _local = True
no arquivo de app1/teste_app1.py e app2/teste_app2.py 


```sh
python3 app1/teste_app1.py
python3 app2/teste_app2.py
python3 app3/teste_app3.py
```