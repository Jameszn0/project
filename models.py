from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Admin(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_username = db.Column(db.String(100))
    admin_pwd = db.Column(db.String(200))
    admin_loggedin = db.Column(db.DateTime, default=datetime.utcnow)


class User(db.Model):
    user_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_firstname=db.Column(db.String(255),nullable=False)
    user_lastname=db.Column(db.String(255),nullable=False)
    user_email=db.Column(db.String(255),nullable=False)
    user_pwd=db.Column(db.String(255),nullable=False)
    user_location=db.Column(db.String(255),nullable=False)

class Category(db.Model):
    cat_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    cat_name=db.Column(db.String(255),nullable=False)
    cat_description=db.Column(db.String(255),nullable=False)
    cat_picture=db.Column(db.String(255),nullable=False)

class Shoe(db.model):
    shoe_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    shoe_name=db.Column(db.String(255),nullable=False)
    shoe_brand=db.Column(db.String(255),nullable=False)
    shoe_releasedate=db.Column(db.String(255),nullable=False)
    shoe_price=db.Column(db.Float(),nullable=False)
    shoe_image=db.Column(db.String(255),nullable=False)
    shoe_description=db.Column(db.String(255),nullable=False)
    shoe_added_date=db.Column(db.String(255),nullable=False)
    shoe_brand_id=db.Column(db.Integer,primary_key=True,autoincrement=True)

    
class Order(db.model):
    order_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id=db.Column(db.Integer,primary_key=True,autoincrement=True)