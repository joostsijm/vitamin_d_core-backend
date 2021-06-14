"""Application blueprint"""

import secrets
from datetime import datetime

from flask import Blueprint, abort, request, jsonify, Response

from vitamin_d_resource_user.models import User, NaamgegevensUser, \
    GeslachtsnaamUser, ContactgegevensUser, EmailAdressenUser, \
    Administrator, Lichaamsgewicht, Lichaamslengte, Session 


blueprint = Blueprint('application', __name__)

@blueprint.route('/', methods=['GET'])
def get():
    """Get"""
    session_code = request.cookies.get('session_code')
    user = User.objects(User__session__code=session_code)
    if not user:
        user = Administrator.objects(User__session__code=session_code)
    return jsonify(user)


@blueprint.route('/', methods=['POST'])
def post():
    """Post"""
    geslacht = request.json['geslacht']
    voornaam = request.json['voornaam']
    achternaam = request.json['achternaam']
    username = request.json['username']
    password = request.json['password']
    geboortedatum = request.json['geboortedatum']
    lengte = request.json['lengte']
    lengtedatum = datetime.now()
    lengtepositie = request.json['lengtepositie']
    gewicht = request.json['gewicht']
    gewichtdatum = datetime.now()
    gewichtpositie = request.json['gewichtpositie']

    user = User(geslacht=geslacht, geboortedatum=geboortedatum, username=username, password=password)
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
    return Response(status=200)


@blueprint.route('/login', methods=['POST'])
def post_login():
    """Post login"""
    username = request.json['username']
    user = User.objects(User__username=username)
    if user:
        password = request.json['password']
        if user.password == password:
            session_code = secrets.token_urlsafe()
            user.session = Session(code=session_code)
            user.save()
            return jsonify(session_code)
    return abort(401)


@blueprint.route('/admin', methods=['POST'])
def post_admin():
    """Manipulate admin data"""
    session_code = request.cookies.get('session_code')
    if not Administrator.objects(User__session__code=session_code):
        return abort(401)
    geslacht = request.json['geslacht']
    voornaam = request.json['voornaam']
    achternaam = request.json['achternaam']
    username = request.json['username']
    password = request.json['password']
    geboortedatum = request.json['geboortedatum']
    specialisme = request.json['specialisme']

    administrator = Administrator(
            geslacht=geslacht,
            geboortedatum=geboortedatum,
            specialisme=specialisme
            username=username,
            password=password
        )
    administrator.naamgegevens = NaamgegevensUser(voornamen=voornaam)
    administrator.naamgegevens.geslachtsnaam = \
            GeslachtsnaamUser(achternaam=achternaam)
    administrator.naamgegevens.contactgegevens = ContactgegevensUser()
    administrator.naamgegevens.contactgegevens.emailAdressen = \
            EmailAdressenUser(emailAdres=username)
    administrator.save()
    return Response(status=200)


@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    print(error)
    return abort(404)
