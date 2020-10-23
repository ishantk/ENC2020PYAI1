"""
    NLTK

    Lexicon Normalization
        > Stemming
        > Lemmatization
"""
# import nltk
# nltk.download('wordnet') -> execute for lemmatization word net

# Stemming
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
word = "troubled"
# word = "races"
# word = "racing"
# word = "playing"
# word = "changed"
processed_word = stemmer.stem(word=word)
print(processed_word)

# Stemming returns roots for the words but i may not be a dictionary meaning

# Lemmatization
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
word = "troubled"
processed_word = lemmatizer.lemmatize(word, "v")
print(processed_word)

