import numpy as np
import nltk
import re
import heapq

paragraph = '''This will be very huge paragrapgh.This will be very huge paragrapgh.
               This is going to be very huge paragrapgh.This is becoming very large paragrapgh.
               This will be very huge paragrapgh.This will be very huge paragrapgh.
               This is going to be very huge paragrapgh.This will be very huge paragrapgh.
               This contains random data feel free to manipulate this paragraph.
               You can add, delete, recreate or modify this paragrapgh.
            '''

sentences = nltk.sent_tokenize(paragraph)

# Preprocessing the data
for i in range(len(sentences)):
    sentences[i] = sentences[i].lower()
    sentences[i] = re.sub(r"\s+", " ", sentences[i])
    sentences[i] = re.sub(r"\W", " ", sentences[i])

# Creating the histogram
word_count = {}
for sent in sentences:
    words = nltk.word_tokenize(sent)

    for word in words:
        if word not in word_count.keys():
            word_count[word] = 1
        else:
            word_count[word] += 1

freq_words = heapq.nlargest(100, word_count, key = word_count.get)

X = []
for sent in sentences:
    vector = []

    for word in freq_words:
        if word in nltk.word_tokenize(sent):
            vector.append(1)
        else:
            vector.append(0)

    X.append(vector)

X = np.asarray(X)
