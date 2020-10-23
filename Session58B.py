# Object Standardization

dictionary = {
    "brb": "be right back",
    "cb": "call back",
    "awsm": "awesome",
    "lol": "laugh out loud",
    "yu": "you"
}

def object_standardization(text):

    words = text.split()

    substitution_words = []

    for word in words:
        if word in dictionary:
            substitution_words.append(word)


    text = " ".join(substitution_words)
    print("TEXT")
    print(text)


chat_text = "awsm yu are. cb soon i will be waiting"
object_standardization(text=chat_text)

# Assignment: Substitute the real menaning of the words in the original text

