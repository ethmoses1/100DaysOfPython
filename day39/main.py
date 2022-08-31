#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flights = FlightSearch()
data = DataManager()

sheet_data = data.get_distination_prices()

for row in sheet_data:
    city  = row['city']
    code = flights.update_iatacode(city)
    data.update_iata_code(row, code)

for row in sheet_data:
    available_flights  = flights.search_flight(row['iataCode'], row['lowestPrice'], frm="SYD")
    if available_flights != -1:
        message = available_flights.text_message_data()
        notify = NotificationManager(message)
