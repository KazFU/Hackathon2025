# Main.py created by Caden Ziskie with the help of ChatGPT

from Pic2ASCII import image_to_ascii, save_ascii_art
from PaintingSquirrel import loadingSquirrel

def main():
    print("A terminal JPG to ASCII conversion program now with 100% more squirrels.\n Please select a mode of operation: ")
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
                print("case 2")
                break
            case '3':
                break
            case _:
                pass

    # Close program
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
    save_ascii_art(ascii_art, saveAs)

def webcam():
    # Implement stuff here
    return

def saveImage():
    # Save As
    print("Please give a name to save the file as: ")
    saveAs = input()

    # Check if that file already exists?

    # Ensure the file has a .txt extension if not provided
    if not saveAs.endswith(".txt"):
        saveAs += ".txt"

if __name__ == "__main__":
    main()
