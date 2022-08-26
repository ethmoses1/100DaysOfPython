import requests
from datetime import datetime
from decouple import config


APP_ID = config("APP_ID")
API_KEY = config("API_KEY")
exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = "https://api.sheety.co/1f1c1d89f2d7c9596f9802aeb72ed8e0/myWorkouts/workouts"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}
# Ran 2 miles and walked for 3km.
body = {
    "query": input("Tell me which exercises you did?: ")
}

response = requests.post(url=exercise_url, headers=header, json=body)
data = response.json()

headers_sheety = {
    "Authorization": f"Basic {config('basic_id')}=="
}
for item in data['exercises']:
    json_payload = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": item['name'].title(),
            "duration": item['duration_min'],
            "calories": item['nf_calories'],
            "id": 3
        }
    }
    response = requests.post(url=sheety_url,headers=headers_sheety, json=json_payload)
    print(response.json())
    

