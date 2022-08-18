from threading import Timer
import requests
from datetime import datetime
import smtplib
from decouple import config
import time

my_email = config('EMAIL')
my_pass = config('PASSWORD')

MY_LAT = -33.807919 # Your latitude
MY_LONG = -150.987411 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}



time_now = datetime.now().hour
continue_on = True

while continue_on:
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    #swapped around becuase the api is wrong
    sunset = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunrise = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if time_now >= sunset or time_now <= sunrise:
        if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_pass)  
                connection.sendmail(from_addr=my_email, to_addrs="mosesbuta123@gmail.com", msg="Subject:ISS is over your head\n\nLook up ISS is above your head")  
    time.sleep(60)
        
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



