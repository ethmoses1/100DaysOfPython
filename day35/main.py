import requests
from twilio.rest import Client
from decouple import config
 
account_sid = config('TWI_API_KEY')
auth_token = config('TWI_AUTH_TOKEN')

api_key =config("OWM_API_KEY")
parameters = {
    "lon":-96.796989,
    "lat":32.776665,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
    
weather_for_next_12_hours = data["hourly"][:12]
will_rain = False
for hourly_data in weather_for_next_12_hours:
    print(hourly_data['weather'])
    if int(hourly_data['weather'][0]['id']) < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token) 
    message = client.messages.create(
                                body="It's going to rain today. Remember to bring an ☂️",      
                                from_="+13862309305",
                                to='+61401915591' 
                            ) 
    print(message.status)