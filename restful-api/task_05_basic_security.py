#!/usr/bin/python3
"""Simple API with Basic and JWT Authentication"""
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'  # Secret key for JWT
jwt = JWTManager(app)

# Simple in-memory user storage
users = {
    "user1": {"password": generate_password_hash("password"), "role": "user"},
    "admin1": {"password": generate_password_hash("password"), "role": "admin"}
}

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint: returns JWT token if credentials are correct"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        token = create_access_token(identity={'username': username, 'role': user['role']})
        return jsonify(access_token=token)
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/protected')
@jwt_required()
def protected():
    """Protected route: requires a valid JWT"""
    user = get_jwt_identity()
    return jsonify({"message": f"Hello {user['username']}, access granted!"})

@app.route('/admin')
@jwt_required()
def admin():
    """Admin-only route"""
    user = get_jwt_identity()
    if user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin access granted"})

if __name__ == "__main__":
    app.run(debug=True)
    