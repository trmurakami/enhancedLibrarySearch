#!/usr/bin/python3
import pickle
from keras_preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import sys
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


labels = ['SDG01', 'SDG02', 'SDG03', 'SDG04',
          'SDG05', 'SDG06', 'SDG07', 'SDG08']

# Carregar o modelo tokenizador
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Carregar o modelo treinado
model = load_model('model_text_classifier.keras')

# Tamanho máximo das sequências (ajuste conforme necessário)
max_sequence_length = 192

# Converter as etiquetas em números (opcional, dependendo do formato das etiquetas)

label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)
num_classes = len(label_encoder.classes_)


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

        query_texts = [title]
        sequences = tokenizer.texts_to_sequences(query_texts)
        sequences_padded = pad_sequences(sequences, maxlen=max_sequence_length)

        prediction = model.predict(sequences_padded)
        predict_result = label_encoder.inverse_transform(
            prediction.argmax(axis=1))[0]
    else:
        return "Error: Não foi informado um título."

    # Create an empty list for our results

    return jsonify(predict_result)


app.run()
