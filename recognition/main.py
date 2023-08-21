import cv2
from skimage.metrics import structural_similarity as ssim

# Load the known images x, y, and z
image_car = cv2.imread("C:/Users/1154-Talha/PycharmProjects/recognition/images/car.png")
image_oreo = cv2.imread("C:/Users/1154-Talha/PycharmProjects/recognition/images/oreo.png")
image_joker = cv2.imread("C:/Users/1154-Talha/PycharmProjects/recognition/images/oreo.png")

# Load the uploaded image
uploaded_image = cv2.imread("C:/Users/1154-Talha/PycharmProjects/recognition/images/uplaodedimage/uploadedimage.png")

# Resize all images to a common size
common_size = (180 , 180)  # Set the desired common size
image_car_resized = cv2.resize(image_car, common_size)
image_joker_resized = cv2.resize(image_oreo, common_size)
image_m_resized = cv2.resize(image_joker, common_size)
uploaded_image_resized = cv2.resize(uploaded_image, common_size)

# Calculate SSIM scores
ssim_x = ssim(image_car_resized, uploaded_image_resized, multichannel=True)
ssim_y = ssim(image_joker_resized, uploaded_image_resized, multichannel=True)
ssim_z = ssim(image_m_resized, uploaded_image_resized, multichannel=True)

# Determine the most similar image
if ssim_x > ssim_y and ssim_x > ssim_z:
    print("The uploaded image is most similar to image car")
elif ssim_y > ssim_x and ssim_y > ssim_z:
    print("The uploaded image is most similar to image oreo")
else:
    print("The uploaded image is most similar to image joker")
