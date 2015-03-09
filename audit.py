#audit

import gspread
import datetime
from configuration import configuration

class audit:

    def __init__(self):
        config = configuration("config.ini")
        self.googleUsername = config.getGoogleUsername()
        self.googlePassword = config.getGooglePassword()

    def save(self, language, synonym, network, message):
        googleSheets = gspread.login(self.googleUsername, self.googlePassword);
        worksheet = googleSheets.open(language).worksheet("Audit");
        audits = worksheet.get_all_values();
        newAuditRow = len(audits) + 1

        d = datetime.datetime.now()
        currentDateTimeString = "%s-%s-%s %s:%s:%s" % (d.year, d.month, d.day, d.hour, d.minute, d.second)
        worksheet.update_cell(newAuditRow, 1, currentDateTimeString)
        worksheet.update_cell(newAuditRow, 2, "Beginner")
        worksheet.update_cell(newAuditRow, 3, synonym.word)
        worksheet.update_cell(newAuditRow, 4, synonym.synonym)
        worksheet.update_cell(newAuditRow, 5, synonym.grammar)
        worksheet.update_cell(newAuditRow, 6, synonym.level)
        worksheet.update_cell(newAuditRow, 7, synonym.link)
        worksheet.update_cell(newAuditRow, 8, network)
        worksheet.update_cell(newAuditRow, 9, message)