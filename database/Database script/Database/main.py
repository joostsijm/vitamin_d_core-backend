# to run the app type:
# set FLASK_APP=main.py
# flask run
# in the terminal


from flask import Flask
from flask_mongoengine import MongoEngine
from DatabaseClasses import *


class Config(object):
    MONGODB_SETTINGS = {'db': 'IoTVitamineD'}


db = MongoEngine()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/')
def home():
    user = User(geslacht="M")
    user.naamgegevens = NaamgegevensUser(voornamen="jesse", initialen="J.R",
                                         roepnaam="jj")
    user.naamgegevens.adressgegevens = AdressgegevensUser(straat="van Heuven Goedhartlaan",
                                                          huisnummer=152, huisnummerletter=" ", huisnummerToevoeging=" ",
                                                          aanduidingBijNummer=" ", woonplaats="Amstelveen",
                                                          gemeente="Amstelveen",
                                                          land="NL", postcode="1181LL", aditioneleInformatie=" ",
                                                          adressSoort='PST')
    user.naamgegevens.geslachtsnaam = GeslachtsnaamUser(voorvoegsels=" ", achternaam="jones")
    user.naamgegevens.contactgegevens = ContactgegevensUser()
    user.naamgegevens.contactgegevens.telefoonnummer = TelefoonnummersUser(telefoonnummer=31615651877,
                                                                           toelichting=" ",
                                                                           telecomType="LL",
                                                                           nummerSoort="HP")
    user.naamgegevens.contactgegevens.emailAdressen = EmailAdressenUser(emailAdres="jesse.r.jones@test.nl",
                                                                        emailSoort="HP")
    user.save()
    return "send"

# @app.route('/add')
# def home():
#
#     return "added"

