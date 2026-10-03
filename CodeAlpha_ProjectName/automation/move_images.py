import os
import shutil

def move_jpg_files(source_folder, dest_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Created folder: {dest_folder}")

    moved_count = 0

    # List all items in source folder
    for filename in os.listdir(source_folder):
        # Build full path
        src_path = os.path.join(source_folder, filename)

        # Skip if it's not a file (e.g., it's a subfolder)
        if not os.path.isfile(src_path):
            continue

        # Check if file ends with .jpg or .JPG
        if filename.lower().endswith(".jpg"):
            dest_path = os.path.join(dest_folder, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved: {filename}")
            moved_count += 1

    print(f"Total .jpg files moved: {moved_count}")
    print(f"All .jpg files are now in: {dest_folder}")

if __name__ == "__main__":
    print("=== JPG File Mover ===")

    # TODO: Change this path to your test_source folder
    source = r"C:\Users\HEMA HASINI\OneDrive\Desktop\CodeAlpha_ProjectName\automation\test__source"

    # Simple validation
    if not os.path.isdir(source):
        print("Invalid folder path. Please check the 'source' variable in the code.")
    else:
        destination = os.path.join(source, "images_only")

        print(f"Moving all .jpg files from:{source}to:{destination}")
        move_jpg_files(source, destination)

    print("Done.")