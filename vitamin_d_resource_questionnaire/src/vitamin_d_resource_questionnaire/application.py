"""Application blueprint"""

from datetime import datetime

from flask import Blueprint, abort, jsonify, Response, request

from vitamin_d_resource_questionnaire.models import Questionnaire, MOBILITY, \
        SELFCARE, USUALACTIVITIES, PAINDISCOMFORT, ANXIETYDEPRESSION


blueprint = Blueprint('application', __name__)

@blueprint.route('/answer', methods=['POST'])
def post_answer():
    """Answer questionnaire"""
    questionnaire = Questionnaire(
            username=request.json['username'],
            mobility=MOBILITY[request.json['mobility']],
            selfCare=SELFCARE[request.json['selfcare']],
            usualActivities=USUALACTIVITIES[request.json['usualactivities']],
            painOrDiscomfort=PAINDISCOMFORT[request.json['paindiscomfort']],
            anxietyDepression=ANXIETYDEPRESSION[
                    request.json['anxietydepression']
                ],
            todaysHealth=request.json['todayshealth'],
            date=datetime.now()
        )
    questionnaire.save()
    return Response(status=200)


@blueprint.route('/questionnaires/<username>', methods=['GET'])
def get_questionnairs(username):
    """Get questionaires based on username"""
    questionnaires = Questionnaire.objects(username=username)
    questionnaires_list = []
    for questionnaire in questionnaires:
        questionnaires_list.append({
                'date': datetime.timestamp(questionnaire.date) * 1000,
                'mobility': MOBILITY.index(questionnaire.mobility),
                'selfCare': SELFCARE.index(questionnaire.selfCare),
                'usualActivities': USUALACTIVITIES.index(
                        questionnaire.usualActivities
                    ),
                'painOrDiscomfort': PAINDISCOMFORT.index(
                        questionnaire.painOrDiscomfort
                    ),
                'anxietyDepression': ANXIETYDEPRESSION.index(
                        questionnaire.anxietyDepression
                    ),
                'todaysHealth': questionnaire.todaysHealth,
            })
    return jsonify(questionnaires_list)


@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    print(error)
    return abort(404)
