from app import app
from flask import Flask, render_template, redirect, request,flash
from flask_bcrypt import Bcrypt

from app.models.user_model import User

bcrypt =Bcrypt(app)

@app.route('/user')
def user_home():
    return render_template('/user/user_home.html')

@app.route('/user/register',methods=['POST'])
def register_user():
    form=request.form
    data={
        "first_name":form['first_name'],
        "last_name":form['last_name'],
        "email_address":form['email_address'],
        "password":form['password'],
    }
    
    if User.validate_registration(form):
        User.register_user(data)
        return redirect('/user')
    
    return redirect('/user')
@app.route('/user/login',methods=['POST'])
def login():
    form=request.form
    
    user= User.get_by_email(form.get('email_address'))# OR form['email_address]
    
    if user is None or bcrypt.check_password_hash(user.password,request.form['password'])==False:
        #this is for if user put wrong email and it will give error message
        flash("Invalid message","login")
        return redirect('/user')
    
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('/user/dashboard.html')
    
    