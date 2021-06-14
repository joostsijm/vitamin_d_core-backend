"""Application blueprint"""

import secrets

from flask import Blueprint, abort, request, jsonify

from vitamin_d_resource_auth.models import User, Administrator, Session


blueprint = Blueprint('application', __name__)

@blueprint.route('/auth', methods=['POST'])
def post_auth():
    """Post auth, check authentication"""
    user = User.objects(User__session__code=request.json['session_code'])
    if user:
        return user.username
    admin = Administrator.objects(Administrator__session__code=request.json['session_code'])
    if admin:
        return admin.username
    return abort(401)


@blueprint.route('/login', methods=['POST'])
def post_login():
    """Post login"""
    username = request.json['username']
    user = User.objects(User__username=username)
    if user:
        password = request.json['password']
        if user.password == password:
            session_code = secrets.token_urlsafe()
            user.session = Session(code=session_code)
            user.save()
            return jsonify(session_code)
    return abort(401)


@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    print(error)
    return abort(404)
