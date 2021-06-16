"""Application blueprint"""

from datetime import datetime

from flask import Blueprint, abort, jsonify, Response

from vitamin_d_questionair.models import Questionair


blueprint = Blueprint('application', __name__)


@blueprint.route('/sendquestionair/respondent/mobility/selfcare/usualactivities/pain/anxiety/health', methodes=['POST'])
def sendquestionair(respondent, mobility, selfcare, usualactivities, pain, anxiety, health):
    sendanswer = Questionair(respondent=respondent, mobility=mobility, selfCare=selfcare,
                             usualActivities=usualactivities, painOrDiscomfort=pain, anxietyDepression=anxiety,
                             todaysHealth=health)
    sendanswer.save()
    return Response(status=200)


@blueprint.route('/getquestionair/respondent/datum', methods=['GET'])
def getquestionair(respondent, datum):
    getanswer = Questionair.objects(respondent=respondent, datumVanQuestionair=datum)
    return jsonify(getanswer)



@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    print(error)
    return abort(404)
