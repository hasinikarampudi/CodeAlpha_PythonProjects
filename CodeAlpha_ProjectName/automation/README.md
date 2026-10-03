# Task Automation: Move JPG Files

A Python script that automates moving all `.jpg` files from a source folder to a new subfolder.

## Description

- The script scans a given folder for files ending with `.jpg` or `.JPG`.
- It creates a new folder named `images_only` inside the source folder.
- All image files are moved into this new folder.
- Other files (e.g., `.txt`, `.pdf`) remain in the original folder.

This demonstrates practical file handling and automation using Python’s standard library.

## Features

- Automatically creates the destination folder if it doesn’t exist.
- Case-insensitive `.jpg` detection (`.jpg`, `.JPG`, etc.).
- Prints a summary of how many files were moved.
- Uses only built-in modules: `os` and `shutil`.

## How to Use

1. Make sure you have Python installed (Python 3.x recommended).
2. Open the `automation` folder.
3. Edit `move_images.py` and set the `source` variable to your desired folder path, e.g.:
   ```python
   source = r"C:UsersYourNamepath\toyour\folder"