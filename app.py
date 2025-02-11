from flask import Flask, request, jsonify

app = Flask (__name__)

@app.route('/test', methods =['GET'])
def test():
    return jsonify({'message': 'Ola mundo'})

@app.route('/usuario/novo', methods =['POST'])
def criar_novo_usuario():
    novo_usuario = request.json
    print(novo_usuario)
    return jsonify({
        'user': novo_usuario,
        'message': 'Usuario criado com sucesso!'
        })
    
if __name__ =='__main__':
    app.run(port=5000)