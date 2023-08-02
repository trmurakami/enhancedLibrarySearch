import sys
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences

data = pd.read_csv('/var/www/html/ml/py/data/Scopus_SDG.tsv', delimiter='\t')
texts = data['Data'].tolist()
labels = data['Label'].tolist()

tokenizer = keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(texts)

# Carregar o modelo treinado
model = load_model('model_text_classifier.keras')

# Tamanho máximo das sequências (ajuste conforme necessário)
max_sequence_length = 192

# Converter as etiquetas em números (opcional, dependendo do formato das etiquetas)

label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)
num_classes = len(label_encoder.classes_)

query_texts = [sys.argv[1]]
sequences = tokenizer.texts_to_sequences(query_texts)
sequences_padded = pad_sequences(sequences, maxlen=max_sequence_length)

prediction = model.predict(sequences_padded)
print(prediction)
print(label_encoder.inverse_transform(prediction.argmax(axis=1))[0])
