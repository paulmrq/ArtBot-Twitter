import tweepy
import datetime

consumer_key = 'UidrqCcspCl0mu5AllKOttCLA'
consumer_secret = 'MY8u643ysHcjWFVFs307P8ewGy2wo08TmPNrDg5FRUf9i6Cmmn'
access_token = '1595914962-T5qSVkOqT4hsAauizKPLq4cLw1BfpDxEOd4j8qz'
access_token_secret = 'LYln4GpnTNPr5CEgEaaUSvRjKQ8plbtAFwOnXDvbxG9g8'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

message = "Bot Twitter crée par Paul, image de shrek incomming......"
user = 754745347
shrek_image_url = 'images/shrek.png'
id = 1183337763724283905


for i in range(1):
    api.send_direct_message(user,message)