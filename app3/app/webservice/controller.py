# Author: Junior Tada
from sanic import Blueprint
from sanic.response import json

# Define o blueprint
webservice = Blueprint('webservice')

@webservice.route('/teste', methods=['GET','POST'])
async def teste(request):
    return json({'teste': 'teste'})