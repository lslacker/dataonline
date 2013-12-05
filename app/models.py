__author__ = 'lslacker'
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'user_auth'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    passwd = db.Column(db.String(100))
    nickname = db.Column(db.String(50))

    def __init__(self, username, passwd, nickname):
        self.username = username.lower()
        self.nickname = nickname.lower()
        self.set_password(passwd)

    def set_password(self, password):
        self.passwd = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwd, password)

class Gary(db.Model):
    __tablename__ = 'gary'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
