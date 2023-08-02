import tensorflowjs as tfjs
import tensorflow as tf
from keras.models import load_model

model = load_model('modelo_text_classifier.keras')
tfjs.converters.save_keras_model(model, 'Model_js')
