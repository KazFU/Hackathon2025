import cv2
import numpy as np

# ASCII characters from light to dark
ASCII_CHARS = " .:-=+*%#"
HEIGHT_FACTOR = 25
WIDTH_FACTOR = 10

def reshape_image(img):
    # Resize while maintaining aspect ratio
    aspect_ratio = img.shape[1] / img.shape[0]
    width = int(img.shape[1]/3)
    height = int(width / aspect_ratio * (WIDTH_FACTOR/HEIGHT_FACTOR))  # Adjust the factor based on your text editor
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

    HEIGHT_FACTOR = 25
    WIDTH_FACTOR = 10
    # Split the ASCII art into rows
    # ascii_rows = ascii_text.split("\n")
    
    # Set the dimensions of the output image
    height = len(ascii_rows) * HEIGHT_FACTOR  # Height based on number of rows
    width = max(len(row) for row in ascii_rows) * WIDTH_FACTOR  # Width based on longest row

    # Create a blank white canvas to draw the ASCII characters
    img = np.zeros((height, width), dtype=np.uint8)  

    # Set text position to start drawing
    y0, dy = HEIGHT_FACTOR, HEIGHT_FACTOR  # Starting y-position and line height

    # Iterate through each row of the ASCII art
    for i, row in enumerate(ascii_rows):
        x0 = WIDTH_FACTOR  # Starting x-position
        for j, char in enumerate(row):
            if char != ' ':
                # Draw each character at the corresponding position
                cv2.putText(img, char, (x0, y0 + i * dy), font, font_scale, (255,255,255), thickness, lineType=cv2.LINE_AA)
            x0 += WIDTH_FACTOR  # Move the x-position for the next character
            
    return img

def convertToContrastASCIIJpg(filePath):
    img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    ascii_rows = contrast_ascii(img)
    return ascii_to_image(ascii_rows)

def convertToContrastASCIITxt(filePath):
    img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    ascii_rows = contrast_ascii(img)
    ascii_text = "\n".join(["".join(row) for row in ascii_rows])
    return ascii_text

def convertToEdgeASCIIJpg(filePath):
    img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    ascii_rows = edges_ascii(img)
    return ascii_to_image(ascii_rows)

def convertToEdgeASCIITxt(filePath):
    img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
    ascii_rows = edges_ascii(img)
    ascii_text = "\n".join(["".join(row) for row in ascii_rows])
    return ascii_text


def process_video(input_video_path, output_video_path, ascii_type):
    """Process the video and create an ASCII video."""
    # Open the input video file
    video_capture = cv2.VideoCapture(input_video_path)
    
    # Get the video properties (frame count, width, height, fps)
        # Get the video properties (frame count, width, height, fps)
    fps = 30
    width = 270
    height = 480

    # Define the codec and create VideoWriter object to save the output video as MP4
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Use "mp4v" codec for output MP4 video
    out_video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        
        # Convert the frame to grayscale
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.rotate(frame_gray, cv2.ROTATE_90_CLOCKWISE)  # Rotate 90 degrees clockwise

        # Convert the grayscale frame to ASCII
        if ascii_type == "edges":
            ascii_rows = edges_ascii(frame_gray)
        elif ascii_type == "contrast":
            ascii_rows = contrast_ascii(frame_gray)
        ascii_img = ascii_to_image(ascii_rows)

        # Resize the ASCII image to match the video dimensions
        ascii_img_resized = cv2.resize(ascii_img, (270, 480))

        # Convert the resized ASCII image back to BGR to write into video
        ascii_bgr = cv2.cvtColor(ascii_img_resized, cv2.COLOR_GRAY2BGR)
        out_video.write(ascii_bgr)


    video_capture.release()
    out_video.release()
    print(f"ASCII video created at {output_video_path}")


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
