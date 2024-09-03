from WordleGameClass import WordleGame
from GameUI import MainWindow

from PyQt6.QtWidgets import QApplication
import sys

#game = WordleGame("homem")
# game = WordleGame("moeda")


# game.guess_word("termo")
# game.printBoard()
# game.guess_word("moeda")
# game.printBoard() 
# game.guess_word("comes")
# game.printBoard() 
# game.guess_word("tomei")
# game.printBoard()
# game.guess_word("homem")
# game.printBoard()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

