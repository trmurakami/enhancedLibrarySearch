#!/usr/bin/python3
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

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
import numpy as np

dadosBiblioteca = pd.read_csv('data.tsv',sep="\t")

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='utf-8', ngram_range=(1, 2), stop_words=stopwords.words('portuguese'))

X_train, X_test, y_train, y_test = train_test_split(dadosBiblioteca['dados'], dadosBiblioteca['label'], test_size=0.30, random_state=42)

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
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(70, ), random_state=1, max_iter=200, verbose=True)
    clf.fit(X_train_tfidf_vectorize, y_train)
    joblib.dump(clf, joblib_file)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/title', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'title' in request.args:
        title = request.args['title']
        predict_result = clf.predict(count_vect.transform([title]))
    else:
        return "Error: Não foi informado um título."

    # Create an empty list for our results
    

    return jsonify(predict_result[0])

app.run()