import os
import pandas as pd


def get_range_key(row_number):
    range_start = ((row_number - 1) // 2000) * 2000 + 1
    range_end = range_start + 1999
    return range_start, range_end


def store_claim_numbers(data, folder_path):
    claim_lists = {}

    # Iterate over the rows of the DataFrame
    for index, row in data.iterrows():
        claim_no = row['ClaimNo']
        row_number = index + 1  # Adding 1 to match the row number starting from 1
        range_key = get_range_key(row_number)

        # Check if the range key exists in the dictionary, if not, create an empty list
        if range_key not in claim_lists:
            claim_lists[range_key] = []

        # Check if the claim number is SYSTEMAUTO
        if row['Type'] == 'SYSTEMAUTO':
            claim_no = claim_no + '_2'

        # Append the claim number to the respective list based on the range key
        claim_lists[range_key].append(claim_no)

    # Read the claim numbers to remove from the text file
    file_path_remove = folder_path + "\\blank_claim_no.txt"
    if os.path.exists(file_path_remove):
        with open(file_path_remove, 'r') as file:
            blank_claim_nos = [line.strip() for line in file]
    else:
        blank_claim_nos = []

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Store the claim numbers in their respective files
    for range_key, claim_list in claim_lists.items():
        range_start, range_end = range_key
        file_name = f"{range_start}-{range_end}\Range_{range_start}-{range_end}.txt"
        file_path = os.path.join(folder_path, file_name)

        # Filter claim numbers not in the blank_claim_nos list
        filtered_claim_list = [claim for claim in claim_list if claim not in blank_claim_nos]

        # Write the claim numbers to the file
        with open(file_path, 'w') as file:
            for claim in filtered_claim_list:
                file.write(str(claim) + '\n')

        print(f"File saved: {file_path}")


# Read the Excel file
df = pd.read_excel('micare_data_ori.xlsx')

# Specify the folder path to store the files
fp = r"StructuredData"

# Store the claim numbers in their respective files
store_claim_numbers(df, fp)
