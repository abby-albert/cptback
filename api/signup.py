import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource 
from datetime import datetime
from auth_middleware import token_required
from model.signups import User
signup_api = Blueprint('signup_api', __name__,
                   url_prefix='/api/signup')

api = Api(signup_api)
class SignupAPI:
    class _CRUD(Resource):  
        def post(self): 
            ''' Read data for json body '''
            body = request.get_json()
            ''' Avoid garbage in, error checking '''
        
            Username = body.get('Username')
            if Username is None or len(Username) < 2:
                return {'message': f'Username is missing, or is less than 2 characters'}, 400
          
            Password = body.get('Password')
            if Password is None or Password < 0 :
                return {'message': f'Password has to be positive number'}, 400
            ''' #1: Key code block, setup USER OBJECT '''
            newUser = User(Username=Username,
                      Password=Password)
            ''' #2: Key Code block to add user to database '''
            just_added_user = newUser.create()
            if just_added_user:
                return jsonify(just_added_user.read())
         
            return {'message': f'Processed {Username}, either a format error or it is duplicate'}, 400
        def get(self):
            users = users.query.all()    
            json_ready = [user.read() for user in users]  
            return jsonify(json_ready)  
        def delete(self):  
            ''' Find user by ID '''
            body = request.get_json()
            del_user = body.get('Username')
            result = User.query.filter(User._Active == del_user).first()
            if result is None:
                 return {'message': f'pulse {del_user} not found'}, 404
            else:
                result.delete()
                print("delete")
    class _get(Resource):
        def get(self, lname=None):  
            print(lname)
            if lname:
                result = User.query.filter_by(_Userame=lname).first()
                print(result)
                if result:
                    print(result)
                    return jsonify([result.read()])  # Assuming you have a read() method in your PulseyApi model
                else:
                    return jsonify({"message": "User not found"}), 404

    api.add_resource(_CRUD, '/')
    api.add_resource(_get, '/<string:lname>')