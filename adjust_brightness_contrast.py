# This code is based on the algorithm described in https://stackoverflow.com/questions/56905592/automatic-contrast-and-brightness-adjustment-of-a-color-photo-of-a-sheet-of-pape/56909036#56909036

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

# Automatic brightness and contrast optimization with optional histogram clipping
def automatic_brightness_and_contrast(gray, clip_hist_percent=1):
    # Calculate grayscale histogram
    hist = cv2.calcHist([gray],[0],None,[256],[0,256])
    hist_size = len(hist)
    
    # Calculate cumulative distribution from the histogram
    accumulator = []
    accumulator.append(float(hist[0]))
    for index in range(1, hist_size):
        accumulator.append(accumulator[index -1] + float(hist[index]))
    
    # Locate points to clip
    maximum = accumulator[-1]
    clip_hist_percent *= (maximum/100.0)
    clip_hist_percent /= 2.0
    
    # Locate left cut
    minimum_gray = 0
    while accumulator[minimum_gray] < clip_hist_percent:
        minimum_gray += 1
    
    # Locate right cut
    maximum_gray = hist_size -1
    while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
        maximum_gray -= 1
    
    # Calculate alpha and beta values
    alpha = 255 / (maximum_gray - minimum_gray)
    beta = -minimum_gray * alpha
    
    auto_result = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return auto_result

# Create a new directory for equalized images
output_dir = "adjusted_grayscale_text_regions"
os.makedirs(output_dir, exist_ok=True)

# Traverse the folders in the input directory
input_dir = "grayscale_text_regions"
for root, _, files in os.walk(input_dir):
    for file in files:
        if file.endswith(".png"):
            # Load the image
            image_path = os.path.join(root, file)
            image = cv2.imread(image_path, 0)  # Read the image in grayscale

            # Adjust brightness and contrast
            adjusted_image= automatic_brightness_and_contrast(image)

            # Create the corresponding output folder and save the image
            relative_path = os.path.relpath(image_path, input_dir)
            output_folder = os.path.join(output_dir, os.path.dirname(relative_path))
            os.makedirs(output_folder, exist_ok=True)
            output_path = os.path.join(output_folder, file)
            cv2.imwrite(output_path, adjusted_image)

print("Brightness and contrast adjustment completed.")


