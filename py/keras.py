import pandas as pd
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle


data = pd.read_csv('/var/www/html/ml/py/data/Scopus_SDG.tsv', delimiter='\t')
texts = data['Data'].tolist()
labels = data['Label'].tolist()

texts, labels = shuffle(texts, labels, random_state=42)

# Tokenização dos textos
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = text_to_sequences(texts)

# # Tamanho máximo das sequências (ajuste conforme necessário)
max_sequence_length = 128

# # Padding das sequências para o mesmo tamanho
sequences_padded = pad_sequences(sequences, maxlen=max_sequence_length)

# # Número total de palavras no vocabulário
vocab_size = len(tokenizer.word_index) + 1

# # Converter as etiquetas em números (opcional, dependendo do formato das etiquetas)

label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)
num_classes = len(label_encoder.classes_)

X_train, X_test, y_train, y_test = train_test_split(
    sequences_padded, encoded_labels, test_size=0.2, random_state=42)

model = keras.Sequential()
model.add(Embedding(vocab_size, 10,
                    input_length=max_sequence_length, mask_zero=True))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=128, epochs=15,
          validation_data=(X_test, y_test))

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

model.save('modelo_text_classifier.keras')

# predictions = model.predict(X_test)
# y_pred = predictions.argmax(axis=1)
# y_test = y_test.astype('int')
# print(y_pred)
# print(y_test)
# print(label_encoder.inverse_transform(y_pred))
# print(label_encoder.inverse_transform(y_test))
