from flask import Flask, request, jsonify
from service import UserService

app = Flask(__name__)
user_service = UserService()

# --- NOVA ROTA: Para testar no navegador sem dar erro 404 ---
@app.route('/', methods=['GET'])
def home():
    return "<h1>Service A (Usuários) Online! 🚀</h1><p>O servidor está rodando. Para cadastrar, envie um POST para <b>/users</b>.</p>", 200

# --- ROTA PRINCIPAL: Onde acontece o cadastro ---
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    # Aplicação do SOLID (SRP): O controller apenas repassa, não processa
    user_id = user_service.create_user(data['name'], data['email'])
    return jsonify({"message": "User created", "id": user_id}), 201

if __name__ == '__main__':
    app.run(port=5001, debug=True)