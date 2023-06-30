import os

# Path to the "StructuredData" folder
folder_path = "./StructuredData"

# Recursively search for files in the folder and its sub folders
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if (filename.endswith(".xlsx") and "modified" in filename) or filename.endswith(".pdf"):
            file_path = os.path.join(root, filename)
            os.remove(file_path)
            print(f"File '{filename}' removed.")
