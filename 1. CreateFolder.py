import os


def create_folders(start, end, step, path):
    # Create the path if it doesn't exist
    os.makedirs(path, exist_ok=True)

    # Create the folders within the specified path
    for i in range(start, end + 1, step):
        folder_name = f"{i}-{i + step - 1}"
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path, exist_ok=True)


# Specify the desired path
fp = r"C:\Users\ChiaChungLim\PycharmProjects\Hospital-Bill-Extraction\StructuredData"

# Call the function to create folders
create_folders(1, 64000, 2000, fp)
