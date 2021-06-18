"""
Fitbit API

Author: Lars Korpel
"""

import datetime
import json

import requests


# Api urls
AUTHORIZE_URL = "https://www.fitbit.com/oauth2/authorize"
TOKEN_URL = "https://api.fitbit.com/oauth2/token"
CALLBACK_URI = "http://127.0.0.1:8080/"
API_URL = "https://api.fitbit.com/1/user/-/activities/date/{}.json".format(datetime.date.today())

# Test user account credentials for testing purposes
CLIENT_ID = '23B84K'
CLIENT_SECRET = '2e1e5fb79a84c1e09efab6f80aa908d8'

AUTHORIZATION_REDIRECT_URL = \
    '{}?response_type=code&client_id={}&redirect_uri={}&scope=activity'.format(
        AUTHORIZE_URL,
        CLIENT_ID,
        CALLBACK_URI,
    )
AUTH_CODE_RESPONSE = requests.get(AUTHORIZATION_REDIRECT_URL)

# Request permission
print("go to the following url on the browser and enter the code from the returned url: ")
print("---  {}  ---".format(AUTHORIZATION_REDIRECT_URL ))
AUTHORIZATION_CODE = input('code: ')

# Turn the authorization code into a access token
DATA = {
        'grant_type': 'authorization_code',
        'code': AUTHORIZATION_CODE,
        'redirect_uri': CALLBACK_URI
    }

print("requesting access token")
ACCESS_TOKEN_RESPONSE = requests.post(
        TOKEN_URL,
        data=DATA,
        verify=False,
        allow_redirects=False,
        auth=(CLIENT_ID, CLIENT_SECRET)
    )

# Get access token
TOKENS = json.loads(ACCESS_TOKEN_RESPONSE.text)
ACCESS_TOKEN = TOKENS['access_token']
print(ACCESS_TOKEN)

# Api call
API_CALL_HEADERS = {'Authorization': 'Bearer {}'.format(ACCESS_TOKEN)}
API_CALL_RESPONSE = requests.get(API_URL, headers=API_CALL_HEADERS, verify=False)

# Get activity data
ACTIVITY = str(API_CALL_RESPONSE.text)
JSON_ACTIVITY = json.loads(ACTIVITY)
JSON_ACTIVITY = JSON_ACTIVITY['summary']['distances']


def totaldistance():
    """Total distance"""
    for activity in JSON_ACTIVITY:
        if 'loggedActivities' in activity['activity']:
            distance = round(activity['distance'], 2)
            print("Total moved distance: {} kilometers!".format(distance))
            return distance
    return 0


def distancewalked():
    """Distance walked"""
    for activity in JSON_ACTIVITY:
        if 'Walk' in activity['activity']:
            distance = round(activity['distance'], 2)
            print("Walked distance: {} kilometers!".format(distance))
            return distance
    return 0


def distanceran():
    """Distance ran"""
    for activity in JSON_ACTIVITY:
        if 'Run' in activity['activity']:
            distance = round(activity['distance'], 2)
            print("Run distance: {} kilometers!".format(distance))
            return distance
    return 0


def distancebiked():
    """Distance biked"""
    for activity in JSON_ACTIVITY:
        if 'Bike' in activity['activity']:
            distance = round(activity['distance'], 2)
            print("Biked distance: {} kilometers!".format(distance))
            return distance
    return 0


def distanceswam():
    """Distance swam"""
    for activity in JSON_ACTIVITY:
        if 'Swim' in activity['activity']:
            distance = round(activity['distance'], 2)
            print("Swam distance: {} kilometers!".format(distance))
            return distance
    return 0


# FOR DEBUGGING
# totaldistance()
# distancewalked()
# distanceran()
# distancebiked()
# distanceswam()
