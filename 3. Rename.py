import os

# Define the directory path where the files are located
directory_path = "StructuredData/"

# Iterate over each folder within the directory
for folder_name in os.listdir(directory_path):
    folder_path = os.path.join(directory_path, folder_name)

    # Check if the current item in the directory is a folder
    if os.path.isdir(folder_path):
        # Iterate over each file within the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # Check if the file is a text file (TXT)
            if file_name.endswith(".txt"):
                # Rename the text file to "ClaimNo.txt"
                new_file_name = "ClaimNo.txt"
                new_file_path = os.path.join(folder_path, new_file_name)
                os.rename(file_path, new_file_path)

            # Check if the file is an Excel file (XLSX)
            elif file_name.endswith(".xlsx"):
                # Rename the Excel file to "data.xlsx"
                new_file_name = "data.xlsx"
                new_file_path = os.path.join(folder_path, new_file_name)
                os.rename(file_path, new_file_path)
