import nltk
import random
import string

# Download necessary resources
nltk.download("punkt")
nltk.download("wordnet")

from nltk.chat.util import Chat, reflections

# Define chatbot responses (Pattern, Response)
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi! How can I help you?"]),
    (r"how are you?", ["I'm just a bot, but I'm doing fine!", "I'm great! How about you?"]),
    (r"what is your name?", ["I'm a chatbot!", "You can call me mini ChatGPT!"]),
    (r"what can you do?", ["I can chat with you, answer basic questions, and make small talk!"]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Take care!"]),
    (r"(.*)", ["I'm not sure how to respond to that.", "Could you ask something else?"])
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chatting
print("Simple Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
