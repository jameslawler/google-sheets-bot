#audit

import gspread
from datetime import datetime
from pytz import timezone
from configuration import configuration

class audit:

    def __init__(self):
        config = configuration("config.ini")
        self.botTimezone = config.getBotTimezone()
        self.googleUsername = config.getGoogleUsername()
        self.googlePassword = config.getGooglePassword()

    def save(self, fileName, sheetName, network, message):
        googleSheets = gspread.login(self.googleUsername, self.googlePassword)
        worksheet = googleSheets.open(fileName).worksheet("Audit")

        newRow = self.getAuditRow(sheetName, network, message)
        worksheet.append_row(newRow)

    def getAuditRow(self, sheetName, network, message):
        customTimeZone = timezone(self.botTimezone)
        now = datetime.now(customTimeZone)
        currentDateTimeString = now.strftime('%Y-%m-%d %H:%M:%S')

        return [  currentDateTimeString,
                  sheetName,
                  network,
                  message]
