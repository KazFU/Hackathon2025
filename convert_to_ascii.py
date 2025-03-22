import cv2
import numpy as np

# ASCII characters from light to dark
ASCII_CHARS = " .:-=+*%#"


def edges_ascii(image_path, width=400):
    # Load image and convert to grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize while maintaining aspect ratio
    aspect_ratio = img.shape[1] / img.shape[0]
    height = int(width / aspect_ratio * 0.5)  # Adjust the factor based on your text editor
    img = cv2.resize(img, (width, height))

    # Apply Canny edge detection
    edges = cv2.Canny(img, 100, 200)

    # Normalize intensities to ASCII character range
    edges_ascii = " #"
    for row in edges:
        for pixel in row:
            # print(min(int((pixel / 255) * len(ASCII_CHARS)), len(ASCII_CHARS)-1))
            # Map pixel intensity to ASCII character
            edges_ascii += ASCII_CHARS[min(int((pixel / 255) * len(ASCII_CHARS)), len(ASCII_CHARS)-1)]  # Normalize pixel intensity
        edges_ascii += "\n"
    
    return edges_ascii

def contrast_ascii(image_path, width=400):
    # Load image and convert to grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize while maintaining aspect ratio
    aspect_ratio = img.shape[1] / img.shape[0]
    height = int(width / aspect_ratio * 0.4)  # Adjust the factor based on your text editor
    img = cv2.resize(img, (width, height))

    alpha = 1.5  # Contrast control
    beta = -70  # Brightness control
    contrast_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    # Normalize intensities to ASCII character range
    contrast_ascii = ""
    for row in contrast_img:
        for pixel in row:
            # print(min(int((pixel / 255) * len(ASCII_CHARS)), len(ASCII_CHARS)-1))
            # Map pixel intensity to ASCII character
            contrast_ascii += ASCII_CHARS[min(int((pixel / 255) * len(ASCII_CHARS)), len(ASCII_CHARS)-1)]  # Normalize pixel intensity
        contrast_ascii += "\n"
    
    return contrast_ascii

def blended_ascii(image_path, width=400):
    # Load image and convert to grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize while maintaining aspect ratio
    aspect_ratio = img.shape[1] / img.shape[0]
    height = int(width / aspect_ratio * 0.5)  # Adjust the factor based on your text editor
    img = cv2.resize(img, (width, height))

    # Apply Canny edge detection
    edges = cv2.Canny(img, 100, 200)
    

    alpha = 1.5  # Contrast control
    beta = -70  # Brightness control
    contrast_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    blended_img = cv2.addWeighted(contrast_img, 0.6, edges, 0.2, 0)  # Blend grayscale and edge-detected images

    # Normalize intensities to ASCII character range
    blended_ascii = ""
    for row in blended_img:
        for pixel in row:
            # print(min(int((pixel / 255) * len(ASCII_CHARS)), len(ASCII_CHARS)-1))
            # Map pixel intensity to ASCII character
            blended_ascii += ASCII_CHARS[min(int((pixel / 255) * len(ASCII_CHARS)), len(ASCII_CHARS)-1)]  # Normalize pixel intensity
        blended_ascii += "\n"
    
    return blended_ascii

def ascii_to_image(ascii_file_path, output_image_path, font_scale=0.5, thickness=1, font=cv2.FONT_HERSHEY_SIMPLEX):
    # Read the ASCII art from the file
    with open(ascii_file_path, 'r') as file:
        ascii_art = file.read()

    # Split the ASCII art into rows
    ascii_rows = ascii_art.split("\n")
    
    # Set the dimensions of the output image
    height = len(ascii_rows) * 20  # Height based on number of rows
    width = max(len(row) for row in ascii_rows) * 12  # Width based on longest row

    # Create a blank white canvas to draw the ASCII characters
    img = np.zeros((height, width), dtype=np.uint8)  

    # Set text position to start drawing
    y0, dy = 30, 30  # Starting y-position and line height

    # Iterate through each row of the ASCII art
    for i, row in enumerate(ascii_rows):
        x0 = 10  # Starting x-position
        for j, char in enumerate(row):
            if char != ' ':
                # Draw each character at the corresponding position
                cv2.putText(img, char, (x0, y0 + i * dy), font, font_scale, (255,255,255), thickness, lineType=cv2.LINE_AA)
            x0 += 12  # Move the x-position for the next character
            
    # Save the image as a JPEG
    cv2.imwrite(output_image_path, img)



# Example usage
image_path = "squirrel.jpg"
ascii_output = contrast_ascii(image_path)
ascii_output_path = "ascii_output.txt"

# Save ASCII art to a text file
with open(ascii_output_path, "w") as file:
    file.write(ascii_output)

image_output_path = "ascii_image.jpg"  # Output image file
ascii_to_image(ascii_output_path, image_output_path)

# Optionally print to console as well
# print(ascii_output)

print("ASCII art saved to image.txt")
