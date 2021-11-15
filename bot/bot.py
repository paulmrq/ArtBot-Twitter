import os
from config import connect_twitter_api,connect_google_api
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
api = connect_twitter_api()
#media = api.media_upload(f"images/{image_ID}.jpg")

#api.update_status(status = message,media_ids=[media.media_id])



drive = connect_google_api()

# View all folders and file in your Google Drive
fileList = drive.ListFile({'q': "'1LeLvu0UDJyHf9WjIlk_pbQlBXGbsWqUS' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))

  # Get the folder ID that you want
  if(file['title'] == "To Share"):
      fileID = file['id']

#file2 = drive.CreateFile({'id': fileID})

media = api.media_upload(file)
print(media)
#api.update_status(status = message,media_ids=[media.media_id])

