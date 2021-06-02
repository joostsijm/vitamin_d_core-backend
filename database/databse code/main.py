# to run the app type:
# set FLASK_APP=main.py
# flask run
# in the terminal


from flask import Flask, request, redirect, url_for, jsonify
from flask_mongoengine import MongoEngine
from DatabaseClasses import *



class Config(object):
    MONGODB_SETTINGS = {'db': 'IoTVitamineD'}


db = MongoEngine()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/n')
def home():
    return "hallo"


@app.route('/sendAdministrator/<geslacht>/<specialisme>/<voornaam>/<achternaam>/<username>/<password>/<geboortedatum>')
def sendAdministrator(geslacht, specialisme, voornaam, achternaam, username, password, geboortedatum):
    administrator = Administrator(geslacht=geslacht, geboortedatum=geboortedatum, specialisme=specialisme)
    administrator.naamgegevens = NaamgegevensUser(voornamen=voornaam)
    administrator.naamgegevens.geslachtsnaam = GeslachtsnaamUser(achternaam=achternaam)
    administrator.naamgegevens.contactgegevens = ContactgegevensUser()
    administrator.naamgegevens.contactgegevens.emailAdressen = EmailAdressenUser(emailAdres=username)
    administrator.save()
    login = Login(username=username, password=password)
    login.save()
    return


@app.route('/sendUser/<geslacht>/<voornaam>/<achternaam>/<username>/<password>/<geboortedatum>/<lengte>/<lengtedatum>/'
           '<lengtepositie>/<gewicht>/<gewichtdatum>/<gewichtpositie>')
def sendName(geslacht, voornaam, achternaam, username, password, geboortedatum, lengte, lengtedatum, lengtepositie,
             gewicht, gewichtdatum, gewichtpositie):
    user = User(geslacht=geslacht, geboortedatum=geboortedatum)
    user.naamgegevens = NaamgegevensUser(voornamen=voornaam)
    user.naamgegevens.geslachtsnaam = GeslachtsnaamUser(achternaam=achternaam)
    user.naamgegevens.contactgegevens = ContactgegevensUser()
    user.naamgegevens.contactgegevens.emailAdressen = EmailAdressenUser(emailAdres=username)
    user.userdata.lichaamslengte = Lichaamslengte(lengteWaarde=lengte, lengteDatum=lengtedatum, positie=lengtepositie)
    user.userdata.lichaamsgewicht = Lichaamsgewicht(gewichtWaarde=gewicht, gewichtDatum=gewichtdatum,
                                                    positie=gewichtpositie)
    user.save()
    login = Login(username=username, password=password)
    login.save()
    return 'send'


@app.route('/replacedata/<username>/<lengte>/<lengtedatum>/<lengtepositie>')
def replacelengtdata(username, lengte, lengtedatum, lengtepositie):
    change = User.objects(User__naamgegevens__contactgegevens__emailAdressen__emailAdres=username)\
        .update(set__user__userdata__lichaamlengte_lengteWaarde=lengte,
                set__user__userdata__lichaamlengte_lengteDatum=lengtedatum,
                set__user__userdata__lichaamlengte_positie=lengtepositie)
    change.reload()
    return 'lengte veranderd'


@app.route('/replacegewichtdata/<username>/<gewicht>/<gewichtdatum>/<gewichtpositie>')
def replacegewichtdata(username, gewicht, gewichtdatum, gewichtpositie):
    change = User.objects(User__naamgegevens__contactgegevens__emailAdressen__emailAdres=username) \
        .update(set__user__userdata__lichaamsgewicht__gewichtWaarde=gewicht,
                set__user__userdata__lichaamsgewicht_gewichtDatum=gewichtdatum,
                set__user__userdata__lichaamsgewicht_positie=gewichtpositie)
    change.reload()
    return 'gewicht veranderd'

@app.route('/getdata/<username>')
def getdata(username):
    if User.objects(User__naamgegevens__contactgegevens__emailAdressen__emailAdres=username):
        get_data = User.objects(User__naamgegevens__contactgegevens__emailAdressen__emailAdres=username)
    else:
        get_data = Administrator.objects(Administrator__naamgegevens__contactgegevens__emailAdressen__emailAdres
                                         =username)

    return jsonify(get_data)


@app.route('/core', methods=['POST'])
def Usergegevens():
    action = request.form['action']
    req_geslacht = request.form['geslacht']
    req_voornaam = request.form['voornaam']
    req_achternaam = request.form['achternaam']
    req_username = request.form['username']
    req_password = request.form['password']
    req_geboortedatum = request.form['geboortedatum']
    req_specialisme = request.form['specialisme']
    req_lengte = request.form['lengte']
    req_lengtedatum = request.form['lengtedatum']
    req_lengtepositie = request.form['lengtepositie']
    req_gewicht = request.form['gewicht']
    req_gewichtdatum = request.form['gewichtdatum']
    req_gewichtpositie = request.form['gewichtpositie']

    if action == 'senduser':
        redirect(url_for('sendUser', geslacht=req_geslacht, voornaam=req_voornaam, achternaam=req_achternaam,
                                username=req_username, password=req_password, geboortedatum=req_geboortedatum,
                                lengte=req_lengte, lengtedatum=req_lengtedatum, lengtepositie=req_lengtepositie,
                                gewicht=req_gewicht, gewichtdatum=req_gewichtdatum, gewichtpositie=req_gewichtpositie))
    elif action =='sendadmin':
        redirect(url_for('sendAdministrator', geslacht=req_geslacht, specialisme=req_specialisme, voornaam=req_voornaam,
                         achternaam=req_achternaam, username=req_username, password=req_password,
                         geboortedatum=req_geboortedatum))
    elif action == 'replacelengtdata':
        redirect(url_for('replacelengtdata', username=req_username, lengte=req_lengte, lengtedatum=req_lengtedatum,
                         lengtepositie=req_lengtepositie))

    elif action =='replacegewichtdata':
        redirect(url_for('replacegewichtdata', username=req_username, gewicht=req_gewicht, gewichtdatum=req_gewichtdatum
                         , gewichtpositie=req_gewichtpositie))

    elif action == 'get':
        redirect(url_for('getdata', username=req_username))
