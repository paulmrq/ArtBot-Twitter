# Artbot-Twitter
## First Version of a Twitter Bot (@UneNuitEtoilee) using Twitter API and Tweepy.
The main idea was to build an easy going script able to post from a folder containing paintings, image as tweets. The script could be deployd on a web service in order to be fully automated ! (This bot is now hosted on a free EC2 AWS server since 17th of November 2021)
Bots make twitter a cooler place and permit also to see my favorite pieces of art each day on the app ! :)
Reminder: This is a 1.0.0, the code is very simple but efficient.

Some tasks for the future : 
- Host all images metadata on a database and the files on S3.

## Install venv with shell
Run shell script on a machine with python already installed:
```bash
./installtion.sh
```
## Run manually
Run manually the code after creating your environement 
```bash
python ./bot/bot.py
```
## Run with Docker
Build image:
```bash
docker build . -t artbot-twitter
```
Run:
```bash
docker run -it -e CONSUMER_KEY="your consumer key" \
 -e CONSUMER_SECRET="your consumer secret" \
 -e ACCESS_TOKEN="your access token" \
 -e ACCESS_TOKEN_SECRET="your token secret" \ artbot-twitter
```

## Install lib manually (venv/conda)
Install lib manually from requirements.txt on an env:
```bash
pip install -r requirements.txt
```
```bash
conda install --file requirements.txt
```

## Sources

https://realpython.com/twitter-bot-python-tweepy/
