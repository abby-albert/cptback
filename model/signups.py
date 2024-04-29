from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    uid = data.get('uid')
    password = data.get('password')

    if not uid or not password:
        return jsonify({'message': 'uid and password are required'}), 400

    if User.query.filter_by(uid=uid).first():
        return jsonify({'message': 'uid already exists'}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(uid=uid, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
