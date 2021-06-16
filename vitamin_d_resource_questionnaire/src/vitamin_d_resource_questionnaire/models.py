"""Database models"""

from flask_mongoengine import mongoengine as me

MOBILITY = ('I have no problems in walking about',
            'I have some problems in walking about',
            'I am confined to bed')
SELFCARE = ('I have no problems with self-care',
            'I have some problems washing or dressing myself',
            'I am unable to wash or dress myself')
USUALACTIVITIES = ('I have no problems with performing my usual activities',
                   'I have some problems with performing my usual activities',
                   'I am unable to perform my usual activities')
PAINDISCOMFORT = ('I have no pain or discomfort',
                  'I have moderate pain or discomfort',
                  'I have extreme pain or discomfort')
ANXIETYDEPRESSION= ('I am not anxious or depressed',
                    'I am moderately anxious or depressed',
                    'I am extremely anxious or depressed')


class Questionnaire(me.Document):
    username = me.EmailField()
    date = me.DateField()
    mobility = me.StringField(choices=MOBILITY)
    selfCare = me.StringField(choices=SELFCARE)
    usualActivities = me.StringField(choices=USUALACTIVITIES)
    painOrDiscomfort = me.StringField(choices=PAINDISCOMFORT)
    anxietyDepression = me.StringField(choices=ANXIETYDEPRESSION)
    todaysHealth = me.IntField(min_value=0, max_value=100)
