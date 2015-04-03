#audit

import gspread
import datetime
import time
from configuration import configuration

class audit:

    def __init__(self):
        config = configuration("config.ini")
        self.googleUsername = config.getGoogleUsername()
        self.googlePassword = config.getGooglePassword()

    def save(self, level, language, synonym, network, message):
        googleSheets = gspread.login(self.googleUsername, self.googlePassword)
        worksheet = googleSheets.open(language).worksheet("Audit")

        newRow = self.getAuditRow(level, language, synonym, network, message)
        worksheet.append_row(newRow)

    def getAuditRow(self, level, language, synonym, network, message):
        now = datetime.datetime.now()
        currentDateTimeString = "%s-%s-%s %s:%s:%s" % (now.year, now.month, now.day, now.hour, now.minute, now.second)
        
        return [  currentDateTimeString,
                  level,
                  synonym.word,
                  synonym.synonym,
                  synonym.grammar,
                  synonym.level,
                  synonym.link,
                  network,
                  message]
