#!/usr/bin/env python3
"""Develop a Simple API using Python with Flask"""

from flask import Flask
from flask import jsonify
from flask import request

# Create the Flask application instance
app = Flask(__name__)

# In-memory dictionary to store users
users = {}


@app.route('/')
def home():
    """Root endpoint returning a welcome message"""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """Return the list of registered usernames"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Health check endpoint"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Retrieve a specific user by username.
    Returns 404 if the user does not exist.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user via POST request.
    Expects JSON body with at least a 'username' field.
    """

    # Parse incoming JSON data
    data = request.get_json()

    # Validate required field
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Prevent duplicate usernames
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store user data in memory
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    # Return success response with HTTP 201 (Created)
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


# Run the Flask development server
if __name__ == "__main__":
    app.run()