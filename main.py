import requests
from datetime import datetime
import os

#
# YOUR_USERNAME="YOUR USERNAME"
# YOUR_PASSWORD="YOUR PASSWORD"
GENDER = "female"
WEIGHT_KG = "50"
HEIGHT_CM = "170"
AGE = "18"
# APP_ID="APP ID"
# API_KEY="API KEY"

APP_ID=os.environ["APP_ID"]
API_KEY=os.environ["API_KEY"]
SHEETY=os.environ["SHEET_ENDPOINT"]
YOUR_USERNAME=os.environ["YOUR_USERNAME"]
YOUR_PASSWORD=os.environ["YOUR_PASSWORD"]

HEADERS={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "x-remote-user-id":"0",
}
# SHEETY="SHEETY LINK"

ex_endp="https://trackapi.nutritionix.com/v2/natural/exercise"
ex_t=input("What exercises did you do?")
ex_params={
    "query": ex_t,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response=requests.post(url=ex_endp, json=ex_params, headers=HEADERS)
result=response.json()
today=datetime.now()
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date":today.strftime("%d/%m/%Y"),
            "time":today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(SHEETY,json=sheet_inputs,auth=(YOUR_USERNAME,YOUR_PASSWORD,))