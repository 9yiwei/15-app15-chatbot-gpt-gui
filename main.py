from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QLineEdit, QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
import sys


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(700, 500)

        # 創建對話框
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # 創建輸入框
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        # 創建送出按鈕
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)


app = QApplication(sys.argv)
main_window = ChatBotWindow()
main_window.show()
sys.exit(app.exec())