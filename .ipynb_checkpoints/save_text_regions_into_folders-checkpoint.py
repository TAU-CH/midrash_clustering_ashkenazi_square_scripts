import os
import json
from PIL import Image


with open('midrash_cluster_coco.json', 'r') as json_file:
    annotation_data = json.load(json_file)

    
output_folder = 'color_text_regions'
os.makedirs(output_folder, exist_ok=True)


for image_info in annotation_data['images']:
    image_id = image_info['id']
    image_file_name = image_info['file_name']

    # Load the corresponding image
    image_path = os.path.join('midrash_cluster_images', image_file_name)
    img = Image.open(image_path)

    for annotation in annotation_data['annotations']:
        if annotation['image_id'] == image_id:
            bbox = annotation['bbox']
            x, y, width, height = bbox
            cropped_region = img.crop((x, y, x + width, y + height))

            # Create a subfolder for each image and save the cropped region with coordinates
            image_folder = os.path.join(output_folder, os.path.splitext(image_file_name)[0])
            os.makedirs(image_folder, exist_ok=True)

            # Remove the file extension
            root_name, file_extension = os.path.splitext(image_file_name)
            # Generate a filename with coordinates
            region_filename = f'{root_name}_region_{x}_{y}_{x+width}_{y+height}.png'
            cropped_region.save(os.path.join(image_folder, region_filename))
print("Cropped the text regions and saved them into text_regions folder")