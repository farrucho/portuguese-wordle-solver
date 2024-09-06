import numpy as np
from termcolor import colored, cprint
from unidecode import unidecode
from WordleDictionary import WordleDictionary

class WordleGame:
    def __init__(self, secretWord,dicionario=WordleDictionary()):
        self.secretWord = secretWord.upper()
        self.board = np.array([['',0],['',0],['',0],['',0],['',0]]) # (char,colorcode) 0-grey 1-yellow 2-green
        self.lifes = 6
        self.dicionario = dicionario
        self.window = None
        self.attempts = []

    def set_window(self,window):
        self.window = window


    def get_window(self):
        return self.window


    def play_game(self) -> None:
        while not self.isGameOver():
            wordTry = input("manda adivinha\n")
            self.guess_word(wordTry)
            self.printBoard()

        if self.isWin(): print("gg")


    def guess_word(self, word) -> bool: # bool caso word esteja noi dicionario
        # check if is valid word
        if unidecode(word).lower() in [unidecode(word) for word in self.dicionario.get_words()]:
            self.lifes = self.lifes - 1

            self.board[:,0] = list(self.dicionario.get_words()[
                [unidecode(word) for word in self.dicionario.get_words()].index(unidecode(word).lower())
                ] .upper()) # update board para meter acentos nas palavras automaticamente


            for index,char in enumerate(self.board[:,0]):
                if unidecode(char) in unidecode(self.secretWord):
                    if unidecode(char) == unidecode(self.secretWord[index]):
                        self.board[index,1] = '2'
                        continue
                    self.board[index,1] = '1'
                    continue
                self.board[index,1] = '0'
                continue
            # print(self.board)
            self.attempts.append(np.copy(self.board))
            return True
        return False


    def printBoard(self) -> None:
        colorDict = {
            '0':"grey",
            '1':"yellow",
            '2':"green"
        }

        for char,colorIndex in self.board:
            cprint(char, colorDict[colorIndex], end=" ")
        print("\n")


    def get_board(self):
        return self.board

    def getDicionario(self):
        return self.dicionario

    def getAttempts(self):
        return self.attempts

    def isGameOver(self) -> bool:
        return (''.join(map(str, self.board[:,0])) == self.secretWord or self.lifes == 0)


    def isWin(self) -> bool:
        return ''.join(map(str, self.board[:,0])) == self.secretWord
    
    def lifes(self) -> int:
        return self.lifes
    
