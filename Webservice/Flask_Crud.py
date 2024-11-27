# Importações necessárias
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Configuração do aplicativo Flask
app = Flask(__name__)

# Configurações do banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do SQLAlchemy
db = SQLAlchemy(app)

# Definição do modelo de dados
class User(db.Model):
    """
    Modelo de usuário para demonstração de CRUD
    Pode ser facilmente modificado para atender necessidades específicas
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer)

    def to_dict(self):
        """
        Converte o objeto User para um dicionário
        Útil para serialização de JSON
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age
        }

# Rota para criar tabelas (usado apenas uma vez)
@app.route('/create_tables', methods=['GET'])
def create_tables():
    """
    Rota para criar todas as tabelas do banco de dados
    Deve ser chamada apenas uma vez na configuração inicial
    """
    with app.app_context():
        db.create_all()
    return jsonify({"message": "Tabelas criadas com sucesso!"})

# Rotas CRUD para User
@app.route('/users', methods=['POST'])
def create_user():
    """
    Cria um novo usuário
    Método: POST
    """
    data = request.json
    new_user = User(
        name=data['name'], 
        email=data['email'], 
        age=data.get('age')
    )
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email já existe"}), 400

@app.route('/users', methods=['GET'])
def get_users():
    """
    Recupera todos os usuários
    Método: GET
    """
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Recupera um usuário específico por ID
    Método: GET
    """
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Atualiza um usuário existente
    Método: PUT
    """
    user = User.query.get_or_404(user_id)
    data = request.json

    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.age = data.get('age', user.age)

    try:
        db.session.commit()
        return jsonify(user.to_dict())
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Erro ao atualizar usuário"}), 400

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Deleta um usuário
    Método: DELETE
    """
    user = User.query.get_or_404(user_id)
    
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Usuário deletado com sucesso"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Tratamento de erros
@app.errorhandler(404)
def not_found(error):
    """
    Tratamento padrão para erro 404 (Não encontrado)
    """
    return jsonify({"error": "Recurso não encontrado"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Tratamento padrão para erro 500 (Erro interno do servidor)
    """
    return jsonify({"error": "Erro interno do servidor"}), 500

# Configurações para executar o aplicativo
if __name__ == '__main__':
    # Contexto do aplicativo para criação de tabelas
    with app.app_context():
        db.create_all()
    
    # Modo de depuração para desenvolvimento
    app.run(debug=True)