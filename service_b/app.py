from flask import Flask, request, jsonify
from service import LogService

app = Flask(__name__)
log_service = LogService()

# --- NOVA ROTA: Para testar no navegador sem dar erro 404 ---
@app.route('/', methods=['GET'])
def home():
    return "<h1>Service B (Logs) Online! 📋</h1><p>O servidor está escutando na porta 5002. Aguardando logs do Service A...</p>", 200

# --- ROTA PRINCIPAL: Onde recebe os logs ---
@app.route('/logs', methods=['POST'])
def create_log():
    data = request.json
    log_service.register_log(data['event'], data['details'])
    return jsonify({"status": "Log saved"}), 201

if __name__ == '__main__':
    # Roda na porta 5002 para não conflitar
    app.run(port=5002, debug=True)