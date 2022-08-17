from email import message
from multiprocessing import connection
import smtplib
from decouple import config
import datetime as dt
from random import choice

my_email = config('EMAIL')
my_pass = config('PASSWORD')


#datetime
now = dt.datetime.now()
day = now.weekday()

if day == 2:
    with open("quotes.txt") as data_file:
        quotes_list = data_file.readlines()
        single_quote = choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs="mosesbuta123@gmail.com", msg=f"Subject:Inspirational quote for today\n\n{single_quote}")




