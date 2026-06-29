import os
import shutil
import logging

# Log Configuration
logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

print("========== FILE AUTOMATION SCRIPT ==========")

folder = input("Enter folder path: ")

if not os.path.exists(folder):
    print("Folder not found!")
    exit()

try:

    count = 1

    for file in os.listdir(folder):

        filepath = os.path.join(folder, file)

        if os.path.isfile(filepath):

            filename, extension = os.path.splitext(file)

            new_name = f"File_{count}{extension}"

            new_path = os.path.join(folder, new_name)

            os.rename(filepath, new_path)

            logging.info(f"Renamed {file} -> {new_name}")

            count += 1

    print("Files Renamed Successfully!")

    categories = {
        ".jpg": "Images",
        ".png": "Images",
        ".jpeg": "Images",
        ".pdf": "PDFs",
        ".txt": "TextFiles",
        ".mp3": "Music",
        ".mp4": "Videos"
    }

    for file in os.listdir(folder):

        filepath = os.path.join(folder, file)

        if os.path.isfile(filepath):

            extension = os.path.splitext(file)[1].lower()

            folder_name = categories.get(extension, "Others")

            destination = os.path.join(folder, folder_name)

            os.makedirs(destination, exist_ok=True)

            shutil.move(filepath, os.path.join(destination, file))

            logging.info(f"Moved {file} to {folder_name}")

    print("Files Sorted Successfully!")

except Exception as e:

    logging.error(str(e))

    print("Error:", e)