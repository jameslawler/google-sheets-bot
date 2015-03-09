#synonym

class synonym:

    def __init__(self, word, synonym, grammar, level, link):
        self.word = word
        self.synonym = synonym
        self.grammar = grammar
        self.level = level
        self.link = link

    def getForFormatting(self):
        return {'word': self.word, 'synonym': self.synonym, 'grammar': self.grammar, 'level': self.level, 'link': self.link}