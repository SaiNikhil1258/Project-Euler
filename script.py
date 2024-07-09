import os


def rename_files():
    """
    Renames files in the current directory with a leading zero padding.

    This script assumes the script itself is located in the same directory as the files to be renamed.
    """
    current_dir = os.getcwd()  # Get the current working directory
    print(current_dir)
    for filename in os.listdir(current_dir):
        if filename.startswith("p") and filename != ".gitignore":
            parts = filename.split("_")
            file_number = int(parts[0][1:])
            # print(file_number)
            if file_number < 10:
                new_number = f"00{file_number}"
            else:
                new_number = f"0{file_number}"

            new_file_name = f"p{new_number}_{'_'.join(parts[1:])}"
            # print(f"{filename} -> {new_file_name}")
            try:
                os.rename(
                    os.path.join(current_dir, filename),
                    os.path.join(current_dir, new_file_name),
                )
            except OSError as error:
                print(error)


rename_files()

print("completed")
