import cv2
import numpy as np

# ASCII characters from light to dark
ASCII_CHARS = " .:-=+*%#"

def reshape_image(img):
    # Resize while maintaining aspect ratio
    aspect_ratio = img.shape[1] / img.shape[0]
    width = int(img.shape[1]/3)
    height = int(width / aspect_ratio * 0.5)  # Adjust the factor based on your text editor
    return cv2.resize(img, (width, height))

def edges_ascii(img, width=400):
   
    # Adjust image size
    reshaped_img = reshape_image(img)

    # edge detection
    edges = cv2.Canny(reshaped_img, 100, 200)

    # convert to ascii
    edges_ascii = ""
    for row in edges:
        for pixel in row:
            # Map pixel intensity to ASCII character
            edges_ascii += ASCII_CHARS[min(int((pixel / 255) * len(ASCII_CHARS)), len(ASCII_CHARS)-1)]  # Normalize pixel intensity
        edges_ascii += "\n"

    return edges_ascii

def contrast_ascii(img, width=400):
   
    # Adjust image size
    reshaped_img = reshape_image(img)

    # increase contrast
    alpha = 1.5  # Contrast control
    beta = -70  # Brightness control
    contrast_img = cv2.convertScaleAbs(reshaped_img, alpha=alpha, beta=beta)

    # convert to ascii
    contrast_ascii = ""
    for row in contrast_img:
        for pixel in row:
            contrast_ascii += ASCII_CHARS[min(int((pixel / 255) * len(ASCII_CHARS)), len(ASCII_CHARS)-1)]  # Normalize pixel intensity
        contrast_ascii += "\n"
    
    return contrast_ascii

def blended_ascii(img, width=400):

    # Adjust image size
    reshaped_img = reshape_image(img)

    #edge detection
    edges = cv2.Canny(reshaped_img, 100, 200)
    
    # increase contrast
    alpha = 1.3  # Contrast control
    beta = -70  # Brightness control
    contrast_img = cv2.convertScaleAbs(reshaped_img, alpha=alpha, beta=beta)

    blended_img = cv2.addWeighted(contrast_img, 0.6, edges, 0.2, 0)  # Blend grayscale and edge-detected images

    # convert to ascii
    blended_ascii = ""
    for row in blended_img:
        for pixel in row:
            blended_ascii += ASCII_CHARS[min(int((pixel / 255) * len(ASCII_CHARS)), len(ASCII_CHARS)-1)]  # Normalize pixel intensity
        blended_ascii += "\n"
    
    return blended_ascii

def ascii_to_image(ascii_text, font_scale=.8, thickness=2, font=cv2.FONT_HERSHEY_SIMPLEX):

    # Split the ASCII art into rows
    ascii_rows = ascii_text.split("\n")
    
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
            
    return img


# read in original image
image_path = "photos/maa.jpg"
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# convert to ascii
ascii_text = contrast_ascii(img)

# Save ascii text to a text file
ascii_output_path = "output/ascii_output.txt"
with open(ascii_output_path, "w") as file:
    file.write(ascii_text)
print("ascii text saved to output/ascii_output.txt")

#convert ascii text to image
ascii_img = ascii_to_image(ascii_text)


# Save the image as a JPEG
image_output_path = "output/ascii_image.jpg"  
cv2.imwrite(image_output_path, ascii_img)

print("ascii image saved to output/ascii_image.jpg")
