#twitterclient

import tweepy
from configuration import configuration

class twitterclient:

    def __init__(self):
        config = configuration("config.ini")

        auth = tweepy.OAuthHandler(config.getTwitterConsumerKey(), config.getTwitterConsumerSecret())
        auth.secure = True
        auth.set_access_token(config.getTwitterAccessToken(), config.getTwitterAccessTokenSecret())

        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(message)
