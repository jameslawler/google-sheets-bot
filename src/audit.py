#audit

import gspread
from datetime import datetime
from pytz import timezone
from configuration import configuration

class audit:

    def __init__(self):
        config = configuration("config.ini")
        self.synonymlyTimezone = config.getSynonymlyTimezone()
        self.googleUsername = config.getGoogleUsername()
        self.googlePassword = config.getGooglePassword()

    def save(self, level, language, synonym, network, message):
        googleSheets = gspread.login(self.googleUsername, self.googlePassword)
        worksheet = googleSheets.open(language).worksheet("Audit")

        newRow = self.getAuditRow(level, language, synonym, network, message)
        worksheet.append_row(newRow)

    def getAuditRow(self, level, language, synonym, network, message):
        customTimeZone = timezone(self.synonymlyTimezone)
        now = datetime.now(customTimeZone)
        currentDateTimeString = now.strftime('%Y-%m-%d %H:%M:%S')

        return [  currentDateTimeString,
                  level,
                  synonym.word,
                  synonym.synonym,
                  synonym.grammar,
                  synonym.level,
                  synonym.link,
                  network,
                  message]
