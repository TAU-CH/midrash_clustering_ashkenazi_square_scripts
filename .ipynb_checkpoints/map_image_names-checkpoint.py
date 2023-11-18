import os

# Directory containing the files
folder_path = "midrash_cluster_images"

# Get a list of files in the directory
file_list = os.listdir(folder_path)

# Create a list of valid extensions in lowercase
valid_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"]

# Create a mapping of original names to new names
file_mapping = {}

# Iterate through the files, filter and rename them
for index, filename in enumerate(file_list):
    _, file_extension = os.path.splitext(filename)
    file_extension = file_extension.lower()  # Convert to lowercase
    if file_extension in valid_extensions:
        # Generate the new filename with the same extension
        new_filename = f"{index+1}{file_extension}"

        # Rename the file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

        # Add the mapping to the dictionary
        file_mapping[filename] = new_filename
    else:
        # Delete files with invalid extensions
        os.remove(os.path.join(folder_path, filename))

# Specify the full path for the "mapping.txt" file
mapping_file = "mapping.txt"

# Create a text file to save the mapping
with open(mapping_file, "w") as f:
    for original, new in file_mapping.items():
        f.write(f"{original} -> {new}\n")

print("Files renamed, invalid files removed, and the mapping is saved to 'mapping.txt'.")
