#synonyms

import gspread
from random import randint
from configuration import configuration
from synonym import synonym

class synonyms:

    def __init__(self):
        config = configuration("config.ini")
        self.googleUsername = config.getGoogleUsername()
        self.googlePassword = config.getGooglePassword()

    def random(self, language, page):
        googleSheets = gspread.login(self.googleUsername, self.googlePassword);
        worksheet = googleSheets.open(language).worksheet(page);
        synonyms = worksheet.get_all_values();

        numberOfSynonyms = len(synonyms) - 1
        headerSynonym = synonyms[0]
        randomSynonym = synonyms[randint(1,numberOfSynonyms)]

        synonymDictionary = {}
        for i in range(len(headerSynonym)):
            synonymDictionary[headerSynonym[i].lower()] = randomSynonym[i]

        return synonym(synonymDictionary)
