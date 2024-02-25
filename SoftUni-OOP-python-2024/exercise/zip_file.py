import zipfile
import os


def zip_directory(directory, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), directory))

# Example usage
directory_to_zip = "project"
zip_name = "project.zip"

zip_directory(directory_to_zip, zip_name)