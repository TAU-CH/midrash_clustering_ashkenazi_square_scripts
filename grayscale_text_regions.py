import os
import cv2

# Define the source folder containing the original images.
source_folder = "color_text_regions"
# Define the destination folder for the binarized images.
destination_folder = "grayscale_text_regions"

# Create the destination folder if it doesn't exist.
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through each folder in the source folder.
for folder_name in os.listdir(source_folder):
    folder = os.path.join(source_folder, folder_name)
    if os.path.isdir(folder):
        # Create a corresponding subfolder in the destination folder.
        destination_subfolder = os.path.join(destination_folder, folder_name)
        if not os.path.exists(destination_subfolder):
            os.makedirs(destination_subfolder)

        # Get a list of image files in the folder.
        image_files = [file for file in os.listdir(folder) if file.endswith(".png")]

        # Process and save binarized images to the destination subfolder.
        for image_file in image_files:
            source_path = os.path.join(folder, image_file)
            destination_path = os.path.join(destination_subfolder, image_file)

            # Read the image in grayscale.
            gray_image = cv2.imread(source_path, cv2.IMREAD_GRAYSCALE)

            # Save the grayscale image to the destination folder.
            cv2.imwrite(destination_path, gray_image)

print("Grayscaling and saving completed.")
