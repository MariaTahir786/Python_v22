from app.config.mysqlconnection import connectToMySQL
from app import app
from flask_bcrypt import Bcrypt
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    dB = 'registeration_db_cls'
    
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email_address=data['email_address']
        self.password=data['password']
        
    #!create
    @classmethod
    def register_user(cls,data):
        bcrypt =Bcrypt(app)
        query="""
            INSERT INTO users
            (first_name, last_name, email_address,password) 
            VALUES 
            (%(first_name)s, %(last_name)s,%(email_address)s,%(password)s)
        """
        #before adding  bcrypt for password encryption
        #return connectToMySQL(cls.dB).query_db(query,data)
        return connectToMySQL(cls.dB).query_db(query,{
            **data,#this is spread operator which creates the copy of object data
            "password":bcrypt.generate_password_hash(data['password'])
        })
    
        
    @classmethod
    def get_by_email(cls,email_address):
        query ="""
                select *
                from users
                where email_address=%(email_address)s
        
        """
        
        results =connectToMySQL(cls.dB).query_db(query,{'email_address':email_address})
        
        #checking to make sure something was loaded
        if not results:
            return None
        return cls(results[0])
    
    
    @staticmethod
    def validate_registration(registration_form):
        #is called blacklisting
        is_valid=True
        #? check if user exits or not in db
        if User.get_by_email(registration_form['email_address']):
            is_valid=False
            flash("Email already exists","registration")
        if len(registration_form['first_name'])<3:
            is_valid=False
            flash("First name must be 3 chars long","registration")
            
        if len(registration_form['last_name'])<3:
            is_valid=False
            flash("FLast name must be 3 chars long","registration")
            
        #? check password length
        if len(registration_form['password'])<8:
            is_valid=False
            flash("password must be 8 characters long","registration")
            
        #?check password and confirm pas match
        if registration_form['password']!= registration_form['confirm_password']:
            is_valid=False
            flash("password must be matching","registration")
        #?to check email is not empty  
        if len(registration_form['email_address'])==0:
            is_valid=False
            flash("email is required","registration")
            
            
            
        if not EMAIL_REGEX.match(registration_form['email_address']):
            is_valid=False
            flash("Invalid email","registration")
            
        if is_valid:
            flash("Thanks for registering",'registration')
        return is_valid