#!/usr/bin/python3

from __future__ import division
from sklearn.datasets import make_classification
import numpy as np
import sys
import pandas as pd
import re
import nltk
from sklearn.datasets import load_files
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.neural_network import MLPClassifier
import joblib

dadosBiblioteca = pd.read_csv('data_sdg.tsv', sep="\t")

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=1, norm='l2', encoding='utf-8',
                        ngram_range=(1, 1), stop_words=stopwords.words('english'))

X_train, X_test, y_train, y_test = train_test_split(
    dadosBiblioteca['dados'], dadosBiblioteca['label'], test_size=0.20, random_state=42)

count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(X_train)

tfidf_transformer = TfidfTransformer()

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

X_train_tfidf_vectorize = tfidf_transformer.fit_transform(X_train_counts)

joblib_file = "clf.pkl"
try:
    f = open(joblib_file)
    f.close()
    clf = joblib.load(joblib_file)
except FileNotFoundError:
    print('File does not exist')
    clf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(70, ),
                        random_state=42, max_iter=100, verbose=True, warm_start=True)
    clf.fit(X_train_tfidf_vectorize, y_train)
    joblib.dump(clf, joblib_file)

print(clf.predict(count_vect.transform([sys.argv[1]])))

print(clf.predict_proba(count_vect.transform([sys.argv[1]]))[:, 1])



#Creating an imaginary dataset
input, output = make_classification(1000, 30, n_informative=10, n_classes=2)
input = input / input.max(axis=0)
N = input.shape[0]
train_input = input[0:N/2, :]
train_target = output[0:N/2]

test_input = input[N/2:N, :]
test_target = output[N/2:N]

#Creating and training the Neural Net
# 1. Disable verbose (verbose is annoying with partial_fit)

clf = MLPClassifier(activation='tanh', algorithm='sgd', learning_rate='constant',
                    alpha=1e-4, hidden_layer_sizes=(15,), random_state=1, batch_size=1, verbose=False,
                    max_iter=1, warm_start=True)

# 2. Set what the classes are
clf.classes_ = [0, 1]

for j in xrange(0, 100):
    for i in xrange(0, train_input.shape[0]):
       input_inst = train_input[[i]]
       target_inst = train_target[[i]]

       clf = clf.partial_fit(input_inst, target_inst)

    # 3. Monitor progress
    print "Score on training set: %0.8f" % clf.score(train_input, train_target)
#Testing the Neural Net
y_pred = clf.predict(test_input)
print y_pred

# 4. Compute score on testing set
print clf.score(test_input, test_target)
