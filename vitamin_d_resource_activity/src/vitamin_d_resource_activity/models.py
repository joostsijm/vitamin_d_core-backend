"""Database models"""

from flask_mongoengine import mongoengine as me

ACTIVITEITEN = ('rennen', 'lopen', 'fietsen', 'zwemmen')


class Activity(me.Document):
    """Activity model"""
    username = me.EmailField()
    date = me.DateField()
    distance = me.IntField()
    # 'rennen', 'lopen', 'fietsen', 'zwemmen'
    activiteit_type = me.StringField(choices=ACTIVITEITEN)
