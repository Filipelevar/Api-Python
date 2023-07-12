from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:filipe1020@localhost:5432/RickandMorty'
db = SQLAlchemy(app)


class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True)
    status = db.Column(db.String(200))
    species = db.Column(db.String(200))
    type = db.Column(db.String(200))
    gender = db.Column(db.String(200))

    def __init__(self, nome, status, species, type, gender):
        self.nome = nome
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    char = Characters('Filipe', 'Alive', 'Allien', '""', 'Undefined')
    db.session.add(char)
    db.session.commit()
    # return "Hello World!"
    return jsonify({'data': 'hello', 'message': 'World', 'name': 'Filipe', 'age': 25})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=105, debug=True)


# É uma variável especial em Python que assume o valor do nome do script.
# Essa linha garante que nosso aplicativo Flask seja executado apenas quando for executado no arquivo principal e não quando for importado para algum outro arquivo

# hostespecifica o servidor no qual queremos que nosso aplicativo flask seja executado. O valor padrão para hosté localhostou127.0.0.1
# 0.0.0.0significa “todos os endereços IPv4 na máquina local”. Isso garante que o servidor seja acessível a partir de todos os endereços.
# O portvalor padrão é 5000e você pode definir o parâmetro portpara usar o número da porta de sua escolha.


# proximo passo conectar


# Regras variaveis

# !!Você pode adicionar seções variáveis ​​a um URL usando <variable_name>. A função recebe a variável como um argumento de palavra-chave.!!

# from flask import Flask
# app = Flask(__name__)

# @app.route( '/<int:number>/' )
# def  incrementer ( number ):
#     return  "O número incrementado é " + str (number+ 1 )

# @app.route( '/ <string:name>/' )
# def  olá ( nome ):
#     return  "Olá " + nome

# app.run()
