"""Application blueprint"""

from datetime import datetime

from flask import Blueprint, abort, request, jsonify, Response

from vitamin_d_resource_user.models import User, NaamgegevensUser, \
    GeslachtsnaamUser, ContactgegevensUser, EmailAdressenUser, \
    Administrator, UserData, Lichaamsgewicht, Lichaamslengte, \
    Schedule


blueprint = Blueprint('application', __name__)

@blueprint.route('/user/<username>', methods=['GET'])
def get(username):
    """Get user"""
    user = User.objects(username=username).first()
    if not user:
        user = Administrator.objects(username=username).first()
    return jsonify(user)


@blueprint.route('/user', methods=['POST'])
def post():
    """Post user"""
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
    kleding = request.json['gewichtpositie']

    user = User(
            geslacht=geslacht,
            geboortedatum=geboortedatum,
            username=username,
            password=password
        )
    user.naamgegevens = NaamgegevensUser(voornamen=voornaam)
    user.naamgegevens.geslachtsnaam = GeslachtsnaamUser(achternaam=achternaam)
    user.naamgegevens.contactgegevens = ContactgegevensUser()
    user.naamgegevens.contactgegevens.emailAdressen = EmailAdressenUser(emailAdres=username)
    user.userdata = UserData()
    user.userdata.lichaamslengte = Lichaamslengte(
            lengteWaarde=lengte,
            lengteDatum=lengtedatum,
            positie=lengtepositie
        )
    user.userdata.lichaamsgewicht = Lichaamsgewicht(
            gewichtWaarde=gewicht,
            gewichtDatum=gewichtdatum,
            kleding=kleding
        )
    user.save()
    return Response(status=200)


@blueprint.route('/admin', methods=['POST'])
def post_admin():
    """Manipulate admin data"""
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
            specialisme=specialisme,
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


@blueprint.route('/sendactiviteiten/username/activiteit/geplandeafstand', methods=['POST'])
def sendactiviteiten(username, activiteit, geplandeafstand):
    """Post schedule from user"""
    sendactiviteit = Schedule(username=username, activiteit=activiteit, geplandeafstand=geplandeafstand)
    sendactiviteit.save()
    Response(status=200)


@blueprint.route('/getactiviteiten/username/activiteit/datum', methods=['GET'])
def getactiviteiten(username, activiteit, datum):
    """Get schedule from user"""
    schedule = Schedule.objects(username=username, activiteit=activiteit, activiteitDatum=datum)
    return jsonify(schedule)


@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    print(error)
    return abort(404)
