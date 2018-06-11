from app import app
from sanic.response import json

@app.route('/')
@app.route('index')
async def test(request):
    return json({'teste': 'app3'})