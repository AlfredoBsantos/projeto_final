import requests

# Dados do usuário para criar
novo_usuario = {
    "name": "Professor Avaliador",
    "email": "nota10@faculdade.edu.br"
}

print("--- 1. Enviando pedido para o Service A (Usuários) ---")

try:
    # Manda os dados para o Service A
    response = requests.post("http://127.0.0.1:5001/users", json=novo_usuario)
    
    if response.status_code == 201:
        print("✅ SUCESSO! Service A respondeu: 201 Created")
        print(f"   Resposta: {response.json()}")
        print("\n--- 2. Verificando se o Service B recebeu o aviso ---")
        print("   AGORA: Olhe para o terminal onde o Service B está rodando.")
        print("   Você deve ver uma mensagem dizendo 'LOG REGISTRADO'.")
    else:
        print(f"❌ Erro no Service A: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"❌ ERRO: Não consegui conectar no Service A. Ele está rodando na porta 5001?")
    print(f"   Detalhe do erro: {e}")