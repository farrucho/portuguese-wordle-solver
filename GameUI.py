from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow,QVBoxLayout, QWidget, QLabel,QHBoxLayout,QPlainTextEdit,QFrame,QTextEdit,QGridLayout
from WordleGameClass import WordleGame
import numpy as np

class LimitedPlainTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)

    def keyPressEvent(self, event):
        if len(self.toPlainText()) < 1 or event.key() in [QtCore.Qt.Key.Key_Backspace, QtCore.Qt.Key.Key_Delete]:
            # super().keyPressEvent(event)
            event.ignore()
        else:
            event.ignore()
    
    
    # meter primeiro teclado funcional or len(self.textCursor().selectedText())>0
    def mouseDoubleClickEvent(self, event):
        event.ignore()

    def mouseReleaseEvent(self, event):
        event.ignore()

    def mouseMoveEvent(self, event):
        event.ignore()

    def mousePressEvent(self, event):
        event.ignore()


class SquareTileWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MainWindow(QMainWindow):
    def __init__(self, wordleGame: WordleGame):
        super().__init__()
        self.setWindowTitle("Wave Main Window")
        self.setFixedWidth(525)
        self.setFixedHeight(650)
        self.setStyleSheet("background-color: #6e5c62; font-family: 'Helvetica Neue';") # font-family: 'Clear Sans', 'Helvetica Neue', Arial, sans-serif;")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget) 
        
        self.game = wordleGame

    def startGame(self):
        self.draw_grid()
        self.draw_grid_line(0)


    def getFirstEmptyTileIndex(self,rowIndex):
        for j in range(0,5):
            if len(self.grid_layout_inputs.itemAtPosition(rowIndex,j).widget().toPlainText()) == 0:
                return j
        return None


    def stop_game(self):
        print("gg")
        if self.game.isWin():
            print(f"numero tentativas: {6-self.game.lifes}")
        else:
            print(f"a palavra era: {self.game.secretWord}")


    def keyPressEvent(self, keyEvent):
        currentRowIndex = self.grid_layout_inputs.rowCount() - 1
        firstEmptyTileIndex = 0

        firstEmptyTileIndex = self.getFirstEmptyTileIndex(currentRowIndex)

        if not self.game.isGameOver():
            if keyEvent.key() == QtCore.Qt.Key.Key_Enter or keyEvent.key() == 16777220 and firstEmptyTileIndex == None:
                currentStr = ""
                for j in range(0,5):
                    currentStr += (self.grid_layout_inputs.itemAtPosition(currentRowIndex,j).widget().toPlainText())
                    self.grid_layout_inputs.removeWidget(self.grid_layout_inputs.itemAtPosition(currentRowIndex,j).widget())
                
                self.game.guess_word(currentStr)
                self.draw_grid_line(currentRowIndex,self.game.board)
                
                if not self.game.isGameOver():
                    self.draw_grid_line(currentRowIndex+1)
                else:
                    self.stop_game()

            elif keyEvent.key() in [QtCore.Qt.Key.Key_Backspace, QtCore.Qt.Key.Key_Delete]:
                if firstEmptyTileIndex == None:
                    # apagar a ultima letra
                    self.grid_layout_inputs.itemAtPosition(currentRowIndex,4).widget().setPlainText("")
                elif firstEmptyTileIndex > 0:
                    self.grid_layout_inputs.itemAtPosition(currentRowIndex,firstEmptyTileIndex-1).widget().setPlainText("")

            elif 64 < keyEvent.key() < 91:
                if firstEmptyTileIndex != None:
                    self.grid_layout_inputs.itemAtPosition(currentRowIndex,firstEmptyTileIndex).widget().setPlainText(str(keyEvent.text()).upper())
                    self.grid_layout_inputs.itemAtPosition(currentRowIndex,firstEmptyTileIndex).widget().setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)


    def draw_grid(self):
        self.grid_layout = QGridLayout()
        self.main_layout.addChildLayout(self.grid_layout)

        for r in range(0,6):
            for c in range(0,5):
                self.row_layout = QHBoxLayout()
                self.square = QFrame()
                self.square.move(c*70+90,10+r*70)
                self.square.resize(65,65)
                self.square.setStyleSheet("background-color: #312a2c; border-radius:10%")
                self.grid_layout.addWidget(self.square,r,c)


    def draw_grid_line(self,rowIndex,rowOfBoard=np.array([['',0],['',0],['',0],['',0],['',0]])):
        # rowOfBoard tem que ser do tipo do gameboard, array2d com char e cores
        
        self.grid_layout_inputs = QGridLayout()
        self.main_layout.addChildLayout(self.grid_layout_inputs)
        
        colorDict = {
            '0':"#312a2c",
            '1':"#d3ad69",
            '2':"#3aa394"
        }

        for c in range(0,5):   
            self.textEditor = LimitedPlainTextEdit(self)
            self.textEditor.insertPlainText(rowOfBoard[c,0])
            self.textEditor.move(c*70+90,10+rowIndex*70)
            self.textEditor.resize(65,65)
            self.textEditor.setStyleSheet(f"font-weight: 900;font-family: 'Mitr', sans-serif;color: #FAFAFF;font-size:40px;margin:0;border:0;background-color: {colorDict[rowOfBoard[c,1]]};border-radius:10%")
            self.textEditor.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.grid_layout_inputs.addWidget(self.textEditor,rowIndex,c)
