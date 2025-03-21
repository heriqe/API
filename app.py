from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')

usuarios = [
    'Kaidy',
    'Renna',
    'Julia',
    'Yasmin',
    'Felipe',
    'Malta',
    'Henrique'
]

@app.route('/users',methods=['GET'])
def pegar_usuarios():
    return jsonify({'users':usuarios})

@app.route('/user/<numero>', methods=['GET'])
def pegar_usuario(numero):
    parsednumero = int(numero)
    return jsonify({'user': usuarios[parsednumero]})

@app.route('/usernovo',methods=['POST'])
def criar_usuario():
    novo_usuario = request.get_json()
    print(novo_usuario)
    return jsonify ({
        'user': novo_usuario,
        "message": "Usuario foi criado com sucesso!"})
    
if __name__ == '__main__':
    app.run(port=3000)