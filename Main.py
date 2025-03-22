# Main.py created by Caden Ziskie with the help of ChatGPT

from PaintingSquirrel import loadingSquirrel
from camie import webcamShot
from convert_to_ascii import convertToEdgeASCIIJpg, convertToEdgeASCIITxt, convertToContrastASCIIJpg, convertToContrastASCIITxt, process_video
import os
import platform
import time
import cv2

def main():
    logo = r""" 
         __                                                 __     __
        /\_\                                               /\_\   /\_\
 ______ \/_/_     ______     ______     ______     ______  \/_/_  \/_/_
/\  __ \  /\ \   /\  ___\   /\____ \   /\  ___\   /\  ___\   /\ \   /\ \   
\ \ \_\ \ \ \ \  \ \ \____  \ \  __ \  \ \___  \  \ \ \____  \ \ \  \ \ \  
 \ \  ___\ \ \_\  \ \_____\  \ \_____\  \/\_____\  \ \_____\  \ \_\  \ \_\ 
  \ \ \__/  \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/   \/_/ 
   \ \ \                                   BY JOCALEXRYEM
    \/_/
    """

    print(logo, "\n")
    print("Please select a mode of operation: ")
    print("[1] Picture File")
    print("[2] Webcam (pictures only)")
    print("[3] Video File")
    print("[4] Quit")

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
                videoFile()
                break
            case '4':
                break
            case _:
                pass

    closePrgm()

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

    # Select what style of ASCII conversion, then convert and play loading animation
    while True:
        print("Please select a conversion style: ")
        print("[1] Outline")
        print("[2] Texture")
        print("[3] Quit")
        conversionStyle = input("Select mode: ")

        match conversionStyle:
            case '1':
                loadingSquirrel(2)
                saveASCIIImage(filePath, '1')
                break
            case '2':
                loadingSquirrel(2)
                saveASCIIImage(filePath, '2')
                break
            case '3':
                break
            case _:
                pass

def webcam():
    print("To take a picture, press the spacebar\nTo close webcam window, press escape")

    # Select what style of ASCII conversion, then call webcamShot to get a pic, convert and play loading animation
    while True:
        print("Please select a conversion style: ")
        print("[1] Outline")
        print("[2] Texture")
        print("[3] Quit")
        conversionStyle = input("Select mode: ")

        match conversionStyle:
            case '1':
                saveASCIIImage(webcamShot(), '1')
                loadingSquirrel(2)
                break
            case '2':
                saveASCIIImage(webcamShot(), '2')
                loadingSquirrel(2)
                break
            case '3':
                break
            case _:
                pass

def videoFile():
    print("Please give a file path to the video (e.g., /path/to/video): ")
    filePath = input("Select file path: ")

    print("Please give a file path for the output file (e.g., /path/to/output): ")
    outputPath = input("Select output path: ")

    print("Please select a conversion style: ")
    print("[1] Outline")
    print("[2] Texture")
    print("[3] Quit")
    conversionStyle = input("Select mode: ")
    
    process_video(filePath, outputPath, conversionStyle)

def get_pictures_folder():
    home_dir = os.path.expanduser("~")

    if platform.system() == "Windows":
        pictures_folder = os.path.join(home_dir, "Pictures")
    elif platform.system() == "Darwin":  # macOS
        pictures_folder = os.path.join(home_dir, "Pictures")
    else:  # Linux
        pictures_folder = os.path.join(home_dir, "Pictures")

    return pictures_folder

def saveASCIIImage(ASCII, style):
    print("Please give a name to save the file as: ")
    saveAs = input("Save as: ")

    # Select output file format
    while True:
        print("Please select a file format: ")
        print("[1] .jpg")
        print("[2] .txt")
        print("[3] Quit")
        fileFormat = input("Select format: ")

        fileFormat = fileFormat + style # Add style to string for follwing switch cases

        match fileFormat:
            case '11': # jpg outline
                # Ensure the file has a .jpg extension if not provided
                if not saveAs.endswith(".jpg"):
                    saveAs += ".jpg"

                # Get path to user's Pictures folder
                pictures_folder = get_pictures_folder()
                os.makedirs(pictures_folder, exist_ok=True)
                file_path = os.path.join(pictures_folder, saveAs)

                # Call requested conversion type
                ascii_art = convertToEdgeASCIIJpg(ASCII)

                # Save file
                with open(file_path, "w") as file: 
                    cv2.imwrite(file_path, ascii_art)

                break
            case '12': # jpg texture
                if not saveAs.endswith(".jpg"):
                    saveAs += ".jpg"

                pictures_folder = get_pictures_folder()
                os.makedirs(pictures_folder, exist_ok=True)
                file_path = os.path.join(pictures_folder, saveAs)

                ascii_art = convertToContrastASCIIJpg(ASCII)

                with open(file_path, "w") as file: 
                    cv2.imwrite(file_path, ascii_art)

                break
            case '21': # txt outline
                if not saveAs.endswith(".txt"):
                    saveAs += ".txt"

                pictures_folder = get_pictures_folder()
                os.makedirs(pictures_folder, exist_ok=True)
                file_path = os.path.join(pictures_folder, saveAs)

                ascii_art = convertToEdgeASCIITxt(ASCII)

                with open(file_path, "w") as file:
                    file.write(ascii_art)

                break
            case '22': # txt texture
                if not saveAs.endswith(".txt"):
                    saveAs += ".txt"

                pictures_folder = get_pictures_folder()
                os.makedirs(pictures_folder, exist_ok=True)
                file_path = os.path.join(pictures_folder, saveAs)

                ascii_art = convertToContrastASCIITxt(ASCII)

                with open(file_path, "w") as file:
                    file.write(ascii_art)

                break
            case '3':
                break
            case _:
                pass

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
        print("Sad to see you go. Come back again!")

if __name__ == "__main__":
    main()
