import requests
import os
import datetime
exercise_endpoint = "NUTRITION_ENDPOINT"


API_ID = "YOUR ID"
API_KEY = "YOUR KEY"
AGE = "YOUR AGE"
GENDER = "YOUR GENDER"
WEIGHT = "YOUR WEIGHT IN KG"
HEIGHT = "YOUR HEIGHT IN CM"
USERNAME = "YOUR USERNAME"
PROJECT = "NAME OF PROJECT"
SHEETNAME = "NAME OF SHEET"

today = datetime.datetime.now()

current_date_day = today.strftime("%d")
current_date_month = today.strftime("%m")
current_date_year = today.strftime("%Y")

current_time = today.strftime("%X")

sheety_endpoint = "LINK TO SHEETY"

exercise_input = input("What exercise did you perform today? ")

activity_params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg":WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

headers = {
    "x-app-id":API_ID,
    "x-app-key": API_KEY

}

response = requests.post(url = exercise_endpoint, json = activity_params, headers = headers)
exercise_data = response.json()
print(exercise_data)

name = exercise_data['exercises'][0]['name']
duration = exercise_data['exercises'][0]['duration_min']
calories = exercise_data['exercises'][0]['nf_calories']

my_workout_params = {
    "workout":{'date':f"{current_date_day}/{current_date_month}/{current_date_year}",
               "time":f"{current_time}",
               'exercise':f"{name.upper()}",
               'duration':f"{duration}",
               'calories':f"{calories}"
               }
}

sheety_headers = {
    "Authorization": "YOUR AUTHORIZATION CODE"
    }

sheety_response = requests.post(url=sheety_endpoint, json = my_workout_params, headers = sheety_headers)
print(sheety_response)