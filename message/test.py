# -*- coding:utf-8 -*-
from flask import Flask,redirect,request,render_template
from wtforms import Form,TextField,PasswordField,validators
# from db import *
from model import *

class LoginForm(Form):
    username=TextField("username",[validators.DataRequired()])
    password=PasswordField("password",[validators.DataRequired()])
class PublishForm(Form):
    content=TextField("content",[validators.DataRequired()])
    sender=TextField("sender",[validators.DataRequired()])


@app.route('/')
def user_mgmt():
    return render_template('mgmt.html')
@app.route("/login",methods=['GET','POST'])
def login():
    myForm=LoginForm(request.form)
    if request.method=='POST':
        u=User(myForm.username.data,myForm.password.data)
        if (u.isExisted()):
            return redirect("http://127.0.0.1:8080/show")
        else:
            message="Login Failed"
            return render_template('index.html',message=message,form=myForm,key='Login')
    return render_template('index.html',form=myForm,key='Login')
@app.route("/register",methods=['GET','POST'])
def register():
    myForm=LoginForm(request.form)
    if request.method=='POST':
        u = User(myForm.username.data, myForm.password.data)
        if (u.isExisted()):
            message="User Exists"
            return render_template('index.html', message=message, form=myForm, key='Register')
        else:
            u.add()
            return "Register Successfully"
    return render_template("index.html",form=myForm,key='Register')

@app.route('/search',methods=['GET','POST'])
def search():
    if request.method=='POST':
        uname=request.form['username']
        if User.query.filter_by(username=uname).first() is None:
            message='User is not Existed'
            return render_template("search.html",message=message)
        else:
            u = User.query.filter_by(username=uname).first()
            l=[]
            l=Entry.query.filter_by(sender_id=u.id).all()
            return render_template('search.html',contents=l)
    return render_template('search.html')

@app.route('/show',methods=['GET','POST'])
def show():
    myEntryForm=PublishForm(request.form)
    l=getAllEntry()
    if request.method=='POST':
        uname = request.form['sender']
        if User.query.filter_by(username=uname).first() is None:
            message='User is not Existed'
            return render_template("show.html",message=message,form=myEntryForm)
        else:
            u=User.query.filter_by(username=uname).first()
            e=Entry(myEntryForm.content.data,u.id)
            e.add()
            return render_template("show.html",entries=l,form=myEntryForm)
    return render_template("show.html",entries=l,form=myEntryForm)

if __name__ == '__main__':
    app.run()
