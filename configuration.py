#configuration

import ConfigParser

class configuration:

	def __init__(self, configurationFilePath):
		self.config = ConfigParser.ConfigParser()
		self.config.read(configurationFilePath)

	def getGoogleUsername(self):
		return self.config.get("Google", "Username")	

	def getGooglePassword(self):
		return self.config.get("Google", "Password")

	def getTwitterConsumerKey(self):
		return self.config.get("Twitter", "ConsumerKey")

	def getTwitterConsumerSecret(self):
		return self.config.get("Twitter", "ConsumerSecret")

	def getTwitterAccessToken(self):
		return self.config.get("Twitter", "AccessToken")

	def getTwitterAccessTokenSecret(self):
		return self.config.get("Twitter", "AccessTokenSecret")