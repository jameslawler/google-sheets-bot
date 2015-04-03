#messages

import gspread
from random import randint
from configuration import configuration

class messages:

    def __init__(self):
        config = configuration("config.ini")
        self.googleUsername = config.getGoogleUsername()
        self.googlePassword = config.getGooglePassword()

    def random(self, language):
        googleSheets = gspread.login(self.googleUsername, self.googlePassword);
        worksheet = googleSheets.open(language).worksheet("Messages");
        messages = worksheet.get_all_values();

        numberOfMessages = len(messages) - 1
        randomMessage = messages[randint(1,numberOfMessages)]

        return randomMessage[0]