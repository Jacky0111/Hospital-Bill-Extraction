import os


def count_pdf_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for f1 in files:
            if f1.endswith('.pdf'):
                count += 1
    return count


def find_pdf_files(directory):
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for f2 in files:
            if f2.endswith('.pdf'):
                pdf_files.append(os.path.splitext(f2)[0])
    return pdf_files


# Replace with the actual directory path
directory_path = os.path.abspath(r'.\Bill\Whole')

pdf_files_list = find_pdf_files(directory_path)
pdf_file_count = len(pdf_files_list)

print("Number of PDF files:", pdf_file_count)
print("PDF files list:", pdf_files_list)

# Store the list in a text file
output_file = os.path.join("StructuredData", "Extracted_Bills.txt")
with open(output_file, "w") as file:
    for pdf_file in pdf_files_list:
        file.write(pdf_file + "\n")

print(f'PDF files list saved to {output_file}, {len(pdf_files_list)} rows')
