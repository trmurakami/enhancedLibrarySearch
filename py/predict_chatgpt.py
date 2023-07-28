from sklearn.preprocessing import LabelEncoder
import pandas as pd
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

data = pd.read_csv('/var/www/html/ml/py/sdg2000.tsv', delimiter='\t')
labels = data['label'].tolist()

# Carregar o modelo treinado
model = load_model('modelo_text_classifier.keras')

# Exemplo de novo texto para classificar
novo_texto = [
    "An Augmented Deep Learning Inference Approach of Vehicle Headlight Recognition for On-Road Vehicle Detection and Counting"]

# Tamanho máximo das sequências (ajuste conforme necessário)
max_sequence_length = 256

# Pré-processamento do novo texto
tokenizer = Tokenizer()
novo_texto_sequences = tokenizer.texts_to_sequences(novo_texto)
novo_texto_padded = pad_sequences(
    novo_texto_sequences, maxlen=max_sequence_length)

# Converter as etiquetas em números (opcional, dependendo do formato das etiquetas)

label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Fazer a previsão
previsao_probabilidades = model.predict(novo_texto_padded)
classe_predita = label_encoder.inverse_transform(
    [previsao_probabilidades.argmax()])

# Exibir a classe prevista
print(f"Texto: {novo_texto}")
print(f"Classe prevista: {classe_predita}")
