from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)
api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class UserSignup(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uid', type=str, required=True, help='uid is required')
        parser.add_argument('password', type=str, required=True, help='Password is required')
        args = parser.parse_args()

        uid = args['uid']
        password = args['password']

        if User.query.filter_by(uid=uid).first():
            return {'message': 'uid already exists'}, 409

        hashed_password = generate_password_hash(password)
        new_user = User(uid=uid, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User created successfully'}, 201

api.add_resource(UserSignup, '/signup')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
