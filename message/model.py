# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:charles2009@127.0.0.1/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(32),unique=True)
    password = db.Column(db.String(32))
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception,e:
            db.session.rollback()
            return e
        finally:
            return 0

    def isExisted(self):
        temUser=User.query.filter_by(username=self.username,password=self.password).first()
        if temUser is None:
            return False
        else:
            return True
class Entry(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content=db.Column(db.Text)
    sender_id=db.Column(db.Integer)
    def __init__(self,content,sender_id):
        self.content=content
        self.sender_id=sender_id
    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception,e:
            db.session.rollback()
            return e
        finally:
            return 0
def getAllEntry():
    mlist = []
    Entlist=[]
    mlist = Entry.query.filter_by().all()
    for message in mlist:
        u = User.query.filter_by(id=message.sender_id).first()
        tmp={'content':message.content,'sender':u.username}
        Entlist.append(tmp)
    return Entlist

db.create_all()




