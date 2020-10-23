import nltk
# nltk.download('punkt') -> Required for word_tokenize
# nltk.download('averaged_perceptron_tagger') -> Required for POS Tagging

from nltk import word_tokenize, pos_tag

sentence = "A very Happy Navratras to All. Code Well. Be at Home. Stay Safe :)"

tokens = word_tokenize(sentence)

print(tokens)

# POS is Parts of Speech
# POS Tagging is tagging the token with language grammar
print(pos_tag(tokens))