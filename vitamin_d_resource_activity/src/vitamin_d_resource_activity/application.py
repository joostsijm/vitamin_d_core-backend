"""Application blueprint"""

from flask import Blueprint, abort, request, jsonify, Response

from vitamin_d_resource_activity.models import Activity


blueprint = Blueprint('application', __name__)

@blueprint.route('/activity/<username>', methods=['GET'])
def get_activity(username):
    """Get activitiy"""
    return jsonify(Activity.objects(username=username).first())


@blueprint.route('/activity', methods=['POST'])
def post_activity():
    """Post activity"""
    activity = Activity(
            username = request.json['username'],
            date = request.json['date'],
            distance = request.json['distance'],
            activity_type = request.json['type'],
        )
    activity.save()
    Response(status=200)


@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    print(error)
    return abort(404)
