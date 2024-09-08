from WordleGameClass import WordleGame
from WordleDictionary import WordleDictionary
import numpy as np
from unidecode import unidecode
import random

class BruteForceWordle:
    def __init__(self, wordleGame: WordleGame):
        self.game = wordleGame
        self.dicionario = self.game.getDicionario()


    def getPossibleWords(self) -> list:
        attempts = self.game.getAttempts()
        if len(attempts) == 0:
            return self.dicionario.get_words()
        else:
            possibleWordleSolution = [[] for _ in range(0,5)]
            # lista size 5 cada elemento tem os caracters obtidos com base na informacao jogada  
            # se elemento é numero significa que ja achou digito naquela posicao especifica
            
            yellowCharsAnalysed = []
            # keep track dos chars analisados
            
            notpossibleChars = []

            # este algoritmo analisa onde podem ou nao estar colocadas as letras amarelas 
            for attempt in attempts:
                for collumn,(letter,index) in enumerate(attempt):
                    if index == '0' and not letter in notpossibleChars: notpossibleChars.append(str(letter))
                    if index == '1':
                        if unidecode(str(letter)).lower() in yellowCharsAnalysed:
                            try: # pode ja ter sido removido por isso é que está o try
                                possibleWordleSolution[collumn].remove(str(letter).lower())
                            except:
                                pass
                        else:
                            for i in range(0,5):
                                if i != collumn and not letter in possibleWordleSolution[i]: # 2ª condicao: pode ja ter sido adicionada
                                    if len(possibleWordleSolution[i]) == 1:
                                        if not isinstance(possibleWordleSolution[i][0], int):
                                            possibleWordleSolution[i].append(str(letter).lower())
                                    else:
                                        possibleWordleSolution[i].append(str(letter).lower())
                            yellowCharsAnalysed.append(unidecode(str(letter)).lower())
                    if index == '2':
                        possibleWordleSolution[collumn] = [ord(str(letter))]

            # print(possibleWordleSolution)

            # get item indexes
            intIndexes = []
            for collumn,elem in enumerate(possibleWordleSolution):
                if len(elem) > 0: # pode haver tile sem informacao sobre letras
                    if type(elem[0]) is int: intIndexes.append(collumn)
            

            dicionario = self.dicionario.get_words()


            possibleWords = []
            for palavra in dicionario:
                # 1 - Verificar compatibilidade com as green tiles
                # 2 - Verificar compatibilidade com notPossibleChars
                # 3 - A palavra tem que ter as letras analisadas
                # 4 - Verificar compatiblidade com o possibleWordleSolution

                # 1
                lista = [unidecode(palavra[intIndex]).lower() == unidecode(chr(possibleWordleSolution[intIndex][0])).lower() for intIndex in intIndexes] # lista com booleans que confirmam se de facto a palavra tem nas green tiles o char certo
                
                # 2
                if all(lista) and len([1 for notChar in notpossibleChars if unidecode(notChar).lower() in unidecode(palavra).lower()]) == 0:
                    # 3
                    if len([1 for char in list(yellowCharsAnalysed+[unidecode(chr(possibleWordleSolution[intIndex][0])).lower() for intIndex in intIndexes]) if not unidecode(char).lower() in unidecode(palavra).lower()]) == 0:
                        # 4
                        if len([(col,char) for col,char in enumerate(palavra) if unidecode(char).lower() in yellowCharsAnalysed and not unidecode(char).lower() in possibleWordleSolution[col] and not col in intIndexes]) == 0: # ult condicao serve para skippar green tiles ja checkadas
                                if not palavra in [''.join(map(str, attempt[:,0])).lower() for attempt in attempts]:
                                    possibleWords.append(palavra)
            
            # print(possibleWords)

            return possibleWords


    def best_guess(self,possibleWords=""):
        # com base na informacao ja jogada manda guess bruteforce
        # para varias possiveis palavras escolhe as mais frequentes e manda word random

        attempts = self.game.getAttempts()
        if len(attempts) == 0:
            print("Starter Word ao calhas escolhida")
            return random.choice(self.game.getDicionario().get_frequent_words())


        possibleWords = self.getPossibleWords()

        mostProbableWords = [word for word in possibleWords if word in self.game.getDicionario().get_frequent_words() and word in possibleWords]

        # print(f"palavra secreta: {self.game.secretWord}")
        # print(f"todas as palavras possiveis: {possibleWords}")
        # print(f"palavras mais provaveis de ser: {mostProbableWords}")
        
        probabilities = mostProbableWords*80 + 20*possibleWords
        # tambem previne caso mostprobableword=[]
        # outra maneira seria com acesso a wordFreqCounts criar uma distribuição de probabilidade das palavras
        
        guess = random.choice(probabilities)

        while guess in [''.join(map(str, attempt[:,0])).lower() for attempt in attempts]:
            guess = random.choice(probabilities)
        
        # print(guess)
        return guess