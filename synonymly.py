# -*- coding: utf-8 -*-

import gaenv_lib
import gspread
from synonyms import synonyms
from messages import messages
from formatter import formatter
from audit import audit

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

		#twitter = twitterclient()
		#twitter.tweet(formattedMessage)

		#audit = audit()
		#audit.save("English", synonym, "Twitter", formattedMessage)

		print "Finished"
		return formattedMessage