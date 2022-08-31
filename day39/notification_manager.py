from decouple import config
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, message):
        from twilio.rest import Client 
        account_sid = config('account_sid')
        auth_token = config('auth_token') 
        client = Client(account_sid, auth_token) 
        
        message = client.messages.create(from_= "+13862309305",        
                                    to='+61401915591', body=message
                                ) 
        print(message.sid)
