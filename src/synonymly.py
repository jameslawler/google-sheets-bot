#synonymly

from synonyms import synonyms
from messages import messages
from formatter import formatter
from audit import audit
from twitterclient import twitterclient

class synonymly:

    def __init__(self, language, level):
        self.language = language
        self.level = level

    def run(self):       
        synonymsObj = synonyms()
        synonym = synonymsObj.random(self.language, self.level)

        messagesObj = messages()
        message = messagesObj.random(self.language)

        formatterObj = formatter()
        formattedMessage = formatterObj.format(message, synonym)

        twitter = twitterclient()
        twitter.tweet(formattedMessage)

        auditObj = audit()
        auditObj.save(self.level, self.language, synonym, "Twitter", formattedMessage)
