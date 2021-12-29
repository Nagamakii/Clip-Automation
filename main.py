import requests
import json

url = 'https://upload.giphy.com/v1/gifs'
data = {'api_key': 'apikey'}


file = {'file': open('Test.mp4','rb')}
authorize = requests.post(url, data=data)
storage = authorize.json()