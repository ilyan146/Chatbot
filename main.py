from ChatGUI import ChatbotWindow
from PyQt6.QtWidgets import QApplication
import sys


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
