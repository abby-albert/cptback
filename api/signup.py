import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required

from model.signups import Username, Password

signup_api = Blueprint('signup_api', __name__,
                   url_prefix='/api/signup')

api = Api(signup_api)

class signupAPI:        
    class _Log(Resource):
        @token_required
        def post(self, current_user): # Log food intake or exercise activity
            body = request.get_json()
            log_type = body.get('log_type')

            if log_type == 'Username':
                Username = body.get('Username')
                if not Username:
                    return {'message': 'username is missing'}, 400

                new_Username = Username(Username=Username, user_id=current_user.id)
                created_Username = new_Username.create()

                if created_Username:
                    return jsonify(created_Username.serialize()), 201
                else:
                    return {'message': 'Failed to signin'}, 500

            elif log_type == 'Password':
                Password = body.get('Password')
                if not Password:
                    return {'message': 'Password missing'}, 400

                new_Password = Password(Password=Password, user_id=current_user.id)
                created_Password = new_Password.create()

                if created_Password:
                    return jsonify(created_Password.serialize()), 201
                else:
                    return {'message': 'Failed to sign up'}, 500

            else:
                return {'message': 'Invalid user type'}, 400

        @token_required
        def get(self, current_user):  # Retrieve user's fitness log
            Username = Username.query.filter_by(user_id=current_user.id).all()
            Password = Password.query.filter_by(user_id=current_user.id).all()

            Username_logs = [Username.serialize() for food in Username]
            Password_logs = [Password.serialize() for exercise in Password]

            return jsonify({'Username': Username_logs, 'Password': Password_logs}), 200

    api.add_resource(_Log, '/log')