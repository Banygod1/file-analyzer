import magic
from pathlib import Path

#File path initialization
file_path = Path.home()

while True:

    #Current path
    print(f"Current directory: {file_path}")

    #File path input
    path_obj = input("Insert the path to the file: ")
    file_path = Path(path_obj)
        
    while not file_path.exists():
        print("This path does not exist. Please insert a valid file path.")
        path_obj = input("Insert the path to the file: ")
        file_path = Path(path_obj)

    #Print all files in current directory and re-prompt if it's a directory
    if file_path.is_dir():
        items = list(file_path.iterdir())
        if not items:
            print("This folder is empty.")
        else:
            for item in items:
                print(item.name)
        print("Please enter a path to a specific file, not just a directory.")
        continue

    #Get MIME type (file format) for a file path
    try:
        mime_type = magic.from_file(str(file_path), mime=True)
        #Get human-readable file description
        description = magic.from_file(str(file_path))
    except Exception as e:
        print(f"Could not analyze file {file_path}: {e}")
        continue

    #Print MIME type and description
    print(f"The file {file_path} has MIME type: {mime_type}")
    print(f"Description: {description}")

    #Print generic file type
    if mime_type.startswith("image/"):
        print("This is an image file.")

    elif mime_type.startswith("video/"):
        print("This is a video file.")

    elif mime_type.startswith("audio/"):
        print("This is an audio file.")

    elif mime_type.startswith("application/"):
        print("This is an application file.")

    elif mime_type.startswith("text/"):
        print("This is a text file.")

    #Continue analyze
    continue_analyze = input("Do you want to analyze another file? (y/n): ")
    if continue_analyze.lower() == "n":
        break
    elif continue_analyze.lower() == "y":
        analyze_file = True
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

print("Thank you for using the file analyzer!")