#twitterclient

import twitter
from configuration import configuration

class twitterclient:

    def __init__(self):
        config = configuration("config.ini")
        self.api = twitter.Api(consumer_key=config.getTwitterConsumerKey(),
                      consumer_secret=config.getTwitterConsumerSecret(),
                      access_token_key=config.getTwitterAccessToken(),
                      access_token_secret=config.getTwitterAccessTokenSecret())

    def tweet(self, message):
        self.api.PostUpdate(message)