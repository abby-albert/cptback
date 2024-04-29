import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required

from model.signups import Username, Password

Signup_api = Blueprint('Signup_api', __name__,
                   url_prefix='/api/Signup')

api = Api(Signup_api)

class SignupAPI:        
    class _Log(Resource):
        @token_required
        def post(self, current_user): # Log food intake or exercise activity
            body = request.get_json()
            log_type = body.get('log_type')

            if log_type == 'Username':
                Username = body.get('Username')
                if not Username:
                    return {'message': 'Username missing'}, 400

                new_Username = Username(Username=Username, user_id=current_user.id)
                created_User = new_Username.create()

                if created_User:
                    return jsonify(created_User.serialize()), 201
                else:
                    return {'message': 'Failed to create user'}, 500

            elif log_type == 'Password':
                Password = body.get('Password')
                if not Password:
                    return {'message': 'Password is missing'}, 400

                Password = Password(Password=Password, user_id=current_user.id)
                created_User = Password.create()

                if created_User:
                    return jsonify(created_User.serialize()), 201
                else:
                    return {'message': 'Failed to Sign Up'}, 500

            else:
                return {'message': 'Invalid information'}, 400

        @token_required
        def get(self, current_user):  # Retrieve user's fitness log
            Usernames = Usernames.query.filter_by(user_id=current_user.id).all()
            Passwords = Passwords.query.filter_by(user_id=current_user.id).all()

            Username_logs = [Username_logs.serialize() for Username_logs in Username]
            Password_logs = [Password_logs.serialize() for Password_logs in Password]

            return jsonify({'Username': Username_logs, 'Password': Password_logs}), 200

    api.add_resource(_Log, '/log')