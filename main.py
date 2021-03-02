import os

import requests
from twilio.rest import Client

weather_params = {
    "lat": 32.361668,
    "lon": -86.279167,
    "appid": "YOUR OPENWEATHER API KEY",
}
account_sid = 'YOUR TWILIO ACCOUNT_SID'
auth_token = 'YOUR TWILIO AUTH TOKEN'

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Bring an umbrella",
            from_='YOUR NUMBER U HAVE FROM TWILIO',
            to='YOUR TWILIO AUTH PHONE NUMBER'
    )
print(message.status)