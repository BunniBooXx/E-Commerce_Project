from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


db=SQLAlchemy()


   
class User(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(45), nullable=False,unique=True )
    email=db.Column(db.String(100), nullable=False, unique=True)
    password=db.Column(db.String(100),nullable=False)

    date_created=db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    first_name= db.Column(db.String(45))
  

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password


class Clothes(db.Model): 
    id=db.Column(db.Integer,primary_key=True)
    product_name=db.Column(db.String(50), nullable = False)
    product_description= db.Column(db.String(200), nullable = False)
    product_price= db.Column(db.Numeric(8,2), nullable=False)
    product_size=db.Column(db.String(50))


class Sign_Up(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(50),nullable = False)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(100), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)
   
    
class Login(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(100), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)