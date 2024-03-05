import pandas as pd
import os
import os.path

# Step 2: Read Excel file
excel_file = "Full_data_v2.xlsx"
data = pd.read_excel(excel_file)

# Step 3: Store "ClaimNo" into a list when "Type" is not null, with "_2" for 'SYSTEMAUTO'
claim_numbers = []
for index, row in data.iterrows():
    claim_no = row['ClaimNo']
    claim_type = row['Type']
    if pd.notnull(claim_type):
        if claim_type == 'SYSTEMAUTO':
            claim_no += '_2'
        claim_numbers.append(claim_no)

# Step 4: Store "ClaimNo" list into a text file
claim_numbers_file = "claim_numbers.txt"
with open(claim_numbers_file, 'w') as file:
    for claim_number in claim_numbers:
        file.write(str(claim_number) + '\n')

# Step 5: Extract entity pdf file names into a list and store in a text file
pdf_files_dir = "C:/Hospital Bill/Bill"
pdf_files = [os.path.splitext(file)[0] for file in os.listdir(pdf_files_dir) if file.endswith('.pdf')]

pdf_files_list_file = "pdf_files_list.txt"
with open(pdf_files_list_file, 'w') as file:
    for pdf_file in pdf_files:
        file.write(pdf_file + '\n')

# Step 6: Read 4th and 5th text files and compare them
with open(claim_numbers_file, 'r') as file:
    claim_numbers_list = file.read().splitlines()

with open(pdf_files_list_file, 'r') as file:
    pdf_files_list = file.read().splitlines()

# Step 7: Find values in the 5th text file not present in the 4th text file
unmatched_values = [value for value in pdf_files_list if value not in claim_numbers_list]

# Step 8: Display the final list
print("Unmatched Values:")
for value in unmatched_values:
    print(value)
