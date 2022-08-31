class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, departure_airport_code, departure_city, arrival_airport_code, arrival_airport_city, local_departure, price):
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.arrival_airport_code = arrival_airport_code
        self.arrival_airport_city = arrival_airport_city
        self.local_departure = local_departure
        self.price = price
    def text_message_data(self):
        data = f"Cheap Flight\n\nDate: {self.local_departure}\nPrice: ${self.price} AUD\nFrom: {self.departure_city}({self.departure_airport_code}) - {self.arrival_airport_city}({self.arrival_airport_code})"
        return data
    
    

