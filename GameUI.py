from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow,QVBoxLayout, QWidget, QLabel,QHBoxLayout,QPlainTextEdit,QFrame

class LimitedPlainTextEdit(QPlainTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def keyPressEvent(self, event):
        if len(self.toPlainText()) < 5 or event.key() in [QtCore.Qt.Key.Key_Backspace, QtCore.Qt.Key.Key_Delete]:
            super().keyPressEvent(event)
        else:
            event.ignore()

class SquareTileWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wave Main Window")
        self.setFixedWidth(525)
        self.setFixedHeight(650)
        self.setStyleSheet("background-color: #6e5c62; font-family: 'Helvetica Neue'; font-size: 16px;")
        # font-family: 'Clear Sans', 'Helvetica Neue', Arial, sans-serif;")

        # Create a central widget and set a layout for it
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget) 

        self.draw_grid()


    def draw_grid(self):
        self.grid_layout = QVBoxLayout()
        self.main_layout.addChildLayout(self.grid_layout)

        for r in range(0,6):
            for c in range(0,5):
                self.row_layout = QHBoxLayout()
                self.square = QFrame()
                self.square.move(c*70+90,10+r*70)
                self.square.resize(65,65)
                self.square.setStyleSheet("background-color: #312a2c; border-radius:5px")
                self.row_layout.addWidget(self.square)
                self.grid_layout.addChildLayout(self.row_layout)



        self.textEditor = LimitedPlainTextEdit(self)
        self.textEditor.insertPlainText("ABCDE")
        self.textEditor.move(90,10)
        self.textEditor.resize(345,65)

        self.textEditor.setStyleSheet(f"font-size: 0.65em;font-weight: 600;font-family: 'Mitr', sans-serif;color: #FAFAFF;font-size:61px; background-color: rgba(242, 69, 57,10);letter-spacing:30px")

        # self.textEditor.setMaximumBlockCount(4)
        # self.textEditor.setTabStopDistance(4)
        


    # def draw_line(self):
    #     row_layout = QHBoxLayout()
    #     self.main_layout.addLayout(row_layout)

    #     row_layout.setSpacing(0)
    #     row_layout.setContentsMargins(0, 0, 0, 0)
        
    #     for _ in range(5):
    #         square_label = QLabel()
    #         square_label.setFixedSize(50, 50)  # Set size to make it a square
    #         square_label.setStyleSheet("background-color: white; margin:0; padding:0")
    #         row_layout.addWidget(square_label)



