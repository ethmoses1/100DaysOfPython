import requests
from decouple import config
SHEETY_URL = "https://api.sheety.co/1f1c1d89f2d7c9596f9802aeb72ed8e0/flightDeals/prices"
SHEETY_URL_USER = "https://api.sheety.co/1f1c1d89f2d7c9596f9802aeb72ed8e0/flightDeals/users"
HEADER = {
    "Authorization": f"Basic {config('authorization')}="
}
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass
    
    def get_distination_prices(self):
        response = requests.get(SHEETY_URL, headers=HEADER)
        return response.json()['prices']
    
    def update_iata_code(self, row, code):
        body = {
            "price": {
                'city': row['city'],
                'iataCode': code,
                'lowestPrice': row['lowestPrice'],
                'id': row['id']
            }
        }
        url = f"{SHEETY_URL}/{row['id']}"
        reponse = requests.put(url=url, headers=HEADER,json=body )
        print(reponse.text)
        
    def get_users(self):
        res = requests.get(url=SHEETY_URL_USER, headers=HEADER)
        return res.json()['users']
        
    def create_new_user(self, fname, lname, email):
        
        res = requests.get(url=SHEETY_URL_USER, headers=HEADER)
        for user in res.json()['users']:
            if user['email'] == email:
                return "Email already exists"
        else:
            body = {
                "user":{
                    "firstName": fname,
                    "lastName": lname,
                    "email": email
                }
            }
            response = requests.post(url=SHEETY_URL_USER, headers=HEADER, json=body)
            if response.status_code == 200:
                return "Your in the club!"
            else:
                return -1