import os
import pandas as pd

# Read the Excel file
df = pd.read_excel('Full_data_v2.xlsx')

# Get the total number of rows in the dataframe
total_rows = len(df)

# Define the chunk size
chunk_size = 2000

# Calculate the number of chunks required
num_chunks = total_rows // chunk_size + 1

# Create the folder if it doesn't exist
folder_path = 'StructuredData'
os.makedirs(folder_path, exist_ok=True)

# Split the dataframe into chunks
chunks = [df[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)]

# Iterate over each chunk
for i, chunk in enumerate(chunks):
    # Perform operations on each chunk (replace this with your own code)
    print(f"Processing chunk {i+1}/{num_chunks}")
    print(chunk)
    print()

    # Save each chunk to a separate Excel file in the folder
    file_path = os.path.join(folder_path, f"chunk_{i+1}.xlsx")
    chunk.to_excel(file_path, index=False)
