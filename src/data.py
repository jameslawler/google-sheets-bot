#data

import gspread
from random import randint
from configuration import configuration

class data:

    def __init__(self):
        config = configuration("config.ini")
        self.googleUsername = config.getGoogleUsername()
        self.googlePassword = config.getGooglePassword()

    def getRandom(self, fileName, sheetName):
        googleSheets = gspread.login(self.googleUsername, self.googlePassword);
        worksheet = googleSheets.open(fileName).worksheet(sheetName);
        rows = worksheet.get_all_values();

        numberOfRows = len(rows) - 1
        header = rows[0]
        row = rows[randint(1,numberOfRows)]

        data = {}
        for i in range(len(header)):
            data[header[i].lower()] = row[i]

        return data
