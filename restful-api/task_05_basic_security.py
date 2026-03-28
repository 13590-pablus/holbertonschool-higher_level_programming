#!/usr/bin/python3
"""
Flask ile Basic Auth ve JWT Güvenlik Modülü.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)

app = Flask(__name__)
# JWT için gizli anahtar (Zorunludur)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Bellekte kullanıcı verileri (Hashed Passwords)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Basic Authentication ---

@auth.verify_password
def verify_password(username, password):
    """Basic Auth şifre doğrulama."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Basic Auth korumalı rota."""
    return "Basic Auth: Access Granted"

# --- JWT Authentication ---

@app.route('/login', methods=['POST'])
def login():
    """Giriş yap ve JWT üret."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
        
    username = data.get('username')
    password = data.get('password')
    
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Rolü token içine claims olarak ekliyoruz
        access_token = create_access_token(
            identity=username, 
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT korumalı rota."""
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Sadece admin rolü erişebilir (RBAC)."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# --- JWT Hata İşleyiciler (401 Dönmesi Önemli) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

if __name__ == "__main__":
    app.run()
