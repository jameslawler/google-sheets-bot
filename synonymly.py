# -*- coding: utf-8 -*-

import gaenv_lib
import gspread
import tweepy
from synonyms import synonyms
from messages import messages
from formatter import formatter
from audit import audit
from configuration import configuration

class synonymly:

	def __init__(self, name):
		self.name = name

	def getWord(self):
		print "Synonymity - English"
		print "Work in Progress"

		synonymsObj = synonyms()
		synonym = synonymsObj.random("English", "Beginner")

		messagesObj = messages()
		message = messagesObj.random("English")

		formatterObj = formatter()
		formattedMessage = formatterObj.format(message, synonym)

		config = configuration("config.ini")
		# The consumer keys can be found on your application's Details
		# page located at https://dev.twitter.com/apps (under "OAuth settings")
		consumer_key=config.getTwitterConsumerKey()
		consumer_secret=config.getTwitterConsumerSecret()

		# The access tokens can be found on your applications's Details
		# page located at https://dev.twitter.com/apps (located
		# under "Your access token")
		access_token=config.getTwitterAccessToken()
		access_token_secret=config.getTwitterAccessTokenSecret()

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.secure = True
		auth.set_access_token(access_token, access_token_secret)

		api = tweepy.API(auth)
		return (api.me().name)
		#twitter = twitterclient()
		#twitter.tweet(formattedMessage)

		#audit = audit()
		#audit.save("English", synonym, "Twitter", formattedMessage)

		#print "Finished"
		#return formattedMessage