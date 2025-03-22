# Main.py created by Caden Ziskie with the help of ChatGPT

from Pic2ASCII import image_to_ascii, save_ascii_art
from PaintingSquirrel import loadingSquirrel
from camie import webcamShot
import os
import platform

def main():
    print("A terminal JPG to ASCII conversion program now with 100% more squirrels.\nPlease select a mode of operation: ")
    print("[1] Picture File")
    print("[2] Webcam")
    print("[3] Quit")

    while True:
        modeOfOperation = input("Select mode: ")

        # Code from https://www.geeksforgeeks.org/switch-case-in-python-replacement/
        match modeOfOperation:
            case '1':
                pictureFile()
                break
            case '2':
                webcam()
                break
            case '3':
                break
            case _:
                pass

    closePrgm()

def closePrgm():
    # All of this multi-line string is contained in closePrgm
        closingFrame = r""" 
 (\__/)
 (o'^'o)
(")___(|)
       v
    ----
    |:(|
    ----
"""
        print(closingFrame)
        print("Sad to see you go. Come back again with nuts!")

def pictureFile():
    # Filepath: Asking for the file path to the image
    while True:
        print("Please give a file path to the picture (e.g., /path/to/image.jpg): ")
        filePath = input()

        # Ensure the file has a .jpg extension if not provided
        if not filePath.endswith(".jpg"):
            filePath += ".jpg"

        # Check if the file path exists
        try:
            with open(filePath, 'rb') as file:
                pass
            break
        except FileNotFoundError:
            print(f"Error: The file '{filePath}' does not exist. Please try again.")

    ascii_art = image_to_ascii(filePath, new_width=150)  # Adjust width for better output
    loadingSquirrel(2)
    saveASCIIImage(ascii_art)

def webcam():
    # All of this multi-line string is contained in function
    webcamControlsFrame = r""" 
 (\__/)
 (o'.'o)
(")___(|)
       v
    ----
    |:p|
    ----
"""
    
    print(webcamControlsFrame)
    print("To take a picture, press the spacebar\nTo close webcam window, press escape")
    print("Please wait for window to appear, can take a min")

    ascii_art = image_to_ascii(webcamShot(), new_width=150)  # Adjust width for better output
    loadingSquirrel(2)
    saveASCIIImage(ascii_art)
    return

def get_pictures_folder():
    home_dir = os.path.expanduser("~")

    if platform.system() == "Windows":
        pictures_folder = os.path.join(home_dir, "Pictures")
    elif platform.system() == "Darwin":  # macOS
        pictures_folder = os.path.join(home_dir, "Pictures")
    else:  # Linux
        pictures_folder = os.path.join(home_dir, "Pictures")

    return pictures_folder

def saveASCIIImage(ASCII):
    print("Please give a name to save the file as: ")
    saveAs = input()

    # Check if that file already exists?

    # Ensure the file has a .txt extension if not provided
    if not saveAs.endswith(".txt"):
        saveAs += ".txt"

    pictures_folder = get_pictures_folder()
    os.makedirs(pictures_folder, exist_ok=True)
    file_path = os.path.join(pictures_folder, saveAs)

    with open(file_path, "w") as file:
        file.write(ASCII)

    print(f"File saved to {file_path}")

if __name__ == "__main__":
    main()
