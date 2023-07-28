#!/usr/bin/python3

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

joblib_file = "clf.pkl"

f = open(joblib_file)
f.close()
clf = joblib.load(joblib_file)

count_vect = CountVectorizer()

print(clf.predict(count_vect.transform(['The impact of subject-specific competencies and reading habits on the income of Japanese business and economics graduates'])))