"""Jobs module"""

from flask_apscheduler import APScheduler


scheduler = APScheduler()

def start_jobs():
    """Start jobs"""
    #scheduler.add_job(
    #    id='',
    #    func=,
    #    trigger='cron',
    #    hour=2,
    #)
