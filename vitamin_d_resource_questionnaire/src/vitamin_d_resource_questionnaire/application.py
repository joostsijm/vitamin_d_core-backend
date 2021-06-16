"""Application blueprint"""

from datetime import datetime

from flask import Blueprint, abort, jsonify, Response

from vitamin_d_resource_questionnaire.models import Questionnaire


blueprint = Blueprint('application', __name__)

@blueprint.route('/answer', methods=['POST'])
def post_answer():
    questionnaire = Questionnaire(
            username=request.json['username'],
            mobility=request.json['mobility'],
            selfCare=request.json['selfcare'],
            usualActivities=request.json['usualactivities'],
            painOrDiscomfort=request.json['paindiscomfort'],
            anxietyDepression=request.json['anxietydepression'],
            todaysHealth=request.json['todayhealth']
        )
    questionnaire.save()
    return Response(status=200)


@blueprint.route('/questionnairs/<username>', methods=['GET'])
def get_questionnairs(username):
    questionnaire = Questionnaire.objects(username=username).first()
    return jsonify(questionnaire)


@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    print(error)
    return abort(404)
