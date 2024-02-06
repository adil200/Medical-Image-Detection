
# Medical Image Detection Web App

Welcome to the Medical Image Detection web app project! This repository contains the code for a Flask-based web application designed to classify medical images into different categories. Below is an in-depth overview of the project, including details about the code structure, algorithms used, and model saving process.
### Input
![Screenshot 2024-02-06 at 3 36 56 PM](https://github.com/adil200/Medical-Image-Detection/assets/75264739/c082a4b3-33bd-4049-8b17-15479476ea3a)
![Screenshot 2024-02-06 at 3 37 29 PM](https://github.com/adil200/Medical-Image-Detection/assets/75264739/59155d20-12ca-4cc8-b6dd-4fb9a1e86628)
### Output
![Screenshot 2024-02-06 at 3 37 35 PM](https://github.com/adil200/Medical-Image-Detection/assets/75264739/6e63a73c-94ad-4567-bd50-97bf4dc55af4)

## Overview

The main file, `app.py`, serves as the core of the web application, integrating Flask, the trained convolutional neural network (CNN) model, and image preprocessing functions. The application allows users to upload medical images, predicts the category of the image using the loaded model, and displays the prediction results on the web interface. What sets this project apart is its ability to classify medical images accurately, enabling medical professionals to streamline diagnosis and treatment processes. The project includes HTML templates for the main and result pages, along with a CSS file for styling.

## Code Details

### Algorithms Used

The Medical Image Detection web app employs a convolutional neural network (CNN) architecture for image classification tasks. CNNs are well-suited for analyzing visual data and have been widely used in medical image analysis due to their ability to extract meaningful features from images. The model is trained on a dataset of medical images spanning different categories such as AbdomenCT, BreastMRI, CXR, ChestCT, Hand, and HeadCT.

### Model Saving Process

The trained CNN model is a crucial component of the Medical Image Detection web app. After training the model on a dataset of medical images, it is saved using TensorFlow's `model.save` function. This serializes the trained model and associated parameters to a file (e.g., `medical_mnist_model.h5`). During the web application's runtime, Flask loads the saved model to classify uploaded medical images accurately.

## Usage

1.  Clone this repository:

```bash
git clone https://github.com/adil200/Medical-Image-Detection.git
cd Medical-Image-Detection
```

2.  To run the web app, ensure you have the required dependencies installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```

3.  Run the Flask application:

```bash
python app.py
```

4.  Open your web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000/) to access the Medical Image Detection web app.
    
5.  Upload a medical image, submit the form, and view the predicted category displayed on the web interface.
    

## Acknowledgments

This web app leverages Flask for web development and utilizes convolutional neural networks for accurate medical image classification. The project aims to assist medical professionals in diagnosing medical conditions more efficiently. Feel free to explore and customize the code to suit your specific requirements.

Please note that the web app is currently set to run in debug mode. Ensure that it meets your security and deployment standards before deploying it in a production environment.
