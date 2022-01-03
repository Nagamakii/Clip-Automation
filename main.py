import requests
from requests import api
import discord
import os
from dotenv import load_dotenv

# Get enviornmental variables and establish connection with discord
load_dotenv()
client = discord.Client()

# Secret info
api = os.getenv('API')
token = os.getenv('TOKEN')

# Prep data for POST requests
url = 'https://upload.giphy.com/v1/gifs'
api_key = {'api_key': api}
file = {'file': open('Test.mp4','rb')}

# Post clip to GIPHY, and get link from JSON response
def upload():
    authorize = requests.post(url, data=api_key, files=file)
    print(authorize.status_code)
    format_data = authorize.json()

    id = format_data['data']

    url_id = id['id']

    gif_url = f'https://giphy.com/gifs/{url_id}'
    
    return gif_url

# idk man this looks dumb but whatever it works
discord_url = upload()
print(discord_url)

# Post link to discord
@client.event
async def on_ready():
    await client.get_channel(869809254498979945).send(discord_url)
client.run(token)

if __name__ == "__main__":
    upload()