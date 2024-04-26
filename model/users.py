# database dependencies to support sqliteDB examples
from random import randrange
from datetime import date
import os
import base64
import json

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

# Import the Flask app instance and SQLAlchemy db instance from __init__.py
from __init__ import app, db

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

def initUsers():
    # Sample user data
    users_data = [
        {'name': 'Scottie Sheffler', 'uid': 'scottie', 'pasword': '123scottie'},
        {'name': 'Nelly Korda', 'uid': 'nelly', 'password': '123nelly'},
        {'name': 'Tiger Woods', 'uid': 'tiger', 'password': '123tiger'},
        {'name': 'Justin Thomas', 'uid': 'jt', 'password': '123jt'} 
       ]

    # Add sample users to the database
    for user_data in users_data:
        name = user_data['name']
        uid = user_data['uid']
        password = user_data['password']

        # Check if username already exists
        existing_user = User.query.filter_by(uid=uid).first()
        if not existing_user:
            # Create new user
            new_user = User(name=name, uid=uid, password=password)
            db.session.add(new_user)
            db.session.commit()

# API route for user signup
@app.route('/api/users', methods=['POST'])
def signup():
    # Get data from request
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if username already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    # Create new user
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
