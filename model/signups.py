""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json
from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''
class User(db.Model):
    __tablename__ = 'user'  
    _Active = db.Column(db.String(255), primary_key=True)
    _Exercise = db.Column(db.Integer, unique=False, nullable=False)
    
    def __init__(self, Username, Password):
        self._Active = Username   
        self._Exercise = Password
        
    @property
    def Username(self):
        return self._Username
    
    @Username.setter
    def Username(self, Username):
        self._Active = Username
    
    @property
    def Password(self):
        return self._Password
   
    @Password.setter
    def Password(self, Password):
        self._Password = Password
   
    def __str__(self):
        return json.dumps(self.read())
    
    def create(self):
        try:
            db.session.add(self)  
            db.session.commit()  
            return self
        except IntegrityError:
            db.session.remove()
            return None

    def read(self):
        return {
            "Username": self.Username,
            "Password": self.Password
        }

    def update(self, Username="", Password=0):
        """only updates values with length"""
        if len(Username) > 0:
            self.Username = Username
        if Password >= 0:
            self.Password = Password
        db.session.commit()
        return self
  
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
"""Database Creation and Testing """

def initUsers():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
       
        Users = []
        try:
            with open(r'users.json','r') as json_file:
                data = json.load(json_file)
        except Exception as error:
            print("failed")
        for item in data:
            # print(item)
            p_toadd = Users(Username=item['Username'], Password=item['Password'])
            Users.append(p_toadd)
        """Builds sample user/note(s) data"""
        for p in Users:
            try:
                p.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {p.Users}")