import os
import shutil
import pandas as pd


def read_extracted_bills_data(fp):
    with open(fp, "r") as file:
        extracted = file.read().splitlines()
    return extracted


def process_text_file(fp):
    with open(fp, "r") as file:
        return file.readlines()


def update_dataframe(data, compare1, compare2, path, fp):
    data['Download?'] = False
    data['Download?'] = data['Download?'].astype(object)
    match_list = []
    for row in compare2:
        if row.strip() in compare1:
            match_list.append(row.strip())
            data.loc[data['ClaimNo'] == row.strip(), 'Download?'] = True
            pdf_file_path = os.path.join(path, row.strip() + ".pdf")
            shutil.copy(pdf_file_path, fp)
            print("PDF file copied:", pdf_file_path)
    modified_file_path = os.path.splitext(file_path)[0] + "_modified.xlsx"
    data.to_excel(modified_file_path, index=False)
    print("Modified Excel file saved as:", modified_file_path)
    return match_list


def save_non_matching_rows(text, m, fp):
    non_matches = [row for row in text if row.strip() not in m]
    with open(os.path.join(fp, "ClaimNo.txt"), "w") as txt_file:
        txt_file.write("".join(non_matches))


# Define the directory path where the files are located
directory_path = 'StructuredData\\'
data_path = 'Bill\Whole\\'
txt_data = None

# Read the "Extracted_Bills.txt" file at the beginning
extracted_bills_file_path = os.path.join(directory_path, "Extracted_Bills.txt")
extracted_bills_data = read_extracted_bills_data(extracted_bills_file_path)

# Iterate over each folder within the directory
for folder_name in os.listdir(directory_path):
    folder_path = os.path.join(directory_path, folder_name)

    # Check if the current item in the directory is a folder
    if os.path.isdir(folder_path):
        print("\nFolder:", folder_name)

        # Iterate over each file within the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            print(file_path)

            # Check if the file is a text file (TXT)
            if file_name.endswith(".txt"):
                txt_data = process_text_file(file_path)
                print("Contents of", file_name + ":")

            # Check if the file is an Excel file (XLSX)
            elif file_name.endswith(".xlsx"):
                df = pd.read_excel(file_path)
                matches = update_dataframe(df, extracted_bills_data, txt_data, data_path, folder_path)
                save_non_matching_rows(txt_data, matches, folder_path)
