from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

from app.models.admin import Admin

AUTH_BP = Blueprint('auth_bp', __name__, url_prefix='/auth')


@AUTH_BP.route('/login', methods=['POST'])
def login():
    password = request.json.get('password', None)

    if not password:
        return jsonify({'msg': 'Missing password parameter'}), 400
    
    admin = Admin.objects.get(name="admin")
    if !check_password_hash(admin.password_hash, password):
        return jsonify({'msg': 'Invalid password'}), 401

    access_token = create_access_token(identity="admin")
    return jsonify(access_token=access_token), 200