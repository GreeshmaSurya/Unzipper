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
