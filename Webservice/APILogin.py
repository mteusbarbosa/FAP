from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    login = data.get('login')
    senha = data.get('senha')

    if login == 'teste' and senha == '123456':
        return jsonify(
            {'msgRetorno': 'Login realizado com sucesso', 
             'logado': True, 
             'linkDownload': "https://localhost:8000/"
             })
    else:
        return jsonify({'msgRetorno': 'Usuário ou senha não confere.', 'logado': False, 'versionApp': '', 'linkDownload': ''})

if __name__ == '__main__':
    app.run(debug=True)