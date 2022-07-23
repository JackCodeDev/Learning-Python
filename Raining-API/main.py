import requests
import os
from twilio.rest import Client

API_KEY = "7f929f9e17b4df398d73c41da0518d32"

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
Phone_number = "19206718445"
account_sid = "AC80f187f805ec2348f769f3ac2c4ddd93"
auth_token = "023340fcd9a9eb8c6887ae289d3c24c9"

weather_params = {
    "lat": 21.028280,
    "lon": 105.853882,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"

}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

# print(data["hourly"][0]["weather"][0]["id"])
weather_slice = hourly_data = data["hourly"][:12]

is_rain = False
for hour in hourly_data:
    # print(hour["weather"][0]["id"])
    if hour["weather"][0]["id"] < 700:
        is_rain = True
if is_rain:

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. You should bring umbrella☂️. From honey with love ❤️",
        from_='+19206718445',
        to='your phone'
    )
    print(message.status)





