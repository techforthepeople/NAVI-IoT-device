from sense_hat import SenseHat
import json
import time
import requests
import os

sense = SenseHat()

sleep = lambda x: time.sleep(x / 1000.0)

high_temp_threshold = 40
low_temp_threshold = 0

api_url = 'https://navi-backend.onrender.com/api/log/2'

while True:

    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    sensor_data = {
        "temperature": str(round(temp)),
        "humidity": str(round(humidity)),
        "pressure": str(round(pressure))
        }

    api_post_data = json.dumps(sensor_data)

    response = requests.post(api_url, json=api_post_data)
    
    print("Data to POST to API: ", api_post_data)

    print("API response: ", response)
    
    if(temp > high_temp_threshold or temp < low_temp_threshold):
        os.system('warning.mp3')
        sense.show_message("HIGH", text_colour=[255,255,255], back_colour=[255,0,0])
    else:
        sense.show_message("OK", text_colour=[255,255,255], back_colour=[0,255,0])

    sleep(2000)
