from flask import Flask
from flask_mongoengine import MongoEngine
# from flask_mongoengine import mongoengine as me
from DatabaseClasses import *


class Config(object):
    MONGODB_SETTINGS = {'db':'IoTVitamineD'}


app = Flask(__name__)
app.config.from_object(Config)

db=MongoEngine()
db.init_app(app)





@app.route('/test')
def home():

    user = User(geslacht="M")
    user.save()


    return "test"