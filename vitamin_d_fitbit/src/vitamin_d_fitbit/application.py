"""Application blueprint"""

from datetime import date

from flask import Blueprint, abort, Response
import requests

from vitamin_d_fitbit import fitbitapi


blueprint = Blueprint('application', __name__)

@blueprint.route('/sync/<username>', methods=(['GET']))
def index(username):
    """Sync data from fitbit"""
    walked_distance = fitbitapi.distancewalked()
    if walked_distance:
        json = {
                'username': username,
                'date': date.today(),
                'distance': walked_distance,
                'type': 'lopen',
            }
        requests.post('http://resource_activity/', json=json)
    ran_distance = fitbitapi.distanceran()
    if ran_distance:
        json = {
                'username': username,
                'date': date.today(),
                'distance': ran_distance,
                'type': 'rennen',
            }
        requests.post('http://resource_activity/', json=json)
    biked_distance = fitbitapi.distancebiked()
    if biked_distance:
        json = {
                'username': username,
                'date': date.today(),
                'distance': biked_distance,
                'type': 'fietsen',
            }
        requests.post('http://resource_activity/', json=json)
    swam_distance = fitbitapi.distanceswam()
    if swam_distance:
        json = {
                'username': username,
                'date': date.today(),
                'distance': swam_distance,
                'type': 'zwemmen',
            }
        requests.post('http://resource_activity/', json=json)
    return Response(status=200)


@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return abort(404)
