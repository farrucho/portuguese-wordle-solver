from WordleGameClass import WordleGame
from WordleDictionary import WordleDictionary
from BruteForceWordle import BruteForceWordle
import numpy as np
from unidecode import unidecode
import random

import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter



class Entropy():
    def __init__(self,wordleGame: WordleGame) -> None:
        self.game = wordleGame
        self.possibleWords = BruteForceWordle(self.game).getPossibleWords()

    def expected_value_information(self,word):
        # vamos experimentar inicialmente com starterword = "termo"
        colorCodes_data = []
        freq_data = []


        for possibleWord in self.possibleWords:
            game = WordleGame(secretWord=possibleWord,dicionario=self.game.getDicionario())
            game.guess_word(word)
            colorsInfo = str([str(colorCode) for colorCode in game.getAttempts()[-1][:,1]])
            if colorsInfo in colorCodes_data:
                freq_data[colorCodes_data.index(colorsInfo)] += 1
            else:
                colorCodes_data.append(colorsInfo)
                freq_data.append(1)

        total_freq = sum(freq_data)
        prob_data = list(np.array(freq_data)/total_freq)
        information_data = list(np.log2(prob_data))
        
        information_entropy = 0
        for index in range(0,len(colorCodes_data)):
            information_entropy += prob_data[index]*information_data[index]

        # plt.figure()            
        # plt.bar(colorCodes_data,np.log2(freq_data),align='center') # A bar chart
        # plt.xlabel('ColorCodes')
        # plt.ylabel('Frequency')
        # plt.show()
        

        return -float(information_entropy)

    
    def best_guess(self):
        entropy_data = []
        

        for index,palavra in enumerate(self.possibleWords):
            entropy_data.append([palavra,self.expected_value_information(palavra)])
            # print(f"{(index+1)*100/len(self.possibleWords)} %")
        
        entropy_data.sort(key=lambda x: x[1])
        entropy_data.reverse()


        # plt.figure()
        # plt.bar(np.array(entropy_data)[:,0],np.array(entropy_data)[:,1].astype(float),align='center') # A bar chart
        # plt.xlabel('Words Possible')
        # plt.ylabel('Expected Information')
        # plt.title("Wordle - Information Theory")
        # plt.xticks(rotation='vertical')
        # plt.show()


        # print(entropy_data[0][0])
        
        return entropy_data[0][0]
