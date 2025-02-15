# Unzip Utility

**Unzip Utility** is a simple Python script that unzips a ZIP file for you. It's designed to be very easy to use—even if you're new to Python. Simply copy the code, paste it into a file, run it, and follow the on-screen instructions.

## How It Works

1. **File Check:** The script checks if the ZIP file exists.
2. **ZIP Validation:** It verifies that the file is a valid ZIP file.
3. **Folder Creation:** It creates the destination folder if it doesn't already exist.
4. **File Extraction:** It extracts the contents of the ZIP file into the specified folder.

## How to Use

1. **Copy the Code**

   Copy and paste the following code into a new file named `unzip.py`:

   ```python
   import os
   import zipfile

   def unzip_file(zip_path, extract_to):
       # Check if the provided zip file exists
       if not os.path.exists(zip_path):
           print(f"Error: The file {zip_path} does not exist.")
           return

       # Check if the provided file is a ZIP file
       if not zipfile.is_zipfile(zip_path):
           print(f"Error: The file {zip_path} is not a valid zip file.")
           return

       # Create the extraction directory if it doesn't exist
       if not os.path.exists(extract_to):
           os.makedirs(extract_to)

       # Extract the ZIP file
       try:
           with zipfile.ZipFile(zip_path, 'r') as zip_ref:
               zip_ref.extractall(extract_to)
               print(f"Files extracted to: {extract_to}")
       except Exception as e:
           print(f"An error occurred while extracting the zip file: {e}")


   if __name__ == "__main__":
       print("Unzip Utility")
       print("-------------")
       zip_file_path = input("Enter the path to the zip file: ").strip()
       extract_directory = input("Enter the directory where files should be extracted: ").strip()

       unzip_file(zip_file_path, extract_directory)

   Run the Script

2. **Run the Script**

   - Open your terminal or command prompt.
   - Navigate to the folder where you saved `unzip.py`.
   - Run the script using the following command:

     ```bash
     python unzip.py
     ```

3. **Follow the Prompts**

   - When prompted, **enter the path to your ZIP file.**
   - Next, **enter the folder where you want the files to be extracted.**
   - The script will extract the files into the specified folder.

## Requirements

- **Python 3** must be installed on your computer.

## Author

**Greeshma Surya**


