import smtplib
import pandas as pd
import datetime as dt
from random import randint
from decouple import config

my_email = config('EMAIL')
my_pass = config('PASSWORD')

#Get current birthday
try:
    data = pd.read_csv("birthdays.csv")
except FileNotFoundError:
    pass
else:
    data_dict = data.to_dict(orient='records')

now = dt.datetime.now()
current_month = now.month
current_day = now.day

for birthday in data_dict:
    name = birthday["name"]
    email = birthday["email"]
    month = birthday["month"]
    day = birthday["day"]
    if month == current_month and day == current_day:
        #Get random letter 
        with open(f"letter_templates/letter_{randint(1, 3)}.txt") as letter:
            message = letter.read()
        message = message.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday\n\n{message}")
        
        


