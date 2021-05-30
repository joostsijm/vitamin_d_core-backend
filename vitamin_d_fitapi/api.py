import requests
import time
import pendulum

# Initialize time
endTime_int = int(round(time.time() * 1000))
endTime = str(endTime_int)
startTime_int = int(endTime_int - 1000000000)
startTime = str(startTime_int)

# Auth is de authorization token gegenereerd door Google als er ingelogd wordt door de gebruiker. (Verloopt elk uur (dus voor mij geen gevaar dat dit openbaar is voor nu))
# Dit moet later via OAuth geregeld gaan worden.
auth = "Bearer ya29.a0AfH6SMBjJa2quHl42omvqHdB2smIo2GfIFZ2raFp7Xgh4z60HN1uPJv9nj7-pztGJlvggm2S-LvLL8MvYK99vCRMzNmOXaTK8DWDOaufFUD1Y2p72kKujlPU1AfDk4IMmYM7phWNeJEklCtIi5QrdCNvNIeD"

# Url api
url = "https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate"
# Inhoud van request
payload = "{\"aggregateBy\":[{\"dataSourceId\": \"derived:com.google.step_count.delta:com.google.android.gms:estimated_steps\"}],\"bucketByTime\":{\"durationMillis\": 86400000},\"startTimeMillis\": "+ startTime +",\"endTimeMillis\": "+ endTime +"}"
headers = {'Authorization': auth, 'Content-Type': 'application/json'}

# Response van api
response = requests.post(url, headers=headers, data=payload)
response_json = response.json()
i = 0
length = len(response_json['bucket'])

# Filter om alleen stappen weer te geven
while i < length:
    a = response_json['bucket'][i]
    # Get amount of steps
    steps_b = a['dataset'][0]
    steps_c = steps_b['point'][0]
    steps_d = steps_c['value'][0]
    steps_int = steps_d['intVal']
    steps = str(steps_int)

    # Get date and time of data
    time_from_millis = int(a['startTimeMillis'])
    time_from_temp = pendulum.from_timestamp(time_from_millis / 1000.0, tz='Europe/Amsterdam')
    time_from = time_from_temp.to_datetime_string()
    time_to_millis = int(a['endTimeMillis'])
    time_to_temp = pendulum.from_timestamp(time_to_millis / 1000.0, tz='Europe/Amsterdam')
    time_to = time_to_temp.to_datetime_string()
    i = i + 1

    # Temp data print
    print("From " + time_from + " to " + time_to + " " + steps + " steps have been counted!")

# import pdb
# pdb.set_trace()
