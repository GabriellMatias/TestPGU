from flask import Blueprint, jsonify
from app.models import User
from .database import db

from uuid import uuid4

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def list_users():
    try:
        users = User.query.all()
    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro no banco de dados {e}'}), 500
    
    users_json = [{'id': user.id, 'nome': user.nome} for user in users]
    
    return jsonify(users_json), 200

@users_bp.route('/gerar_usuarios', methods=['POST'])
def gerar_usuarios():

    #Utilizando blocos de tentativa sempre quando houver busca ou insercao no DB
    try:
        for i in range(10):
            user = User(str(uuid4()), f'User Numero {i+1}')
            db.session.add(user)
        db.session.commit()
    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro no banco de dados {e}'}), 500
    
    return jsonify({"message": "Usuarios criados com sucesso!."}), 200
