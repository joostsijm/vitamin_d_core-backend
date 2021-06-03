"""Application blueprint"""

from datetime import datetime

from flask import Blueprint, abort, request, redirect, url_for, jsonify

from vitamin_d_resource_user.models import User, NaamgegevensUser, \
    GeslachtsnaamUser, ContactgegevensUser, EmailAdressenUser, \
    Administrator, Lichaamsgewicht, Lichaamslengte, Login


blueprint = Blueprint('application', __name__)

@blueprint.route('/n')
def home():
    """Home route"""
    return "hallo"


@blueprint.route('/getdata/<username>')
def getdata(username):
    """Get user data"""
    if User.objects(User__naamgegevens__contactgegevens__emailAdressen__emailAdres=username):
        get_data = User.objects(
                User__naamgegevens__contactgegevens__emailAdressen__emailAdres=username
            )
    else:
        get_data = Administrator.objects(
                Administrator__naamgegevens__contactgegevens__emailAdressen__emailAdres=username
            )
    return jsonify(get_data)


@blueprint.route('/user', methods=['POST', 'GET'])
def user_data():
    """Manipulate user data"""
    if request.method == 'POST':
        geslacht = request.form['geslacht']
        voornaam = request.form['voornaam']
        achternaam = request.form['achternaam']
        username = request.form['username']
        password = request.form['password']
        geboortedatum = request.form['geboortedatum']
        lengte = request.form['lengte']
        lengtedatum = datetime.now()
        lengtepositie = request.form['lengtepositie']
        gewicht = request.form['gewicht']
        gewichtdatum = datetime.now()
        gewichtpositie = request.form['gewichtpositie']

        user = User(geslacht=geslacht, geboortedatum=geboortedatum)
        user.naamgegevens = NaamgegevensUser(voornamen=voornaam)
        user.naamgegevens.geslachtsnaam = GeslachtsnaamUser(achternaam=achternaam)
        user.naamgegevens.contactgegevens = ContactgegevensUser()
        user.naamgegevens.contactgegevens.emailAdressen = EmailAdressenUser(emailAdres=username)
        user.userdata.lichaamslengte = Lichaamslengte(
                lengteWaarde=lengte,
                lengteDatum=lengtedatum,
                positie=lengtepositie
            )
        user.userdata.lichaamsgewicht = Lichaamsgewicht(
                gewichtWaarde=gewicht,
                gewichtDatum=gewichtdatum,
                positie=gewichtpositie
            )
        user.save()
        login = Login(username=username, password=password)
        login.save()
        return 'send'
    return redirect(url_for('getdata', username=request.form['username']))

@blueprint.route('/admin', methods=['POST', 'GET'])
def admin_data():
    """Manipulate admin data"""
    if request.method == 'POST':
        geslacht = request.form['geslacht']
        voornaam = request.form['voornaam']
        achternaam = request.form['achternaam']
        username = request.form['username']
        password = request.form['password']
        geboortedatum = request.form['geboortedatum']
        specialisme = request.form['specialisme']

        administrator = Administrator(
                geslacht=geslacht,
                geboortedatum=geboortedatum,
                specialisme=specialisme
            )
        administrator.naamgegevens = NaamgegevensUser(voornamen=voornaam)
        administrator.naamgegevens.geslachtsnaam = \
                GeslachtsnaamUser(achternaam=achternaam)
        administrator.naamgegevens.contactgegevens = ContactgegevensUser()
        administrator.naamgegevens.contactgegevens.emailAdressen = \
                EmailAdressenUser(emailAdres=username)
        administrator.save()
        login = Login(username=username, password=password)
        login.save()
        return 'send'
    return redirect(url_for('getdata', username=request.form['username']))


@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    print(error)
    return abort(404)
