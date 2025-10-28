"""
Serviço de Autenticação - Sistema de Cinema
Autor: Cauã Costa
Data: 28/10/2025
"""

import json
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin):
    """Classe de usuário para Flask-Login"""
    
    def __init__(self, id, username, email, password_hash, role='user', created_at=None):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.created_at = created_at or datetime.now().strftime("%d/%m/%Y %H:%M")
    
    def check_password(self, password):
        """Verifica se a senha está correta"""
        return check_password_hash(self.password_hash, password)
    
    def is_admin(self):
        """Verifica se o usuário é administrador"""
        return self.role == 'admin'
    
    def to_dict(self):
        """Converte usuário para dicionário"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
            'role': self.role,
            'created_at': self.created_at
        }


class AuthService:
    """Serviço de gerenciamento de autenticação"""
    
    def __init__(self, arquivo_usuarios='dados/usuarios.json'):
        self.arquivo_usuarios = arquivo_usuarios
        self._garantir_arquivo_existe()
        self._criar_admin_padrao()
    
    def _garantir_arquivo_existe(self):
        """Garante que o arquivo de usuários existe"""
        os.makedirs('dados', exist_ok=True)
        if not os.path.exists(self.arquivo_usuarios):
            with open(self.arquivo_usuarios, 'w', encoding='utf-8') as f:
                json.dump({}, f, indent=2, ensure_ascii=False)
    
    def _criar_admin_padrao(self):
        """Cria usuário admin padrão se não existir"""
        usuarios = self._carregar_usuarios()
        tem_admin = any(u.get('role') == 'admin' for u in usuarios.values())
        
        if not tem_admin:
            admin = {
                'id': '1',
                'username': 'admin',
                'email': 'admin@cinema.com',
                'password_hash': generate_password_hash('admin123'),
                'role': 'admin',
                'created_at': datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            usuarios['1'] = admin
            self._salvar_usuarios(usuarios)
            print("✅ Usuário admin padrão criado (username: admin, senha: admin123)")
    
    def _carregar_usuarios(self):
        """Carrega usuários do arquivo JSON"""
        try:
            with open(self.arquivo_usuarios, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def _salvar_usuarios(self, usuarios):
        """Salva usuários no arquivo JSON"""
        with open(self.arquivo_usuarios, 'w', encoding='utf-8') as f:
            json.dump(usuarios, f, indent=2, ensure_ascii=False)
    
    def _gerar_novo_id(self, usuarios):
        """Gera um novo ID único para usuário"""
        if not usuarios:
            return '1'
        ids = [int(uid) for uid in usuarios.keys() if uid.isdigit()]
        return str(max(ids) + 1) if ids else '1'
    
    def registrar_usuario(self, username, email, password, role='user'):
        """Registra um novo usuário"""
        usuarios = self._carregar_usuarios()
        
        if len(username) < 3:
            return False, "Nome de usuário deve ter pelo menos 3 caracteres", None
        if len(password) < 6:
            return False, "Senha deve ter pelo menos 6 caracteres", None
        if '@' not in email or '.' not in email:
            return False, "Email inválido", None
        
        for user_data in usuarios.values():
            if user_data['username'].lower() == username.lower():
                return False, "Nome de usuário já existe", None
            if user_data['email'].lower() == email.lower():
                return False, "Email já cadastrado", None
        
        novo_id = self._gerar_novo_id(usuarios)
        password_hash = generate_password_hash(password)
        novo_usuario = User(id=novo_id, username=username, email=email, password_hash=password_hash, role=role)
        usuarios[novo_id] = novo_usuario.to_dict()
        self._salvar_usuarios(usuarios)
        
        return True, "Usuário registrado com sucesso!", novo_usuario
    
    def autenticar_usuario(self, username, password):
        """Autentica um usuário"""
        usuarios = self._carregar_usuarios()
        usuario_data = None
        
        for user_data in usuarios.values():
            if (user_data['username'].lower() == username.lower() or user_data['email'].lower() == username.lower()):
                usuario_data = user_data
                break
        
        if not usuario_data:
            return False, "Usuário não encontrado", None
        if not check_password_hash(usuario_data['password_hash'], password):
            return False, "Senha incorreta", None
        
        user = User(id=usuario_data['id'], username=usuario_data['username'], email=usuario_data['email'],
                   password_hash=usuario_data['password_hash'], role=usuario_data['role'],
                   created_at=usuario_data.get('created_at'))
        return True, "Login realizado com sucesso!", user
    
    def buscar_usuario_por_id(self, user_id):
        """Busca usuário por ID"""
        usuarios = self._carregar_usuarios()
        usuario_data = usuarios.get(str(user_id))
        if not usuario_data:
            return None
        return User(id=usuario_data['id'], username=usuario_data['username'], email=usuario_data['email'],
                   password_hash=usuario_data['password_hash'], role=usuario_data['role'],
                   created_at=usuario_data.get('created_at'))
    
    def listar_usuarios(self):
        """Lista todos os usuários"""
        usuarios = self._carregar_usuarios()
        return [User(id=u['id'], username=u['username'], email=u['email'], password_hash=u['password_hash'],
                    role=u['role'], created_at=u.get('created_at')) for u in usuarios.values()]