"""
começamos criando uma aplicação Flask chamada app.py. 
Em seguida, criamos uma rota simples chamada /hello-world para testar se a aplicação está funcionando corretamente. 
Depois disso, importamos a classe SQL Alchemy do Flask SQL Alchemy para estabelecer a conexão com o banco de dados. 
Configuramos a chave secreta e a URL do banco de dados. Por fim, discutimos que na próxima aula iremos mapear os usuários e criar as tabelas correspondentes no banco de dados.
"""

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

# Banco de dados

app.confi['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
    