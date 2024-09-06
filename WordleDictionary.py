from pypdf import PdfReader
import re
from unidecode import unidecode


class WordleDictionary():
    def __init__(self,filepath="./wordlist-big-latestUTF8.txt"):
        self.words=[]
        self.mostFrequentWords = []
        self.filepath = filepath
        self.get_words_from_txtdictionary()
        self.getMostUsedWordsPortuguese()
    

    def get_words_from_txtdictionary(self):
        # wordlist cortesia de https://natura.di.uminho.pt
        with open(self.filepath, 'r',encoding='utf-8') as file:
            for line in file:
                word = line.strip()
                if len(word) == 5:
                    if word[0].upper() != word[0]: # tirar nomes proprias
                        if not "-" in word:
                            self.words.append(word)
    
    
    def getMostUsedWordsPortuguese(self):
        reader = PdfReader("AFrequencyDictionary.pdf")
        frequentWords = []
        for page in reader.pages:
            texto = page.extract_text(extraction_mode="layout")
            pattern = r'\s{1}([a-zA-Z]{5})\s{1}'
            # Find all matches in the string
            matches = re.findall(pattern, texto)

            for match in matches:
                if unidecode(match).lower() in self.words and not match.lower() in frequentWords:
                    frequentWords.append(match.lower())

        self.mostFrequentWords = frequentWords
    

    def set_main_dicionario(self,wordsList):
        self.words = wordsList

    def get_words(self):
        return self.words
    
    def get_frequent_words(self):
        return self.mostFrequentWords