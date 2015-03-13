#synonymly

import gaenv_lib
from synonyms import synonyms
from messages import messages
from formatter import formatter
from audit import audit
from twitterclient import twitterclient

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
		
        twitter = twitterclient()
        twitter.tweet(formattedMessage)

        auditObj = audit()
        auditObj.save("English", synonym, "Twitter", formattedMessage)

        print "Finished"
