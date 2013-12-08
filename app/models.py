__author__ = 'lslacker'
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


class User(db.Model):
    __tablename__ = 'user_auth'

    id = db.Column(db.Integer, primary_key=True)
    #id = db.relationship('tasks', backref='user_auth', lazy='dynamic')
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

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


class Job(db.Model):
    """
    Jobs Table
    """
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    jobname = db.Column(db.String(100))
    created_by = db.Column(db.Integer())
    created_on = db.Column(db.DateTime, default=datetime.datetime.now)

class JobsLock(db.Model):
    """
    Jobs Lock Table
    """
    __tablename__ = 'jobs_lock'

    id = db.Column(db.Integer, primary_key=True)
    jobid = db.Column(db.Integer())
    userid = db.Column(db.Integer())
    jobs_lodged_by = db.Column(db.DateTime, default=datetime.datetime.now)
    status = db.Column(db.VARCHAR(5))


class Tasks(db.Model):
    """
    Tasks Table
    """
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    jobid = db.Column(db.Integer(), db.ForeignKey('jobs.id'))
    job = db.relationship('Job', backref=db.backref('jobs', lazy='dynamic'))
    canonical_order = db.Column(db.Integer())
    task_type = db.Column(db.VARCHAR(50))
    task_name = db.Column(db.VARCHAR())
    created_by = db.Column(db.Integer(), db.ForeignKey('user_auth.id'))
    user = db.relationship('User', backref=db.backref('tasks', lazy='dynamic'))
    created_on = db.Column(db.DateTime, default=datetime.datetime.now)
    last_modify = db.Column(db.DateTime, default=datetime.datetime.now)
    status = db.Column(db.VARCHAR(20), default='Initial')
    when_start = db.Column(db.DateTime())
    duration = db.Column(db.Integer())
    error = db.Column(db.Text)
    continue_on_error = db.Column(db.Integer, default=0)

