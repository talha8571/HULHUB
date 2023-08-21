import cv2
from skimage.metrics import structural_similarity as ssim
import os

# Load the known images x, y, and z
# image_car = cv2.imread("C:/Users/1154-Talha/PycharmProjects/recognition/images/car/car.png")
image_joker = cv2.imread("C:/Users/1154-Talha/PycharmProjects/recognition/images/joker/joker.png")
# image_oreo = cv2.imread("C:/Users/1154-Talha/PycharmProjects/recognition/images/oreo/oreo.png")
# image_m = cv2.imread("C:/Users/1154-Talha/PycharmProjects/recognition/images/m/m.png")

# Define the dataset folders
dataset_folders = {
    # "car": "C:/Users/1154-Talha/PycharmProjects/recognition/images/car/",
    "joker": "C:/Users/1154-Talha/PycharmProjects/recognition/images/joker/",
    # "oreo": "C:/Users/1154-Talha/PycharmProjects/recognition/images/oreo/",
    # "m": "C:/Users/1154-Talha/PycharmProjects/recognition/images/m/"
}

# Load the uploaded image
uploaded_image = cv2.imread("C:/Users/1154-Talha/PycharmProjects/recognition/images/uplaodedimage/oo2.png")

# Resize the uploaded image
common_size = (180, 180)
uploaded_image_resized = cv2.resize(uploaded_image, common_size)

# Calculate SSIM scores for each image in the dataset
max_ssim = -1
matching_label = None

for label, folder in dataset_folders.items():
    for filename in os.listdir(folder):
        image_path = os.path.join(folder, filename)
        known_image = cv2.imread(image_path)
        known_image_resized = cv2.resize(known_image, common_size)
        similarity = ssim(uploaded_image_resized, known_image_resized, multichannel=True)

        if similarity > max_ssim:
            max_ssim = similarity
            matching_label = label

# Determine the most similar image label
if matching_label is not None:
    print(f"The uploaded image is most similar to image {matching_label}.")
else:
    print("No matching image found in the dataset.")

print(similarity)
