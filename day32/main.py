from email import message
from multiprocessing import connection
import smtplib
from decouple import config
import datetime as dt
from random import choice

my_email = config('EMAIL')
my_pass = config('PASSWORD')


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(from_addr=my_email, to_addrs="mosesbuta123@gmail.com", msg=f"Subject:hello\n\nHello Bro")




