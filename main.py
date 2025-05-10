from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import Chatbot


# Create a chatbot window class
class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # Initialize the chatbot backend
        self.chatbot = Chatbot()

        # Add the chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        # Connect enter key to send message
        self.input_field.returnPressed.connect(self.send_message)

        # Add button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        if not user_input:
            return
        # Display user input in chat area
        self.chat_area.append(f"You: {user_input}")
        # Get the response
        response = self.chatbot.get_response(user_input)

        # Display the chatbot response in chat area
        self.chat_area.append(f"Chatbot: {response}")

        # Clear the input field
        self.input_field.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ChatbotWindow()
    sys.exit(app.exec())
