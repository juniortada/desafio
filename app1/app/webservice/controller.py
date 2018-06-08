# Author: Junior Tada
from flask import Blueprint, request, render_template, jsonify
from app.webservice.model import Cidade, Endereco, Divida, Cliente


# Define the blueprint
webservice = Blueprint('webservice', __name__)


@webservice.route('/consultar_cpf', methods=['GET', 'POST'])
def consultar_cpf():
    """ 
    Método que exibe a página para consultar CPF.
    :return: View de página html.
    """
    return render_template("webservice/consulta_cpf.html")