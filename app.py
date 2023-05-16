import streamlit as st
import tensorflow as tf
import os
import numpy as np
from PIL import Image

MODEL_DIR = "saved_models"  # Define the directory to save the model

# Define class names for Fashion MNIST
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

@st.cache(allow_output_mutation=True, hash_funcs={tf.keras.Model: id})
def load_model():
    model_path = os.path.join(MODEL_DIR, "/content/drive/MyDrive/project/model.h5")
    model = tf.keras.models.load_model(model_path)
    return model

st.write("# Clothes Detection System")
file = st.file_uploader("Choose clothes photo from computer", type=["jpg", "png"])

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    model = load_model()  # Load the trained model
    prediction = model.predict(np.array([np.array(image.resize((28, 28)))/255.0]))
    predicted_class = class_names[np.argmax(prediction)]
    string = "OUTPUT : " + predicted_class
    st.success(string)
