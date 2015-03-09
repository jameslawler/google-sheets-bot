#formatter

class formatter:

    def format(self, message, synonym):
        return message.format(**synonym.getForFormatting())