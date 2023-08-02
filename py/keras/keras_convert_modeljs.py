import tensorflow as tf
import tensorflowjs as tfjs


model = tf.keras.models.load_model('model_text_classifier.keras')
tfjs.converters.save_keras_model(model, 'Model_js')
