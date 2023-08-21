import cv2
import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load the VGG16 model without classification layers
base_model = VGG16(weights="imagenet", include_top=False)
model = Model(inputs=base_model.input, outputs=base_model.layers[-1].output)

# Define the dataset folders and corresponding labels
dataset_folders = {
    "folder1": "path/to/folder1",
    "folder2": "path/to/folder2",
    "folder3": "path/to/folder3",
    "folder4": "path/to/folder4"
}

# Load the uploaded image
uploaded_image = cv2.imread("path_to_uploaded_image.jpg")

# Preprocess uploaded image and extract features
uploaded_features = model.predict(np.expand_dims(preprocess_input(uploaded_image), axis=0))

# Calculate cosine similarity with images in each folder
max_similarity = -1
matching_folder = None

for label, folder in dataset_folders.items():
    for filename in os.listdir(folder):
        image_path = os.path.join(folder, filename)
        known_image = cv2.imread(image_path)

        # Preprocess known image and extract features
        known_features = model.predict(np.expand_dims(preprocess_input(known_image), axis=0))

        # Calculate cosine similarity
        similarity = cosine_similarity(uploaded_features, known_features)[0][0]

        if similarity > max_similarity:
            max_similarity = similarity
            matching_folder = label

# Set a similarity score threshold
threshold = 0.7  # Adjust this threshold based on your data

# Determine the matching folder based on similarity
if matching_folder is not None and max_similarity > threshold:
    print(f"The uploaded image matches folder: {matching_folder}")
else:
    print("No matching folder found for the uploaded image.")
