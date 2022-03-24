from discord import Webhook, RequestsWebhookAdapter
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from dotenv import load_dotenv
import moviepy.editor
import requests
import time
import os

load_dotenv() # Get enviornmental variables and establish connection with discord

api = os.getenv('API')  # Secret info
wh = os.getenv('WEBHOOK')
path = ("Z:\pi-clips")

class Exeventhandler(FileSystemEventHandler):   # Establish event handler
    def on_created(self, event):
        main(event.src_path)

def main(file): # Post clip to GIPHY, format JSON response to get link, and send in discord
    
    # Prep data for POST requests
    giphy_url = 'https://upload.giphy.com/v1/gifs'
    api_key = {'api_key': api}
    upload_file = {'file': open(file,'rb')}
    
    # Check video length
    video = moviepy.editor.VideoFileClip(file)
    vid_len = int(video.duration)
    
    if vid_len > 15:
        print("GIPHY only allows for 15sec clips, please clip to under 15 until a better solution is found.")
    else:
        print('Clip is good!')
        print('Uploading and Encoding...')
        gif_upload = requests.post(giphy_url, data=api_key, files=upload_file)
        print(gif_upload.status_code)
        
        format_data = gif_upload.json()
        id = format_data['data']
        url_id = id['id']
        gif_url = f'https://giphy.com/gifs/{url_id}'
    
        print('Posting Message...')
        Webhook.from_url(wh, adapter=RequestsWebhookAdapter()).send(gif_url, username='Clip Bot')

if __name__ == "__main__":
    observer = Observer()
    event_handler = Exeventhandler() # create event handler
    
    # set observer to use created handler in directory
    observer.schedule(event_handler, path=path)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()