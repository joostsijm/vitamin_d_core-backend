"""Database models"""

from flask_mongoengine import mongoengine as me


class Session(me.EmbeddedDocument):
    code = me.StringField()


class Administrator(me.Document):
    username = me.EmailField()
    password = me.StringField()


class User(me.Document):
    username = me.EmailField()
    password = me.StringField()
