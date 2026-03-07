import argparse
import magic
from pathlib import Path

#Metadata return logic
def analyze_file(file_path: Path) -> bool:
    """Analyze a file and print MIME type and description. Returns True if successful."""
    try:
        mime_type = magic.from_file(str(file_path), mime=True)
        description = magic.from_file(str(file_path))
    except Exception as e:
        print(f"Could not analyze file {file_path}: {e}")
        return False

    print(f"The file {file_path} has MIME type: {mime_type}")
    print(f"Description: {description}")

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
    return True


def main():
    parser = argparse.ArgumentParser(description="Analyze a file and show its MIME type and description.")
    parser.add_argument("path", nargs="?", help="Path to the file to analyze (optional; if omitted, runs interactively)")
    args = parser.parse_args()

    # If a path was given as an argument on the command line, analyze it and exit
    if args.path is not None:
        path_str = args.path.strip()
        if len(path_str) == 2 and path_str[1] == ":" and path_str[0].isalpha():
            path_str += "\\"
        file_path = Path(path_str)
        if not file_path.exists():
            print(f"This path does not exist: {file_path}")
            return
        if file_path.is_dir():
            items = list(file_path.iterdir())
            if not items:
                print("This folder is empty.")
            else:
                for item in items:
                    print(item.name)
            print("Please pass a path to a specific file, not a directory.")
            return
        analyze_file(file_path)
        print("Thank you for using the file analyzer!")
        return

    # No argument: run interactive loop
    file_path = Path.home()
    while True:
        print(f"Current directory: {file_path}")

        path_obj = input("Insert the path to the file: ")
        path_str = path_obj.strip()

        #If file path starts with something like C: or D:, let the command line interpret it as a Drive.
        if len(path_str) == 2 and path_str[1] == ":" and path_str[0].isalpha():
            path_str += "\\"
        file_path = Path(path_str)

        #Reprompt for file path if given path doesn`t exist
        while not file_path.exists():
            print("This path does not exist. Please insert a valid file path.")
            path_obj = input("Insert the path to the file: ")
            path_str = path_obj.strip()
            if len(path_str) == 2 and path_str[1] == ":" and path_str[0].isalpha():
                path_str += "\\"
            file_path = Path(path_str)

        #Folder behavior logic
        if file_path.is_dir():
            items = list(file_path.iterdir())
            if not items:
                print("This folder is empty.")
            else:
                for item in items:
                    print(item.name)
            print("Please enter a path to a specific file, not just a directory.")
            continue

        if not analyze_file(file_path):
            continue

        continue_analyze = input("Do you want to analyze another file? (y/n): ")
        if continue_analyze.lower() == "n":
            break
        if continue_analyze.lower() != "y":
            print("Invalid input. Please enter 'y' or 'n'.")

    print("Thank you for using the file analyzer!")


if __name__ == "__main__":
    main()