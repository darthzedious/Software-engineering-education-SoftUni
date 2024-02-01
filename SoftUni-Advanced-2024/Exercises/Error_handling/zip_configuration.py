import zipfile
import os

# Define the files you want to include in the zip file
files_to_zip = ['01_numbers_dictionary.py', '02_email_validator.py']  #'other_folder/another_file.py'

# Specify the name of the zip file
zip_file_name = 'homework.zip'

# Open the zip file in write mode
with zipfile.ZipFile(zip_file_name, 'w') as zipf:
    # Add each file to the zip file
    for file in files_to_zip:
        zipf.write(file)

print(f'Zip file "{zip_file_name}" created successfully.')
