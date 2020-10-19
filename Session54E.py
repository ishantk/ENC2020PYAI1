"""
    Feature Extraction -> Count Vectorizer
"""

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
print(vectorizer)


chat_log = [
    'Hello, This is Gorge. How can i Help you?',
    'hi, i need to raise a complaint',
    'may i know which laptop model is it for',
    'this is for my macbook air',
    'what exactly is the complaint?',
    'it is not supporting icloud'
]

print(chat_log)


X = vectorizer.fit_transform(chat_log)
print(X)

analysis = vectorizer.build_analyzer()
print(analysis)

print(vectorizer.get_feature_names())
print(X.toarray())