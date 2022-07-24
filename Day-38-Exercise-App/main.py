import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = "77"
HEIGHT_CM = "164.5"
AGE = "28"
# Application_ID = os.environ.get("ID")
Application_ID = "f06a1158"
#"f06a1158"
# API_KEY = os.environ.get("API_KEY")
API_KEY = "2925bd8b480ae468bab1970f05beac36"
#2925bd8b480ae468bab1970f05beac36

Exercise_Endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/39fbc02e801a2073ba7218dbb94be15c/myWorkouts/workouts"
exercise_text = input("Tell me which exercises you did: ")

Exercise_params = {
 "query": exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE,
}
headers = {
    "x-app-id": Application_ID,
    "x-app-key": API_KEY
}

response = requests.post(Exercise_Endpoints, json=Exercise_params, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    sheet_response.raise_for_status()
    data = sheet_response.json()
    print(sheet_response.text)
