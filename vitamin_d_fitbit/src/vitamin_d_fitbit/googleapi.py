# Author = Lars Korpel

import requests
import time
import pendulum
import requests_oauthlib
import os

# Initialize time
endTime_int = int(round(time.time() * 1000))
endTime = str(endTime_int)
startTime_int = int(endTime_int - 864000000)
startTime = str(startTime_int)

# Auth is de authorization token gegenereerd door Google als er ingelogd wordt door de gebruiker. (Verloopt elk uur (dus voor mij geen gevaar dat dit openbaar is voor nu))
# Dit moet later via OAuth geregeld gaan worden.
auth = "Bearer ya29.a0AfH6SMBi96Phau6n1_ffnLtOUx_asi5_1aNwXLO4HqdGd-FsTHIrabtmI89FBESz83gm43ZmOu245G0iQlZ5aLeUrOPFGTEiWwWX7mk5RL_CDQBdjCaIAgSDf4xk3SmeEBHpXJ-ww2dc2Mlu2n6kibf3veDv"


def countedSteps():
    # Url api
    url = "https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate"
    # Inhoud van request
    payload = "{\"aggregateBy\":[{\"dataSourceId\": \"derived:com.google.step_count.delta:com.google.android.gms:estimated_steps\"}],\"bucketByTime\":{\"durationMillis\": 86400000},\"startTimeMillis\": "+ startTime +",\"endTimeMillis\": "+ endTime +"}"
    headers = {'Authorization': auth, 'Content-Type': 'application/json'}

    # Response api
    response = requests.post(url, headers=headers, data=payload)
    response_json = response.json()
    i = 0
    length = len(response_json['bucket'])
    print(response.text)

    while i < length:
        steps_a = response_json['bucket'][i]
        # Get amount of steps
        steps_b = steps_a['dataset'][0]
        steps_c = steps_b['point'][0]
        steps_d = steps_c['value'][0]
        steps_int = steps_d['intVal']
        steps = str(steps_int)

        # Get date and time of data
        time_from_millis = int(steps_a['startTimeMillis'])
        time_from_temp = pendulum.from_timestamp(time_from_millis / 1000.0, tz='Europe/Amsterdam')
        time_from = time_from_temp.to_datetime_string()
        time_to_millis = int(steps_a['endTimeMillis'])
        time_to_temp = pendulum.from_timestamp(time_to_millis / 1000.0, tz='Europe/Amsterdam')
        time_to = time_to_temp.to_datetime_string()
        i = i + 1

        # Temp data print
        print("From " + time_from + " to " + time_to + " " + steps + " steps have been counted!")

        # Data needs to be sent to the database, ordered by day and connected to the specific user.


def credentials():
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    # Credentials you get from registering a new application
    client_id = '320545529437-r4atgi73fflempfv1lbo39ts5stk9b8v.apps.googleusercontent.com'
    client_secret = 'GTzUOpkMgeI81v-D6br5XsVd'
    redirect_uri = 'http://localhost:8080/'

    # OAuth endpoints given in the Google API documentation
    authorization_base_url = "https://accounts.google.com/o/oauth2/auth"
    token_url = "https://oauth2.googleapis.com/token"
    scope = [
        "https://www.googleapis.com/auth/fitness.sleep.read",
        "https://www.googleapis.com/auth/fitness.heart_rate.read",
        "https://www.googleapis.com/auth/fitness.reproductive_health.read",
        "https://www.googleapis.com/auth/fitness.body_temperature.read",
        "https://www.googleapis.com/auth/fitness.oxygen_saturation.read%",
        "https://www.googleapis.com/auth/fitness.blood_glucose.read",
        "https://www.googleapis.com/auth/fitness.blood_pressure.read",
        "https://www.googleapis.com/auth/fitness.nutrition.read",
        "https://www.googleapis.com/auth/fitness.body.read",
        "https://www.googleapis.com/auth/fitness.location.read",
        "https://www.googleapis.com/auth/fitness.activity.read"
        ]

    from requests_oauthlib import OAuth2Session
    google = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

    # Redirect user to Google for authorization
    authorization_url, state = google.authorization_url(authorization_base_url,
        access_type = "offline", prompt = "select_account")

    print
    'Please go here and authorize,', authorization_url

    # Get the authorization verifier code from the callback url
    redirect_response = input('Paste the full redirect URL here:')

    # Fetch the access token
    google.fetch_token(token_url, client_secret=client_secret,
        authorization_response = redirect_response)

    # Fetch a protected resource, i.e. user profile
    r = google.get('https://fitness.googleapis.com/fitness/v1/users/me/dataSources')
    print
    r.content


countedSteps()
# credentials()

# import pdb
# pdb.set_trace()
