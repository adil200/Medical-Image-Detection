"""
This file contains the Flask application that serves the web interface for the image classification model.
"""

# Importing the required libraries
from flask import Flask, render_template, request, redirect, url_for
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from flask import send_from_directory
from PIL import Image

app = Flask(__name__)

# Loading the trained model
model_path = "/Users/adilmohammed/Desktop/Medical Image Detection/model/medical_mnist_model.h5"
model = tf.keras.models.load_model(model_path)

app.config['UPLOAD_FOLDER'] = 'uploads'

# Function to preprocess the image
def preprocess_image(image_path):
    img = Image.open(image_path).convert('L') 
    img = img.resize((128, 128))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=-1) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Function to make predictions
def predict_image(image_path):
    img_array = preprocess_image(image_path)
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    return predicted_class

# Function to serve the uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Function to handle the index page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            return redirect(request.url)

        if file:
            image_path = os.path.join("uploads", file.filename)
            file.save(image_path)

            predicted_class = predict_image(image_path)

            class_names = ["AbdomenCT", "BreastMRI", "CXR", "ChestCT", "Hand", "HeadCT"]
            predicted_class_name = class_names[predicted_class]

            return render_template("result.html", predicted_class=predicted_class_name, img_path=image_path, file=file)
        
    return render_template("index.html")

# Main function
if __name__ == "__main__":
    app.run(debug=True)