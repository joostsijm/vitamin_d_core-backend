"""Application blueprint"""

from flask import Blueprint, abort, request, redirect, url_for, jsonify

from vitamin_d_resource_user.models import User, NaamgegevensUser
        # AdressgegevensUser, GeslachtsnaamUser, ContactgegevensUser, \
        # TelefoonnummersUser,  EmailAdressenUser


blueprint = Blueprint('application', __name__)

@blueprint.route('/n')
def home():
    """Home"""
    return "hallo"


@blueprint.route('/sendName/<geslacht>/<voornaam>/<initialen>/<roepnaam>')
def sendname(geslacht, voornaam, initialen, roepnaam):
    """Send name"""
    user = User(geslacht=geslacht)
    user.naamgegevens = NaamgegevensUser(voornamen=voornaam, initialen=initialen, roepnaam=roepnaam)

    user.save()
    return 'send'


@blueprint.route('/getdata/<voornaam>/<achternaam>')
def getdata(voornaam, achternaam):
    """Get data"""
    if (voornaam & achternaam) != ' ':
        get_data = User.objects(
                naamgegevens__voornamen=voornaam,
                naamgegevens__geslachtsnaam__achternaam=achternaam
            )
    elif voornaam != ' ':
        get_data = User.objects(naamgegevens__voornamen=voornaam)
    elif achternaam != ' ':
        get_data = User.objects(naamgegevens__geslachtsnaam__achternaam=achternaam)
    else:
        get_data = User.objects()

    return jsonify(get_data)


@blueprint.route('/core', methods=['POST'])
def login():
    """login"""
    action = request.form['action']
    req_geslacht = request.form['geslacht']
    req_voornaam = request.form['voornaam']
    req_initialen = request.form['initialen']
    req_roepnaam = request.form['roepnaam']
    req_achternaam = request.form['achternaam']

    if action == 'send':
        return redirect(url_for(
                'sendName',
                geslacht=req_geslacht,
                voornaam=req_voornaam,
                initialen=req_initialen,
                roepnaam=req_roepnaam
            ))
    if action == 'replace':
        return 0

    # elif action == 'get':
    return redirect(url_for(
            'getdata',
            voornaam=req_voornaam,
            achternaam=req_achternaam
        ))


@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return abort(404)
