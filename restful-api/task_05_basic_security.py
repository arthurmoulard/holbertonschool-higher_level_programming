#!/usr/bin/python3
"""Simplified Flask API with Basic Auth and JWT"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import timedelta

app = Flask(__name__)

# --- JWT Configuration ---
app.config["JWT_SECRET_KEY"] = "super-secret-key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=5)

jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory token revocation list
revoked_tokens = set()

# --- Users (in-memory) ---
users = {
    "user1": {"password": generate_password_hash("password"), "role": "user"},
    "admin1": {"password": generate_password_hash("password"), "role": "admin"}
}

# --- Basic Auth ---
@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Auth"""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected with Basic Auth"""
    return "Basic Auth: Access Granted"

# --- JWT Login ---
@app.route("/login", methods=["POST"])
def login():
    """Authenticate user and return a JWT"""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]},
        fresh=True
    )
    return jsonify(access_token=access_token), 200

# --- JWT Protected Route ---
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protected with JWT"""
    return "JWT Auth: Access Granted"

# --- Admin-only decorator ---
def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        claims = get_jwt()
        if claims.get("role") != "admin":
            return jsonify({"error": "Admin access required"}), 403
        return fn(*args, **kwargs)
    return wrapper

@app.route("/admin-only")
@admin_required
def admin_only():
    """Admin-only route"""
    return "Admin Access: Granted"

# --- Logout (Token revocation) ---
@app.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """Revoke JWT"""
    jti = get_jwt()["jti"]
    revoked_tokens.add(jti)
    return jsonify({"message": "Token revoked"}), 200

# --- Fresh token example ---
@app.route("/fresh-protected")
@jwt_required(fresh=True)
def fresh_protected():
    """Route requiring a fresh JWT"""
    return "Fresh Token Access Granted"

# --- Token revocation check ---
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    """Check if the token has been revoked"""
    jti = jwt_payload["jti"]
    return jti in revoked_tokens

# --- Custom JWT error handlers ---
@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_fresh_token_required(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(debug=True)
    