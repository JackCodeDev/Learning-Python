import requests
from datetime import datetime
TOKEN = "o23jljsadsfdfipjop"
USERNAME = "jacknguyen"
pixela_endpoint = "https://pixe.la/v1/users"
ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_configs = {

    "id": ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response =requests.post(url=graph_endpoint, json=graph_configs, headers=headers)
# print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_creation_configs = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km you cycle today?: "),
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

response =requests.post(url=pixel_creation_endpoint, json=pixel_creation_configs, headers=headers)
print(response.text)

day_update = datetime(year=2022, month=7, day=24)
date_update = day_update.strftime("%Y%m%d")
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{date_update}"

pixel_update_configs = {
    "quantity": "20"
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
response =requests.put(url=pixel_update_endpoint, json=pixel_update_configs, headers=headers)
print(response.text)

day_delete = datetime(year=2022, month=7, day=23)
date_delete = day_delete.strftime("%Y%m%d")
print(date_delete)
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{date_delete}"

headers = {
    "X-USER-TOKEN": TOKEN,
}
response =requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
