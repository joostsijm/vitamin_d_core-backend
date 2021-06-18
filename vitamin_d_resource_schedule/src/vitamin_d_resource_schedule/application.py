"""Application blueprint"""

from flask import Blueprint, abort, request, jsonify, Response

from vitamin_d_resource_schedule.models import Schedule


blueprint = Blueprint('application', __name__)

@blueprint.route('/schedule/<username>', methods=['GET'])
def get_schedule(username):
    """Get activitiy"""
    return jsonify(Schedule.objects(username=username))


@blueprint.route('/schedule', methods=['POST'])
def post_schedule():
    """Post schedule"""
    schedule = Schedule(
            username = request.json['username'],
            date = request.json['date'],
            distance = request.json['distance'],
            activity_type = request.json['type'],
        )
    schedule.save()
    return Response(status=200)


@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    print(error)
    return abort(404)
