"""
    NATURAL LANGUAGE PROCESSING
    NLTK - Natual Language Toolkit

    https://www.nltk.org/
    https://www.nltk.org/book/

    pip install nltk
    nltk.download() -> API will download the desired packages for us| UI pop up
    nltk.download("stopwords") -> Download soe individual module with command
"""

import nltk
import re
# nltk.download()
# nltk.download("stopwords")

stop_words = ["is", "a", "and", "we", "to", "go"]

def remove_noise_from_text(text):
    words = text.split()
    print(words)
    noise_free_words = [word for word in words if word not in stop_words]
    print(noise_free_words)

    noise_free_text = " ".join(noise_free_words)
    print(noise_free_text)


def remove_noise_from_text_re(text, pattern):
    matches = re.finditer(pattern, text)

    for match in matches:
        print("Group", match.group())
        text = re.sub(match.group().strip(), '', text)

    print("Final Text", text)

# Text Pre-Processing
# text = "This is a very good day. we will have a vacation planned today and go to work"
# remove_noise_from_text(text=text)

text = "This is a #Covid19 situation. Please stay safe and be at home"
regex_pattern = "#[\w]*"

remove_noise_from_text_re(text=text, pattern=regex_pattern)

# Assignment:
# Explore NLTK APIs to remove stop words