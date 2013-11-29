__author__ = 'lslacker'

from app import db
from app import models


def add_users(username, password, nickname):

    u = models.User(nickname=nickname,
                    username=username,
                    passwd=password)
    db.session.add(u)

    db.session.commit()


if __name__ == '__main__':
    #db.drop_all()
    #db.create_all()
    #-- Luan Mai
    add_users('luan', 'abc123', 'Luan Mai')
    users = models.User.query.all()
    for user in users:
        print user.check_password('abc123')