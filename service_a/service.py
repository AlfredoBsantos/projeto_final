import requests
from repository import UserRepository

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, name, email):
        # 1. Regra de negócio: Salva no banco local
        user_id = self.repository.save(name, email)
        
        # 2. Comunicação Síncrona: Avisa o Service B (Log Service)
        try:
            requests.post('http://localhost:5002/logs', json={
                'event': 'User Created',
                'details': f'User {name} created with ID {user_id}'
            })
        except:
            print("Erro ao comunicar com Service B")
            
        return user_id