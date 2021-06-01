"""Application blueprint"""

from flask import Blueprint, abort

from vitamin_d_fitbit.fitapi import fitapi


blueprint = Blueprint('application', __name__)

@blueprint.route('/', methods=(['GET']))
def index():
    """Get data from fitbit"""
    return 'send'

@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return abort(404)
