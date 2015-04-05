#bot

from data import data
from messages import messages
from formatter import formatter
from audit import audit
from twitterclient import twitterclient

class bot:

    def __init__(self, fileName, sheetName):
        self.fileName = fileName
        self.sheetName = sheetName

    def run(self):       
        dataObj = data()
        messageData = dataObj.getRandom(self.fileName, self.sheetName)

        messagesObj = messages()
        messageTemplate = messagesObj.getRandom(self.fileName)

        formatterObj = formatter()
        formattedMessage = formatterObj.format(messageTemplate, messageData)

        twitter = twitterclient()
        twitter.tweet(formattedMessage)

        auditObj = audit()
        auditObj.save(self.fileName, self.sheetName, "Twitter", formattedMessage)
