import requests
from requests import api
import os
from dotenv import load_dotenv
import moviepy.editor
import discord

# Get enviornmental variables and establish connection with discord
load_dotenv()
user_file = input("File: ").strip('"')
client = discord.Client()

# Secret info
api = os.getenv('API')
token = os.getenv('TOKEN')

# Prep data for POST requests
giphy_url = 'https://upload.giphy.com/v1/gifs'
api_key = {
    'api_key': api
    }
file = {
    'file': open(user_file,'rb')
    }

# Post clip to GIPHY, format response to get link, and send in discord
def main():
    video = moviepy.editor.VideoFileClip(user_file)
    vid_len = int(video.duration)
    if vid_len > 15:
        print("GIPHY only allows for 15sec clips, please clip to under 15 until a better solution is found.")
        quit()
    else:
        print('Clip is good!')
        print('Uploading and Encoding...')
        gif_upload = requests.post(
            giphy_url, data=api_key, files=file
            )
        print(gif_upload.status_code, gif_upload.text)
        
        format_data = gif_upload.json()
        id = format_data['data']
        url_id = id['id']
        gif_url = f'https://giphy.com/gifs/{url_id}'
    
        print('Posting Message...')
        @client.event
        async def on_ready():
            await client.get_channel(815836813221822475).send(gif_url)
        client.run(token)
        
if __name__ == "__main__":
    main()
