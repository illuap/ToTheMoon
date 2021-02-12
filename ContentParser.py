import csv
import re

class ContentParser(object):
    banned_words = [';', ':', '!', "*", ".","$"]
    def __init__(self):
        with open('banned_words.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                self.banned_words.append(row[0])

    def get_clean_sentence(self, sentence: str):
        # Remove characters and don't leave spaces
        for ch in self.banned_words:
            sentence = sentence.replace(ch, '')
        # for ch in space_chars:
        #     sentence = sentence.replace(ch, ' ')

        sentence = re.sub(r'[^\w\s]',' ',sentence)

        return sentence 