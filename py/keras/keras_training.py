import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from keras_preprocessing.sequence import pad_sequences


data = pd.read_csv('/var/www/html/ml/py/data/Scopus_SDG.tsv', delimiter='\t')
texts = data['Data'].tolist()
labels = data['Label'].tolist()

texts, labels = shuffle(texts, labels, random_state=42)

tokenizer = keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

max_sequence_length = 192

sequences_padded = pad_sequences(sequences, maxlen=max_sequence_length)

vocab_size = len(tokenizer.word_index) + 1

label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)
num_classes = len(label_encoder.classes_)

X_train, X_test, y_train, y_test = train_test_split(
    sequences_padded, encoded_labels, test_size=0.2, random_state=42)

model = keras.Sequential()
model.add(keras.layers.Embedding(vocab_size, 10,
                                 input_length=max_sequence_length, mask_zero=True))
model.add(keras.layers.LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(keras.layers.Dense(num_classes, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=192, epochs=15,
          validation_data=(X_test, y_test))

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

model.save('model_text_classifier.keras')

predictions = model.predict(X_test)
y_pred = predictions.argmax(axis=1)
y_test = y_test.astype('int')
print(y_pred)
print(y_test)
print(label_encoder.inverse_transform(y_pred))
print(label_encoder.inverse_transform(y_test))