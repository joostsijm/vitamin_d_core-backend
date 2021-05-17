"""Stall blueprint"""

from flask import Blueprint, request, abort

from iot_backend import payment_wrapper


blueprint = Blueprint('api_stall', __name__, url_prefix='/api/stall')

@blueprint.route('/', methods=(['GET', 'POST']))
def index():
    """index route"""
    if request.method == 'POST':
        return 'TODO: implement POST'
    return 'TODO: implement GET'

@blueprint.route('/create_payment', methods=(['POST']))
def create_payment():
    """Create payment"""
    amount = request.form.get('amount')
    # return QR url
    return payment_wrapper.create_payment(amount)

@blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return abort(404)

