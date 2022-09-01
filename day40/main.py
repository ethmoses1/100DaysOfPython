#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flights = FlightSearch()
data = DataManager()
notification = NotificationManager()
FROM_CITY = "SYD"

print("Welcome to Angela's Flight Club")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n").lower()

email_confirmation = ""
while email != email_confirmation:
    email_confirmation = input("Type your email again\n").lower()

created_user = data.create_new_user(first_name, last_name, email)
print(created_user)

sheet_data = data.get_distination_prices()
#update sheety with City Codes
# for row in sheet_data:
#     city  = row['city']
#     code = flights.update_iatacode(city)
#     data.update_iata_code(row, code)

# for row in sheet_data:
#     available_flights  = flights.search_flight(row['iataCode'], row['lowestPrice'], frm=FROM_CITY)
#     if available_flights != -1:
#         message = available_flights.text_message_data()
#         notification.sms(message)

users = data.get_users()
for user in users:
    for row in sheet_data:
        available_flights  = flights.search_flight(row['iataCode'], row['lowestPrice'], frm=FROM_CITY)
        if available_flights != -1:
            message = available_flights.text_message_data()
            email = user['email']
            notification.email(email, message)
        
        
