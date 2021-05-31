"""Application blueprint"""

from flask import Blueprint, abort

from vitamin_d_resource_user.models import User, NaamgegevensUser, \
        AdressgegevensUser, GeslachtsnaamUser, ContactgegevensUser, \
        TelefoonnummersUser, EmailAdressenUser


blueprint = Blueprint('application', __name__)

@blueprint.route('/', methods=(['GET']))
def index():
    """Index route"""
    user = User(geslacht="M")
    user.naamgegevens = NaamgegevensUser(
            voornamen="jesse", initialen="J.R", roepnaam="jj"
        )
    user.naamgegevens.adressgegevens = AdressgegevensUser(
            straat="van Heuven Goedhartlaan",
            huisnummer=152, huisnummerletter=" ", huisnummerToevoeging=" ",
            aanduidingBijNummer=" ", woonplaats="Amstelveen",
            gemeente="Amstelveen", land="NL", postcode="1181LL",
            aditioneleInformatie=" ", adressSoort='PST'
        )
    user.naamgegevens.geslachtsnaam = GeslachtsnaamUser(
            voorvoegsels=" ", achternaam="jones"
        )
    user.naamgegevens.contactgegevens = ContactgegevensUser()
    user.naamgegevens.contactgegevens.telefoonnummer = TelefoonnummersUser(
            telefoonnummer=31615651877, toelichting=" ", telecomType="LL",
            nummerSoort="HP"
        )
    user.naamgegevens.contactgegevens.emailAdressen = EmailAdressenUser(
            emailAdres="jesse.r.jones@test.nl", emailSoort="HP"
        )
    user.save()
    return "send"

# @app.route('/add')
# def home():
#
#     return "added"


@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return abort(404)
