import os
from base64 import b64encode
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ta_adoption.settings import database

# Where am I ?
basedir = os.path.abspath(os.path.dirname(__file__))
print ("**************************")
print('In __init__.py Name: ', __name__)
print(' In __init__.py File: ', __file__)
print ("**************************")

#Create the Flask App Object
application =  app = Flask(__name__)

#Assign App Config Variables
token = os.urandom(64)
token = b64encode(token).decode('utf-8')
app.config['SECRET_KEY']= token
app.config['DEBUG'] = False # Enable/Disable debug toolbar
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False # allow page redirects without intercept
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Various MySql Connectors

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:YOUR_PASSWORD@aa1ho1ni9nfz56e.cp1kaaiuayns.us-east-1.rds.amazonaws.com/cust_ref_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:YOUR_PASSWORD@aay9qgi0q2ps45.cp1kaaiuayns.us-east-1.rds.amazonaws.com/cust_ref_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:passwords["DB_PASSWORD"]@localhost/cust_ref_db'
#application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'jimsDB.db')

#Remote connect to RaspPi (Stan)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:YOUR_PASSWORD@overlook-mountain.com:12498/cust_ref_db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:passwords["DB_PASSWORD"]@stan/cust_ref_db'

# Create db for SQL Alchemy
db = SQLAlchemy(app)

# import the models and views
from ta_adoption import models
from ta_adoption import views

# Another "better" way to import
# from .models import *
# from .views import *


