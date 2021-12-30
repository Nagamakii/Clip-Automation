import requests
from requests import api
from requests.api import post
from requests.models import Response
import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

api = os.getenv('API')
token = os.getenv('TOKEN')

url = 'https://upload.giphy.com/v1/gifs'
api_key = {'api_key': api}
file = {'file': open('Test.mp4','rb')}

def upload():
    
    authorize = requests.post(url, data=api_key, files=file)
    print(authorize.status_code)
    format_data = authorize.json()

    id = format_data['data']

    url_id = id['id']

    gif_url = f'https://giphy.com/gifs/{url_id}'
    
    return gif_url

discord_url = upload()
print(discord_url)

@client.event
async def on_ready():
    await client.get_channel(869809254498979945).send(discord_url)
client.run(token)

if __name__ == "__main__":
    upload()