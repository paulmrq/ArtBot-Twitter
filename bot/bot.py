import os
from config import create_api
import json



try :
    with open('images/info.json', 'r') as f:
        file = json.load(f)
except:
    print("json not found !")

image_ID = file['images'][0]['imageID']
name = file['images'][0]['name']
author = file['images'][0]['author']
date = file['images'][0]['date']


message = f"{name} by {author},{date}"
api = create_api()
media = api.media_upload(f"images/{image_ID}.jpg")

api.update_status(status = message,media_ids=[media.media_id])
