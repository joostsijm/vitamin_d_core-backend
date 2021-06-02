"""Application blueprint"""

from flask import Blueprint, abort, request, redirect, url_for, jsonify

from vitamin_d_resource_user.models import User, NaamgegevensUser
        # AdressgegevensUser, GeslachtsnaamUser, ContactgegevensUser, \
        # TelefoonnummersUser,  EmailAdressenUser


blueprint = Blueprint('application', __name__)

@blueprint.route('/n')
def home():
    return "hallo"


@blueprint.route('/sendAdministrator/<geslacht>/<specialisme>/<voornaam>/<achternaam>/<username>/<password>/<geboortedatum>')
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


@blueprint.route('/sendUser/<geslacht>/<voornaam>/<achternaam>/<username>/<password>/<geboortedatum>/<lengte>/<lengtedatum>/'
           '<lengtepositie>/<gewicht>/<gewichtdatum>/<gewichtpositie>')
def sendName(geslacht, voornaam, achternaam, username, password, geboortedatum, lengte, lengtedatum, lengtepositie,
             gewicht, gewichtdatum, gewichtpositie):
    user = User(geslacht=geslacht, geboortedatum=geboortedatum)
    user.naamgegevens = NaamgegevensUser(voornamen=voornaam)
    user.naamgegevens.geslachtsnaam = GeslachtsnaamUser(achternaam=achternaam)
    user.naamgegevens.contactgegevens = ContactgegevensUser()
    user.naamgegevens.contactgegevens.emailAdressen = EmailAdressenUser(emailAdres=username)
    user.userdata.lichaamslengte = Lichaamslengte(lengteWaarde=lengte, lengteDatum=lengtedatum, positie=lengtepositie)
    user.userdata.lichaamsgewicht = Lichaamsgewicht(gewichtWaarde=gewicht, gewichtDatum=gewichtdatum, positie=gewichtpositie)
    user.save()
    login = Login(username=username, password=password)
    login.save()
    return 'send'


@blueprint.route('/getdata/<username>')
def getdata(username):
    if User.objects(User__naamgegevens__contactgegevens__emailAdressen__emailAdres=username):
        get_data = User.objects(User__naamgegevens__contactgegevens__emailAdressen__emailAdres=username)
    else:
        get_data = Administrator.objects(Administrator__naamgegevens__contactgegevens__emailAdressen__emailAdres =username)

    return jsonify(get_data)


@blueprint.route('/core', methods=['POST'])
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
    elif action == 'replace':
        print(0)

    elif action == 'get':
        redirect(url_for('getdata', username=req_username))


@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return abort(404)
