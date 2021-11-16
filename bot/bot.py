import os
from config import connect_twitter_api, connect_google_api
import json
import logging
import re
import time

""" 
    This work plans to create a bot for Twitter @UneNuitEtoilee posting art images each day at a certain frequency 
    from a source folder ./images/
"""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def process_string(file):
    """format string Name - Author - Date - Info"""
    file = re.sub(r'(.png|.jpg|.jpeg|.JPG)', '', file)
    string = str(file).split("-")
    name = string[0].replace("_", " ").strip()
    author = string[1].replace("_", " ").strip()
    try:
        date = string[2].replace("_", " ").strip()
    except:
        date = 'date unknown'

    return author, name, date


def gdrive_method():
    drive = connect_google_api()

    # View all folders and file in your Google Drive
    fileList = drive.ListFile({'q': "'1LeLvu0UDJyHf9WjIlk_pbQlBXGbsWqUS' in parents and trashed=false"}).GetList()
    for file in fileList:
        print('Title: %s, ID: %s' % (file['title'], file['id']))

        # Get the folder ID that you want
        if file['title'] == "To Share":
            fileID = file['id']


def fill_json():
    data = {}
    data['Paintings'] = []

    for root, dirs, files in os.walk('./images'):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                (author, name, date) = process_string(file)
                data['Paintings'].append({
                    "author": author,
                    "name": name,
                    "date": date,
                    "file": file
                })
            elif file.lower().endswith(('.json')):
                pass
            else:
                logging.error(file + 'not an image format !')

    with open('./images/info.json', 'w') as outfile:
        json.dump(data, outfile)
        logger.info("Json Updated")


def main():
    api = connect_twitter_api()
    fill_json()

    while True:
        try:
            with open('./images/info.json', 'r') as f:
                file = json.load(f)
        except:
            logger.critical("Json not found !")

        for i in range(len(file['Paintings'])):
            name = file['Paintings'][i]['name']
            author = file['Paintings'][i]['author']
            date = file['Paintings'][i]['date']
            source = file['Paintings'][i]['file']

            if len(date) == 4:
                message = f"{name} par {author}, {date}"
            else:
                message = f"{name} par {author}"

            media = api.media_upload(f"images/{source}")
            api.update_status(status=message, media_ids=[media.media_id])
            logger.info(f"{source} upload on twitter at")

            time.sleep(60)

        logger.info("All images are upload")


if __name__ == "__main__":
    main()
