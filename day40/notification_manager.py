from decouple import config
from smtplib import SMTP
my_email = config('EMAIL')
my_pass = config('PASSWORD')
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass
    def sms(self, message):
        from twilio.rest import Client 
        account_sid = config('account_sid')
        auth_token = config('auth_token') 
        client = Client(account_sid, auth_token) 
        
        message = client.messages.create(from_= "+13862309305",        
                                    to='+61401915591', body=message
                                ) 
        print(message.sid)
    
    def email(self, email, message):
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Hot cheap flight deals🔥\n\n{message}".encode('utf-8'))
