import os
import tweepy
import logging

os.environ["CONSUMER_KEY"] = 'FL1CuSE5FLR7lzsrBMCj18DZ6'
os.environ["CONSUMER_SECRET"] = 'Z4rxGkf6JVt2YhcCVzT1Rc6IVM6uHAXmA2Jm2uqO0AxooIhdYf'
os.environ["ACCESS_TOKEN"] = '1460015666908606468-a8PUGya8Kx3y6JMMWUNPbkvHO5rRJk'
os.environ["ACCESS_TOKEN_SECRET"] = '7ptlNnwfA1RykRcDpEspwmcktnYwBqXyMKbeZUxmCVPHL'

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api