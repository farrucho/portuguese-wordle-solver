from WordleGameClass import WordleGame
from BruteForceWordle import BruteForceWordle
from WordleDictionary import WordleDictionary
from EntropyWordle import Entropy
from GameUI import MainWindow
from PyQt6.QtWidgets import QApplication
import matplotlib.pyplot as plt
import numpy as np
import sys



# -----------------------
# USER PLAY NORMAL GAME
# -----------------------
# game = WordleGame("homem")
# app = QApplication(sys.argv)
# window = MainWindow(game)
# window.show()
# window.startGame()




# -----------------------
#   INFORMATION THEORY
#   (melhor algoritmo)
# -----------------------
# Aprender qual é a melhor starterWord com Information Theory (no wordle-wordlist.txt)
# o processo é igual para wordlist-big-latestUTF8.txt, mas é mais tedioso pois tem o dobro das palavras
# Para a wordlist wordle-wordlist.txt, a melhor palavra é rasto
# Pequena nota: 
#   -   apesar de já se notar numa wordlist com 1000 palavras que information theory é mais eficiente,
#       para wordlist maior, information theory tem +wins e em -tentativas


# dicionario = WordleDictionary(filepath="./wordle-wordlist.txt")
# dicionario.set_main_dicionario(dicionario.get_words())
# e = Entropy(dicionario)
# print(e.best_guess())



# Podemos comparar como funcionam os dois da seguinte maneira:
# app = QApplication(sys.argv)
# dicionario = WordleDictionary(filepath="./wordle-wordlist.txt")
# lista = dicionario.get_words()

# entropy_data = [['1',0],['2',0],['3',0],['4',0],['5',0],['6',0],['loss',0]]
# bruteforce_data = [['1',0],['2',0],['3',0],['4',0],['5',0],['6',0],['loss',0]]
# # [number of tries, wins]

# for index,answerWord in enumerate(lista):
#     game1 = WordleGame(answerWord,dicionario)
#     window_entropy = MainWindow(game1)
#     # window_entropy.show()
#     window_entropy.setWindowTitle("ENTROPY")
#     window_entropy.startGameWithEntropyAlgorithm(timer=1000)
#     # window_entropy.close()

#     game2 = WordleGame(answerWord,dicionario)
#     window_bruteforce = MainWindow(game2)
#     # window_bruteforce.show()
#     window_bruteforce.setWindowTitle("BRUTE FORCE")
#     window_bruteforce.startGameWithBruteForceAlgorithm(timer=0)
#     # window_bruteforce.close()
    
#     if game1.isWin(): entropy_data[6-game1.lifes-1][1] += 1 
#     elif game1.isLoss():
#         print(game1.secretWord)
#         entropy_data[6][1] += 1
    
    
#     if game2.isWin(): bruteforce_data[6-game1.lifes-1][1] += 1
#     elif game2.isLoss(): bruteforce_data[6][1] += 1
    
#     print(f"{100*(index+1)/len(lista)} %")



# plt.figure()
# plt.bar(np.array(entropy_data)[:,0],np.array(entropy_data)[:,1].astype(int),align='center')
# plt.xlabel('Number of Tries')
# plt.ylabel('Win Frequency')
# plt.title("Wordle Information Theory Média de Tentativas: " + str((int(entropy_data[0][0])*int(entropy_data[0][1])+int(entropy_data[1][0])*int(entropy_data[1][1])+int(entropy_data[2][0])*int(entropy_data[2][1])+int(entropy_data[3][0])*int(entropy_data[3][1])+int(entropy_data[4][0])*int(entropy_data[4][1])+int(entropy_data[5][0])*int(entropy_data[5][1]))/len(lista)))
# plt.show()


# plt.figure()
# plt.bar(np.array(bruteforce_data)[:,0],np.array(bruteforce_data)[:,1].astype(int),align='center')
# plt.xlabel('Number of Tries')
# plt.ylabel('Win Frequency')
# plt.title("Wordle Brute Force: Média de Tentativas: " + str((int(bruteforce_data[0][0])*int(bruteforce_data[0][1])+int(bruteforce_data[1][0])*int(bruteforce_data[1][1])+int(bruteforce_data[2][0])*int(bruteforce_data[2][1])+int(bruteforce_data[3][0])*int(bruteforce_data[3][1])+int(bruteforce_data[4][0])*int(bruteforce_data[4][1])+int(bruteforce_data[5][0])*int(bruteforce_data[5][1]))/len(lista)))
# plt.show()

# >>> print(entropy_data) 
# [['1', 1], ['2', 123], ['3', 543], ['4', 278], ['5', 33], ['6', 6], ['loss', 0]]
# >>> print(bruteforce_data) 
# [['1', 1], ['2', 123], ['3', 543], ['4', 273], ['5', 32], ['6', 6], ['loss', 6]]





# --------------------------------------------------------
# BRUTE-FORCE SOLVING WORDLE REAL TIME ALL POSIBILITIES:
# --------------------------------------------------------
# O algoritmo brute-force funciona com base em:
# -     As palavras resposta/tentaiva possíveis podem ser todas as palavras da língua portuguesa ou apenas as mais frequentes,
#       cabe ao jogador decidir aquando inicialização do loop
# Aqui considera-se:
# -     tentativas ∈ todas as palavras possíveis portuguesas
# -     palavra secreta ∈ palavras mais comuns portuguesas
# isto é o jogador nao sabe que palavras podem aparecer no jogo


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
#             window.startGameWithAlgorithm(BruteForceWordle(game),startingWord,timer=1000)
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
