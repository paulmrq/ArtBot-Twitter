# Artbot-Twitter
## First Version of a Twitter Bot (@UneNuitEtoilee) using Twitter API and Tweepy.
The main idea was to build an easy going script able to post from a folder containing paintings, image as tweets. The script could be deployd on a web service in order to be fully automated !
Bots make twitter a cooler place and permit also to see my favorites piece of art each day on the app ! :)
Reminder: This is a 1.0.0, the code is very simple but efficient.

Some tasks for the future : 
- Host all the images on a database.
- Deploy the bot on AWS.

## Install venv with shell
Run shell script on a machine with python already installed:
```bash
./installtion.sh
```

## Run with Docker
Build image:
```bash
docker build . -t artbot-twitter
```
Run:
```bash
docker run artbot-twitter
```

## Install lib manually (venv/conda)
Install lib manually from requirements.txt on an env:
```bash
pip install -r requirements.txt
```
```bash
conda install --file requirements.txt
```
