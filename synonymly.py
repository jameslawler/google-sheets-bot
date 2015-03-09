# -*- coding: utf-8 -*-

import gspread
from synonyms import synonyms
from messages import messages
from formatter import formatter
from twitterclient import twitterclient
from audit import audit

class synonymly:

    def getWord(self):
		print "Synonymity - English"
		print "Work in Progress"

		synonyms = synonyms()
		synonym = synonyms.random("English", "Beginner")

		messages = messages()
		message = messages.random("English")

		formatter = formatter()
		formattedMessage = formatter.format(message, synonym)

		#twitter = twitterclient()
		#twitter.tweet(formattedMessage)

		#audit = audit()
		#audit.save("English", synonym, "Twitter", formattedMessage)

		print "Finished"
		return formattedMessage

