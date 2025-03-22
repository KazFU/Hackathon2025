import cv2
import numpy as np

# ASCII characters from light to dark
ASCII_CHARS = " .:-=+*%#"
def reshape_image(img):
    # Resize while maintaining aspect ratio
    aspect_ratio = img.shape[1] / img.shape[0]
    width = int(img.shape[1]/3)
    height = int(width / aspect_ratio * .4)  # Adjust the factor based on your text editor
    return cv2.resize(img, (width, height))

def edges_ascii(img, width=400):
   
    # Adjust image size+++
    reshaped_img = reshape_image(img)

    # edge detection
    edges_img = cv2.Canny(reshaped_img, 100, 200)

     # Vectorized ASCII mapping using NumPy
    scaled = (edges_img / 255 * (len(ASCII_CHARS) - 1)).astype(int)
    return np.array([[ASCII_CHARS[p] for p in row] for row in scaled])
    
    # return "\n".join(["".join(row) for row in ascii_img])

def contrast_ascii(img, width=400):
   
    # Adjust image size
    reshaped_img = reshape_image(img)

    # contrast
    alpha, beta = 1.5, -70 
    contrast_img = cv2.convertScaleAbs(reshaped_img, alpha=alpha, beta=beta)

    # convert to ascii
    scaled = (contrast_img / 255 * (len(ASCII_CHARS) - 1)).astype(int)
    return np.array([[ASCII_CHARS[p] for p in row] for row in scaled])
    
def ascii_to_image(ascii_rows, font_scale=2, thickness=2, font=cv2.FONT_HERSHEY_SIMPLEX):

    height_factor = 25
    width_factor = 10
    # Split the ASCII art into rows
    # ascii_rows = ascii_text.split("\n")
    
    # Set the dimensions of the output image
    height = len(ascii_rows) * height_factor  # Height based on number of rows
    width = max(len(row) for row in ascii_rows) * width_factor  # Width based on longest row

    # Create a blank white canvas to draw the ASCII characters
    img = np.zeros((height, width), dtype=np.uint8)  

    # Set text position to start drawing
    y0, dy = height_factor, height_factor  # Starting y-position and line height

    # Iterate through each row of the ASCII art
    for i, row in enumerate(ascii_rows):
        x0 = width_factor  # Starting x-position
        for j, char in enumerate(row):
            if char != ' ':
                # Draw each character at the corresponding position
                cv2.putText(img, char, (x0, y0 + i * dy), font, font_scale, (255,255,255), thickness, lineType=cv2.LINE_AA)
            x0 += width_factor  # Move the x-position for the next character
            
    return img

def convertToContrastASCII(filePath):
    img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    ascii_rows = contrast_ascii(img)
    return ascii_to_image(ascii_rows)

def convertToContrastASCIITxt(filePath):
    img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    ascii_rows = contrast_ascii(img)
    ascii_text = "\n".join(["".join(row) for row in ascii_rows])
    return ascii_text

def convertToEdgeASCII(filePath):
    img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    ascii_rows = edges_ascii(img)
    return ascii_to_image(ascii_rows)

def convertToEdgeASCIITxt(filePath):
    img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    ascii_rows = edges_ascii(img)
    ascii_text = "\n".join(["".join(row) for row in ascii_rows])
    return ascii_text


# # read in original image
# image_path = "photos/squirrel.jpg"
# img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# # convert to ascii
# ascii_rows = contrast_ascii(img)
# ascii_text = "\n".join(["".join(row) for row in ascii_rows])

# # Save ascii text to a text file
# ascii_output_path = "output/ascii_output.txt"
# with open(ascii_output_path, "w") as file:
#     file.write(ascii_text)
# print("ascii text saved to output/ascii_output.txt")

# #convert ascii text to image
# ascii_img = ascii_to_image(ascii_rows)

# # Save the image as a JPEG
# image_output_path = "output/ascii_image.jpg"  
# cv2.imwrite(image_output_path, ascii_img)

# print("ascii image saved to output/ascii_image.txt")
