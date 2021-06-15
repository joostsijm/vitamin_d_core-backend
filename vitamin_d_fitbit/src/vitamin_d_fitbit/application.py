"""Application blueprint"""

from flask import Blueprint, abort

from vitamin_d_fitbit.fitapi import fitapi

from vitamin_d_resource_user/vitamin_d_resource_user.models import Schedule


blueprint = Blueprint('application', __name__)

@blueprint.route('/', methods=(['GET']))
def index():
    """Get data from fitbit"""
    return 'send'


@blueprint.route('/afstand/username/activiteit/datum', methods=['POST'])
def afstand(username, activiteit, datum):
    """Post of de activiteit is behaald"""
    if activiteit == lopen:
        afstandactiviteit = distancewalked()
    elif activiteit == rennen:
        afstandactiviteit = distanceran()
    elif activiteit == fietsen:
        afstandactiviteit = distancebiked()
    else: 
        afstandactiviteit = distanceswam()

    qset = Schedule.objects(username=username, activiteit=activiteit, activiteitDatum=datum)
    doc = qset.first()
    if int(doc.geplandeafstand) <= afstandactiviteit:
        return True
    else:
        return False


@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return abort(404)
