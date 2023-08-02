import sys

if len(sys.argv) != 2:
    print("Uso: python keras_predict.py <query>")
else:
    try:

        from sklearn.preprocessing import LabelEncoder
        from sklearn.model_selection import train_test_split
        from keras.models import load_model
        from keras.preprocessing.text import Tokenizer
        from keras.preprocessing.sequence import pad_sequences

        labels = ['SDG01', 'SDG02', 'SDG03', 'SDG04', 'SDG05', 'SDG06', 'SDG07', 'SDG08',
                  'SDG09', 'SDG10', 'SDG11', 'SDG12', 'SDG13', 'SDG14', 'SDG15', 'SDG16', 'SDG17']

        # Carregar o modelo treinado
        model = load_model('modelo_text_classifier.keras')

        # Tokenização dos textos
        tokenizer = Tokenizer()

        # Tamanho máximo das sequências (ajuste conforme necessário)
        max_sequence_length = 128

        # Converter as etiquetas em números (opcional, dependendo do formato das etiquetas)

        label_encoder = LabelEncoder()
        encoded_labels = label_encoder.fit_transform(labels)
        num_classes = len(label_encoder.classes_)

        query_string = sys.argv[1]
        prediction = model.predict(pad_sequences(
            tokenizer.texts_to_sequences([query_string]), maxlen=max_sequence_length))
        # print(prediction)
        print(label_encoder.inverse_transform(prediction.argmax(axis=1))[0])
    except ValueError:
        print("Por favor, insira uma consulta válida.")
