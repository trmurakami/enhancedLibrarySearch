from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense

data = pd.read_csv('/var/www/html/ml/py/sdg2000.tsv', delimiter='\t')
texts = data['dados'].tolist()
labels = data['label'].tolist()

texts, labels = shuffle(texts, labels, random_state=42)

# Tokenização dos textos
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# Tamanho máximo das sequências (ajuste conforme necessário)
max_sequence_length = 256

# Padding das sequências para o mesmo tamanho
sequences_padded = pad_sequences(sequences, maxlen=max_sequence_length)

# Número total de palavras no vocabulário
vocab_size = len(tokenizer.word_index) + 1

# Converter as etiquetas em números (opcional, dependendo do formato das etiquetas)

label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)
num_classes = len(label_encoder.classes_)

X_train, X_test, y_train, y_test = train_test_split(
    sequences_padded, encoded_labels, test_size=0.2, random_state=42)

model = Sequential()
model.add(Embedding(vocab_size, 100,
          input_length=max_sequence_length, mask_zero=True))
model.add(LSTM(256, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='sgd', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=128, epochs=10,
          validation_data=(X_test, y_test))

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

model.save('modelo_text_classifier.keras')
