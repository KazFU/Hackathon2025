# Main.py created by Caden Ziskie with the help of ChatGPT

from Pic2ASCII import image_to_ascii, save_ascii_art
from PaintingSquirrel import loadingSquirrel
from camie import webcamShot
from convert_to_ascii import convertToEdgeASCII, convertToContrastASCII
import os
import platform
import time
import cv2

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
        filePath = input("Select file path: ")

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

    while True:
        print("Please select a conversion style: ")
        print("[1] Outline")
        print("[2] Texture")
        print("[3] Quit")
        conversionStyle = input("Select mode: ")

        match conversionStyle:
            case '1':
                ascii_art = convertToEdgeASCII(filePath)
                loadingSquirrel(2)
                saveASCIIImage(ascii_art)
                break
            case '2':
                ascii_art = convertToContrastASCII(filePath)
                loadingSquirrel(2)
                saveASCIIImage(ascii_art)
                break
            case '3':
                break
            case _:
                pass

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
    print("To take a picture, press the spacebar, then press space again to close preview\nTo close webcam window, press escape")
    print("Please wait for window to appear, can take a min")
    time.sleep(3)

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
    saveAs = input("Save as: ")

    while True:
        print("Please select a file format: ")
        print("[1] .jpg")
        print("[2] .txt")
        print("[3] Quit")
        fileFormat = input("Select format: ")

        match fileFormat:
            case '1':
                # Ensure the file has a .jpg extension if not provided
                if not saveAs.endswith(".jpg"):
                    saveAs += ".jpg"

                pictures_folder = get_pictures_folder()
                os.makedirs(pictures_folder, exist_ok=True)
                file_path = os.path.join(pictures_folder, saveAs)

                with open(file_path, "w") as file: 
                    cv2.imwrite(file_path, ASCII)

                break
            case '2':
                # Ensure the file has a .txt extension if not provided
                if not saveAs.endswith(".txt"):
                    saveAs += ".txt"

                pictures_folder = get_pictures_folder()
                os.makedirs(pictures_folder, exist_ok=True)
                file_path = os.path.join(pictures_folder, saveAs)

                with open(file_path, "w") as file:
                    file.write(ASCII)

                break
            case '3':
                break
            case _:
                pass

    print(f"File saved to {file_path}")

if __name__ == "__main__":
    main()
