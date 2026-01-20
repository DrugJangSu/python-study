import requests
import os
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 90
HEIGHT_CM = 180
AGE = 29

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = "https://api.sheety.co/55cc5b5daded5bc769b5946eadc2882f/myWorkouts(day38)/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

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

    sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs,
    auth=(
        USERNAME,
        PASSWORD,
        )
    )

    print(sheet_response.text)
