import os
import shutil
import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel("Sample Hospital Bills for POC.xlsx")

# Create an empty list to store claim numbers
claim_numbers = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Check if the "Extracted?" column value is "Y"
    if row["Extracted?"] == "Y":
        # Store the "ClaimNo" column value in the list
        claim_numbers.append(row["ClaimNo"])


# Create the "Samples" folder if it doesn't exist
if not os.path.exists("Samples"):
    os.makedirs("Samples")

# Iterate through each claim number
for cn in claim_numbers:
    # Build the file path to the PDF in the "\Bill\Whole" folder
    pdf_file_path = os.path.join("Bill\\Whole", cn + ".pdf")

    # Check if the PDF file exists
    if os.path.isfile(pdf_file_path):
        # Copy the PDF file to the "Samples" folder
        destination_path = os.path.join("Samples", cn + ".pdf")
        shutil.copy(pdf_file_path, destination_path)
