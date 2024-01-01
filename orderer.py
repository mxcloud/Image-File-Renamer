import os
import uuid

def generate_unique_id():
    # Generate a UUID and convert it to a string, then take the first 10 characters
    return str(uuid.uuid4())[:10]

def rename_images_in_folder(folder_path):
    # List all files in the directory
    for filename in os.listdir(folder_path):
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Generate a unique ID for the new filename
            new_filename = generate_unique_id() + os.path.splitext(filename)[1]
            # Construct the full old and new file paths
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed "{filename}" to "{new_filename}"')

# Replace 'path_to_your_folder' with the path to the folder containing your images
rename_images_in_folder(r'path_to_your_folder')
