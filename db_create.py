__author__ = 'lslacker'

from app import db
from app import models


#def add_users(username, password, nickname):

#    u = models.User(nickname=nickname,
#                    username=username,
#                    passwd=password)
#    db.session.add(u)

#    db.session.commit()


#if __name__ == '__main__':
    #db.drop_all()
    #db.create_all()
    #-- Luan Mai
    #add_users('test', '111111111111111111111111111111111111111111', 'Test User')
    #users = models.User.query.all()
    #for user in users:
    #    print user.username
    #    print user.check_password('abc123')

def add_jobs(jobname, created_by):

    v = models.Job(jobname=jobname,
                   created_by=created_by)
    db.session.add(v)

    db.session.commit()

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    add_jobs('super','1')
    jobs = models.Job.query.all()
    for jobs in jobs:
        print jobs.jobname

