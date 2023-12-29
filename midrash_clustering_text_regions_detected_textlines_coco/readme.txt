MIDRASH CLUSTERING DATASET DETECTED TEXT LINES

- midrash_detected_textlines_coco.json file contains the bounding box coordinates of the detected text lines in coco json format.
- inversed_resized_adjusted_grayscale_text_regions_without_folders contains the cropped text regions. These text regions were
resized to have an average character height of 15 pixels, adjusted in terms of brightness and contrast, grayscaled and inversed.
- The images in inversed_resized_adjusted_grayscale_text_regions_without_folders folder are named with this convention:
"{image_file_name}_region_{x}_{y}_{x+width}_{y+height}.png"
image_file_name: is an automatically assigned name consist of numbers. The mapping to the original names are saved in mapping.txt.
x: top left x coordinate
y: top left y coordinate
