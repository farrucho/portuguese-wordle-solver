import numpy as np
from termcolor import colored, cprint

class WordleGame:
    def __init__(self, secretWord):
        self.secretWord = secretWord
        self.board = np.array([['',0],['',0],['',0],['',0],['',0]]) # (char,colorcode) 0-grey 1-yellow 2-green
        self.lifes = 6

    

    def play_game(self) -> None: # true se ganhou falso se perdeu
        print("◻ ◻ ◻ ◻ ◻")
        
        while not self.isGameOver():
            wordTry = input("manda adivinha\n")
            self.guess_word(wordTry)
            self.printBoard()
            self.lifes = self.lifes - 1

        if self.isWin(): print("gg")



    def guess_word(self, word) -> None:
        self.board[:,0] = list(word)
        for index,char in enumerate(self.board[:,0]):
            if char in self.secretWord:
                if char == self.secretWord[index]:
                    self.board[index,1] = '2'
                    continue
                self.board[index,1] = '1'
                continue
            self.board[index,1] = '0'
            continue



    # game booleans and get properties:
    def printBoard(self) -> None:
        colorDict = {
            '0':"grey",
            '1':"yellow",
            '2':"green"
        }

        for char,colorIndex in self.board:
            cprint(char, colorDict[colorIndex], end=" ")
        print("\n")


    def isGameOver(self) -> bool:
        return (''.join(map(str, self.board[:,0])) == self.secretWord or self.lifes == 0)

    def isWin(self) -> bool:
        return ''.join(map(str, self.board[:,0])) == self.secretWord