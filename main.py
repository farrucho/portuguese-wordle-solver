from WordleGameClass import WordleGame
from BruteForceWordle import BruteForceWordle
from WordleDictionary import WordleDictionary
from EntropyWordle import Entropy
from GameUI import MainWindow
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


# -----------------------
#   INFORMATION THEORY
#   (melhor algoritmo)
# -----------------------

# Aprender qual é a melhor starterWord com Information Theory (no wordle-wordlist.txt)
# o processo é igual para wordlist-big-latestUTF8.txt, mas é mais tedioso pois tem o dobro das palavras
# A MELHOR PALAVRA É RASTO
# dicionario = WordleDictionary(filepath="./wordle-wordlist.txt")
# dicionario.set_main_dicionario(dicionario.get_words())
# e = Entropy(dicionario)
# print(e.best_guess())



# Podemos comparar como funcionam os dois da seguinte maneira:

app = QApplication(sys.argv)
dicionario = WordleDictionary(filepath="./wordlist-big-latestUTF8.txt")
lista = dicionario.get_words()

for answerWord in lista[5:10]:
    game = WordleGame(answerWord,dicionario)
    window_entropy = MainWindow(game)
    window_entropy.show()
    window_entropy.setWindowTitle("ENTROPY")
    window_entropy.startGameWithEntropyAlgorithm(timer=2000)
    # window_entropy.close()
    game = WordleGame(answerWord,dicionario)
    window_bruteforce = MainWindow(game)
    window_bruteforce.show()
    window_bruteforce.setWindowTitle("BRUTE FORCE")
    window_bruteforce.startGameWithBruteForceAlgorithm(timer=2000)
    del game
    del window_entropy






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
