# Author Lars Korpel
import requests, json
import datetime

# Api urls
authorize_url = "https://www.fitbit.com/oauth2/authorize"
token_url = "https://api.fitbit.com/oauth2/token"
callback_uri = "http://127.0.0.1:8080/"
api_url = "https://api.fitbit.com/1/user/-/activities/date/" + str(datetime.date.today()) + ".json"

# Test user account credentials for testing purposes
client_id = '23B84K'
client_secret = '2e1e5fb79a84c1e09efab6f80aa908d8'

authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' \
                             + callback_uri + '&scope=activity'
auth_code_response = requests.get(authorization_redirect_url)

# Request permission
print("go to the following url on the browser and enter the code from the returned url: ")
print("---  " + authorization_redirect_url + "  ---")
authorization_code = input('code: ')

# Turn the authorization code into a access token
data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}
print("requesting access token")
access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id,
                                                                                                       client_secret))

# Get access token
tokens = json.loads(access_token_response.text)
access_token = tokens['access_token']
print(access_token)

# Api call
api_call_headers = {'Authorization': 'Bearer ' + access_token}
api_call_response = requests.get(api_url, headers=api_call_headers, verify=False)

# Get activity data
activity = str(api_call_response.text)
json_activity = json.loads(activity)
json_activity = json_activity['summary']['distances']


def totaldistance():
    for i in range(len(json_activity)):
        if 'loggedActivities' in json_activity[i]['activity']:
            distance = round(json_activity[i]['distance'], 2)
            print("Total moved distance: " + str(distance) + " kilometers!")
            return distance


def distancewalked():
    for i in range(len(json_activity)):
        if 'Walk' in json_activity[i]['activity']:
            distance = round(json_activity[i]['distance'], 2)
            print("Walked: " + str(distance) + " kilometers!")
            return distance


def distanceran():
    for i in range(len(json_activity)):
        if 'Run' in json_activity[i]['activity']:
            distance = round(json_activity[i]['distance'], 2)
            print("Ran: " + str(distance) + " kilometers!")
            return distance


def distancebiked():
    for i in range(len(json_activity)):
        if 'Bike' in json_activity[i]['activity']:
            distance = round(json_activity[i]['distance'], 2)
            print("Biked: " + str(distance) + " kilometers!")
            return distance


def distanceswam():
    for i in range(len(json_activity)):
        if 'Swim' in json_activity[i]['activity']:
            distance = round(json_activity[i]['distance'], 2)
            print("Swam: " + str(distance) + " kilometers!")
            return distance


# FOR DEBUGGING
# totaldistance()
# distancewalked()
# distanceran()
# distancebiked()
# distanceswam()
