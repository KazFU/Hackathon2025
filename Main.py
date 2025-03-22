from Pic2ASCII import image_to_ascii, save_ascii_art
from PaintingSquirrel import loadingSquirrel

def main():
    print("A terminal JPG to ASCII conversion program now with 100% more squirrels.")

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

    # Save As
    print("Please give a name to save the file as: ")
    saveAs = input()

    # Ensure the file has a .txt extension if not provided
    if not saveAs.endswith(".txt"):
        saveAs += ".txt"

    print("Now converting...")
    ascii_art = image_to_ascii(filePath, new_width=150)  # Adjust width for better output
    loadingSquirrel(2)
    save_ascii_art(ascii_art, saveAs)

if __name__ == "__main__":
    main()
