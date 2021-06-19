"""Jobs module"""

from flask_apscheduler import APScheduler
import requests


scheduler = APScheduler()

def start_jobs():
    """Start jobs"""
    scheduler.add_job(
        id='activity_sync',
        func=activity_sync,
        trigger='cron',
        hour=1,
    )

def activity_sync():
    """Sync activities"""
    users = requests.get('http://resource_user/user')
    for user in users.json():
        requests.get('http://resource_fitbit/sync/{}'.format(user['username']))
