"""Commands blueprint"""

from flask import Blueprint

from vitamin-d-scheduler import scheduler

commands_blueprint = Blueprint('commands', __name__)

@commands_blueprint.cli.command('schedule_job')
def schedule_job():
    """Run job"""
    # scheduler.schedule_job()
