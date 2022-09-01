import requests
from datetime import datetime, timedelta
from flight_data import FlightData
from random import choice
from decouple import config


HEADER = {
    "apikey": config('apikey')
}
URL =  "https://tequila-api.kiwi.com"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass
    
    def search_flight(self,to, price_range, frm="SYD"):
        date = self.dates()
        date_from = date[0]
        date_to = date[1]
        query = {
            "curr": "AUD",
            "price_from": 0,
            "price_to": price_range
        }
        url = f"{URL}/v2/search?fly_from={frm}&fly_to={to}&dateFrom={date_from}&dateTo={date_to}"
        response = requests.get(url, headers=HEADER, params=query)
        
        flight_data = self.update_fligh_info(response.json()['data'])
        return flight_data


    def update_iatacode(self, cityname):
        query = {"term": cityname, "location_types": "city"}
        url = f"{URL}/locations/query"
        response = requests.get(url, headers=HEADER, params=query)
        data = response.json()['locations']
        cities  =["Melbourne","Brisbane","Hobart"]

        if cityname in cities:
            for item in data:
                country = item['country']['name']
                if country == "Australia":
                    return item['code']
        else:
            for item in data:
                if item['name'] == cityname:
                    return item['code']
    
    def dates(self):
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_formatted = tomorrow.strftime("%d/%m/%Y")

        future_day = tomorrow.day
        future_month = (tomorrow.month + 6) % 12
        future_year = tomorrow.year + ((tomorrow.month + 6) // 12)

        six_months_later = datetime(future_year, future_month, future_day).strftime("%d/%m/%Y")
        return [tomorrow_formatted, six_months_later]
    
    def update_fligh_info(self, datas):
        if len(datas) > 0:
            flight = choice(datas)
            flight_data = FlightData(flight['flyFrom'], flight['cityFrom'],flight['flyTo'], flight['cityTo'], flight['utc_departure'].split('T')[0], flight['price'], flight['deep_link'] )
            return flight_data
        return -1

            
