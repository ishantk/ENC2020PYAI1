"""
    ChatBot -> It has no AI/DL involved in it
    NLTK -> Natural Language Processing ToolKit
"""

from nltk.chat.util import Chat, reflections

# Chat is class in NLTK to develop a simple ChatBot
# reflections is a pre-defined dictionary for opposites

# print(reflections)
# print(reflections['i am'])

# Conversation is a List of Question and Answers
conversation = [
    [
        # Question OR Ask by User
        "Hi",
        # Answer OR Reply to User
        ["Hey I am John, What can I do for You? ", "Hi I am John, I will be happy to assist You"]
    ],

    [
        # Question OR Ask by User
        "I need to know about courses",
        # Answer OR Reply to User
        ["Sue, May i know your name first? ", ]
    ],

    [
        # Question OR Ask by User
        r"my name is (.*)", # use regular expression in strings
        # Answer OR Reply to User
        ["Thank You %1. what programming languages do you know ?", ]
    ],

    [
        # Question OR Ask by User
        r"i know (.*)", # use regular expression in strings
        # Answer OR Reply to User
        ["That's Great for you to code in %1", ]
    ],
]

# List of Lists
print(conversation)


def main():
    print("Welcome to Help Support")
    chat_bot = Chat(conversation, reflections)
    chat_bot.converse()

if __name__ == '__main__':
    main()


# Explore more on Chat Object of NLTK to develop some support for your project work :)
# Framework to write Conversational Apps : https://dialogflow.cloud.google.com/