"""Database models"""

from flask_mongoengine import mongoengine as me

ACTIVITEITEN = ('rennen', 'lopen', 'fietsen', 'zwemmen')


class Schedule(me.Document):
    """Schedule model"""
    username = me.EmailField()
    date = me.DateField()
    distance = me.IntField()
    # 'rennen', 'lopen', 'fietsen', 'zwemmen'
    activity_type = me.StringField(choices=ACTIVITEITEN)
