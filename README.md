# Hospital-Bill-Extraction

This repository contains scripts for extracting hospital bills from the MiCare Portal. The main objective of this project is to automate the process of crawling and downloading hospital bills from the MiCare Portal for further analysis.

**Note:**
Due to limitations and drawbacks with Selenium Python, we had to switch to UiPath simulation to download the hospital bills after obtaining the URL Excel file using Selenium Python.

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/downloads/)

## Table of Contents

- [Introduction](#introduction)
- [MiCare Portal](#micare-portal)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The Hospital-Bill-Extraction project aims to automate the process of extracting hospital bills from the MiCare Portal, an online platform for managing medical bills. The provided scripts streamline the workflow, allowing users to retrieve and organize hospital bills efficiently.

## MiCare Portal

The MiCare Portal is an online platform ([https://eclaims.micaresvc.com/](https://eclaims.micaresvc.com/)) where users can access and manage their medical bills. This repository provides a solution to automate the extraction of hospital bills from this portal.

## Project Structure

The repository consists of the following Python files:

1. `main.py`: First step of the extraction process. It navigates to the MiCare Portal, performs the login process, and crawls the links for UiPath simulation.
2. `DownloadProcess/`: This folder contains the UiPath scripts for simulating the necessary actions to download the hospital bills. Please refer to the files in this folder for the complete automation process.
3. `CreateFolder.py`: Create folders and store the extracted information. Each folder is created to store a range of 2000 records for better organization and manageability.
4. `DistributeRowForBill.py`: Facilitates the distribution of data to the folders created in the previous step. It ensures that each folder contains a maximum of 2000 rows, optimizing organization and efficiency.
5. `Rename.py`: Rename the text file and Excel file within the folders in the `StructuredData/` directory to predefined names. It helps in standardizing the file naming convention for better organization and clarity.
6. `StoreClaim.py`: Store the claim numbers with existing links into a text file. It captures the claim numbers associated with bills that have valid links and saves them in a text file for further checking and reference purposes.
7. `GatherAllBills.py`: Records the downloaded hospital bills and stores the claim numbers in a text file called "Extracted_Bills.txt".
8. `CheckDownloadBill.py`: Validate whether a hospital bill has been successfully downloaded.
9. `RemoveRedundantFiles.py`: Remove redundant files that may accumulate during the debugging process of `CheckDownloadBill.py`.

Additionally, there are other files and directories related to the project. Each file is explained in detail in the subsequent sections.

## Usage

To use this project, follow the instructions below:

1. Clone the repository to your local machine.
2. Install the necessary dependencies (e.g., UiPath, Python packages).
3. Obtain the URL Excel file using the `main.py` script.
4. Open the `Main.xaml` file in UiPath Studio.
5. Configure the necessary settings and variables in UiPath to match your requirements.
6. Run the UiPath script to simulate the necessary actions and download the hospital bills.
7. Run the `CreateFolder.py` script to create folders.
8. Run the `DistributeRowForBill.py` script to distribute the data to the previously created folders.
9. Use the `Rename.py` script to standardize the file naming convention.
10. Run the `StoreClaim.py` script to store the claim numbers with existing links.
11. Run the `GatherAllBills.py` script to record the downloaded hospital bills.
12. Use the `CheckDownloadBill.py` script to validate whether a hospital bill has been successfully downloaded.
13. Optionally, use the `RemoveRedundantFiles.py` script to remove any redundant files.

Please refer to the individual script files and their corresponding sections in the README for more detailed information on their usage and functionality.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

## Acknowledgments

We would like to acknowledge the following resources and libraries that were instrumental in the development of this project:

- [MiCare Portal](https://eclaims.micaresvc.com/): The online portal for accessing and managing hospital bills.
- [UiPath](https://www.uipath.com/): The Robotic Process Automation (RPA) platform used for simulating the necessary actions.
- [Selenium Python](https://selenium-python.readthedocs.io/): The Python library used for web crawling (although not used in the final solution).
- [Pandas](https://pandas.pydata.org/): The Python library for data manipulation and analysis.
- [os](https://docs.python.org/3/library/os.html): The Python library for interacting with the operating system.
- [shutil](https://docs.python.org/3/library/shutil.html): The Python library for file operations and management.
- [urllib](https://docs.python.org/3/library/urllib.html): The Python library for handling URLs and network operations.

We are grateful to the developers and contributors of these tools and libraries for their valuable contributions to the project.
