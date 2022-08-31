import requests
from decouple import config
SHEETY_URL = "https://api.sheety.co/1f1c1d89f2d7c9596f9802aeb72ed8e0/flightDeals/prices"
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