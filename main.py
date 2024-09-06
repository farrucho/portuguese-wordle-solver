from WordleGameClass import WordleGame
from BruteForceWordle import BruteForceWordle
from GameUI import MainWindow
from WordleDictionary import WordleDictionary
from PyQt6.QtWidgets import QApplication
import sys

# -----------------------
# USER PLAY NORMAL GAME
# -----------------------
 
# game = WordleGame("homem")
# app = QApplication(sys.argv)
# window = MainWindow(game)
# window.show()
# window.startGame()




# --------------------------------------------------------
# BRUTE-FORCE SOLVING WORDLE REAL TIME ALL POSIBILITIES:
# --------------------------------------------------------

# dicionario = WordleDictionary(filepath="./wordlist-big-latestUTF8.txt")
# dicionarioLista = dicionario.get_words()
# dicionarioMoreCommonWords = dicionario.get_frequent_words() # usar palavras mais comuns como answers do jogo

# gameWordsFreq = [[word,0,0] for word in dicionarioLista] # lista com freq de jogos ganhos por palavra inicial
#                 # [palavra, wins, media tentativas por win]
#                 # é obvio que a media é muito grande para win=1, mas isto é criterio de comparacao para os que tem maior numero de wins
#                 # muito tedioso, aconselhável rodar com dicionarioLista[0:40]

# NTIMESLOOPGAMES = 1

# print(f"comecando treino em {len(dicionarioLista)} palavras")
# print(f"jogos treinados por palavra:{len(dicionarioMoreCommonWords)*NTIMESLOOPGAMES}")
# app = QApplication(sys.argv)
# for index,startingWord in enumerate(dicionarioLista):
#     for index2,answerWord in enumerate(dicionarioMoreCommonWords):
#         for j in range(0,NTIMESLOOPGAMES):
#             game = WordleGame(answerWord,dicionario)
#             window = MainWindow(game)
#             window.show()
#             window.startBruteForceGame(startingWord,timer=1000)
#             window.close()
#             if game.isWin():
#                 gameWordsFreq[index][1] += 1
#                 gameWordsFreq[index][2] += 6-game.lifes
#             else:
#                 print(f"loss {game.getAttempts()} {game.secretWord}")
#             del game
#     print(f"{100*(index+1)/(len(dicionarioLista))} %")

# gameWordsFreq.sort(key=lambda x: (x[1], x[2]))
# gameWordsFreq.reverse()
# gameWordsFreq = [[elem[0],elem[1],elem[2]/elem[1]] for elem in gameWordsFreq]
# print(gameWordsFreq)
