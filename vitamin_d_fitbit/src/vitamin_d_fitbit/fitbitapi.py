import requests, json
from bs4 import BeautifulSoup
import subprocess
import sys
import pdb

authorize_url = "https://www.fitbit.com/oauth2/authorize"
token_url = "https://api.fitbit.com/oauth2/token"
callback_uri = "http://127.0.0.1:8080/"
api_url = "https://api.fitbit.com/1/user/-/profile.json"

# Test user account credentials, don't worry!
client_id = '23B84K'
client_secret = '2e1e5fb79a84c1e09efab6f80aa908d8'

authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' + callback_uri + '&scope=profile'
auth_code_response = requests.get(authorization_redirect_url)
# soup = BeautifulSoup(auth_code_response.content, "html.parser")
# pdb.set_trace()

print("go to the following url on the browser and enter the code from the returned url: ")
print("---  " + authorization_redirect_url + "  ---")
authorization_code = input('code: ')

# turn the authorization code into a access token, etc
data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}
print("requesting access token")
access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

print("response")
print(access_token_response.headers)
print('body: ' + access_token_response.text)

tokens = json.loads(access_token_response.text)
access_token = tokens['access_token']
print("access token: " + access_token)

api_call_headers = {'Authorization': 'Bearer ' + access_token}
api_call_response = requests.get(api_url, headers=api_call_headers, verify=False)

print(api_call_response.text)
