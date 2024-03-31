import requests
from twilio.rest import Client

API_Key = "3bc4b0e3cb30d035a2dfebe1f563e0a0"
account_sid = "ACe627fe888f0b4aeb486a1171d9a03d52"
auth_token = "5d74ce39302cd124478013d6ac2f6c1b"
client = Client(account_sid, auth_token)
parameters = {
    "lat": 51.601311,
    "lon": 12.122150,
    "cnt": 4,
    "appid": API_Key
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()["list"]
will_rain = False

for data in weather_data:
    id = data["weather"][0]["id"]
    description = data["weather"][0]["description"]
    time = data["dt_txt"]
    if id < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        body="It's going to rain today'. Remember to bring Umbrella",
        from_="+16572015492",
        to="+918791820874"
    )