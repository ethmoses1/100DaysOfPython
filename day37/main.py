from datetime import datetime
import requests
from decouple import config
username = config("username")
token = config("token")
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)


graph_endpoint =f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
    }

headers = {
    "X-USER-TOKEN": token
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers
# )


today = datetime.now()
# new_date = ''.join(str(today).split('-'))
single_pixel_endpoint = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?: "),
    "id": "graph1",
    
}
response = requests.post(url=f"{graph_endpoint}/graph1", json=single_pixel_endpoint, headers=headers)


update_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)


delete_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1/{today.strftime('%Y%m%d')}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
