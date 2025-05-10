from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


class Chatbot:
    def __init__(self):
        self.url = os.getenv("API_URL")
        self.key = os.getenv("API_KEY")
        # openai.api_key = os.environ.get("openai_key")

    # def get_response_old(self, user_input):
    #     response = (
    #         openai.ChatCompletion.create(
    #             engine="text-davinci-001",  # text-davinci-003"
    #             prompt=user_input,
    #             max_tokens=3000,
    #             temperature=0.5,
    #         )
    #         .choices[0]
    #         .text
    #     )
    #     return response

    def get_response(self, user_input):
        client = AzureOpenAI(
            azure_endpoint=self.url, api_key=self.key, api_version="2024-05-01-preview"
        )
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ],
        )
        chatbot_response = response.choices[0].message.content
        return chatbot_response


if __name__ == "__main__":
    chatbot = Chatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        chat_response = chatbot.get_response(user_input)
        print("Chatbot:", chat_response)
