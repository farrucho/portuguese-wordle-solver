from WordleGameClass import WordleGame
from GameUI import MainWindow

from PyQt6.QtWidgets import QApplication
import sys


game = WordleGame("útero")

app = QApplication(sys.argv)

window = MainWindow(game)
window.show()

window.startGame()


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



# window.draw_grid_line(0)
