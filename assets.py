import cv2
import numpy as np

# Define the dimensions of the black image
width = 800
height = 800

# Create a black image (all zeros)
black_image = np.zeros((height, width, 3), dtype=np.uint8)
green_image = np.zeros((50,150,3), dtype = np.uint8)
green_image[:,:,1] = 255

# Display the black image (optional)
cv2.imwrite("Background.jpg", black_image)
cv2.imwrite("Bot.jpg",green_image)

