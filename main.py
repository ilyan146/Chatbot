from PyQt6 import QMainWindow, QTextEdit

# Create chatbot window class
class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # Add chat are widget
        self.chat_area = QTextEdit(self)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
