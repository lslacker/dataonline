__author__ = 'lslacker'
import os

CSRF_ENABLED = True

SECRET_KEY = os.urandom(24)

basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'postgresql://joboperators:abc123@localhost:5432/jobs'

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joboperators:abc123@localhost:5432/jobs'