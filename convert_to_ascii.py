import cv2
import numpy as np

# ASCII characters from light to dark
ASCII_CHARS = " .:-=+*%#"
SHORT_ASCII_CHARS = " #"
HEIGHT_FACTOR = 50
WIDTH_FACTOR = 20

def reshape_image(img):
    # Resize while maintaining aspect ratio
    aspect_ratio = img.shape[1] / img.shape[0]
    width = int(img.shape[1]/5)
    height = int(width / aspect_ratio * (WIDTH_FACTOR/HEIGHT_FACTOR))  # Adjust the factor based on your text editor
    return cv2.resize(img, (width, height))

def edges_ascii(img, width=400, precision=5):
   
    # Adjust image size+++
    reshaped_img = reshape_image(img)

    # edge detection
    edges_img = cv2.Canny(reshaped_img, 100, 200)
    # edges_img = cv2.Canny(reshaped_img, 50, 150)  # Lower thresholds for more edges

     # Vectorized ASCII mapping using NumPy
    
    scaled = (edges_img / 255 * (len(SHORT_ASCII_CHARS) - 1)).astype(int)
    return np.array([[SHORT_ASCII_CHARS[p] for p in row] for row in scaled])
    
    # return "\n".join(["".join(row) for row in ascii_img])

def contrast_ascii(img, width=400, precision = 5):
   
    # Adjust image size
    reshaped_img = reshape_image(img)

    # contrast
    alpha, beta = 1.5, -70 
    contrast_img = cv2.convertScaleAbs(reshaped_img, alpha=alpha, beta=beta)

    # convert to ascii
    scaled = (contrast_img / 255 * (len(ASCII_CHARS) - 1)).astype(int)
    # scaled = ((contrast_img - contrast_img.min()) / (contrast_img.max() - contrast_img.min()) * (len(ASCII_CHARS) - 1)).astype(int)

    return np.array([[ASCII_CHARS[p] for p in row] for row in scaled])
    
def ascii_to_image(ascii_rows, font_scale=1., thickness=3, font=cv2.FONT_HERSHEY_SIMPLEX):

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
            
    # Compress the image using JPEG format with specified quality
    # The quality value is between 0 and 100, where 100 is the highest quality (least compression)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 10]
    _, compressed_img = cv2.imencode('.jpg', img, encode_param)

    # Decode the compressed image back to a NumPy array
    compressed_img = cv2.imdecode(compressed_img, 1)

    return compressed_img

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

def process_video(input_video_path, output_video_path, ascii_type, precision = 10):
    """Process the video and create an ASCII video."""
    # Open the input video file
    video_capture = cv2.VideoCapture(input_video_path)
    
    # Get the video properties (frame count, width, height, fps)
    fps = 30
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object to save the output video as MP4
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Use "mp4v" codec for output MP4 video
    out_video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        
        # Convert the frame to grayscale
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # frame_gray = cv2.convertScaleAbs(frame_gray, alpha=1.5, beta=50) # Make video's brighter and add more contrast to get better output
        # frame_gray = cv2.rotate(frame_gray, cv2.ROTATE_90_CLOCKWISE)  # Rotate 90 degrees clockwise

        # Works for normal videos, but stretches vertical phone vids

        # Convert the grayscale frame to ASCII
        ascii_rows =""
        if ascii_type == "edges":
            ascii_rows = edges_ascii(frame_gray, precision)
        else:
            ascii_rows = contrast_ascii(frame_gray, precision)
        ascii_img = ascii_to_image(ascii_rows)

        # Resize the ASCII image to match the video dimensions
        ascii_img_resized = cv2.resize(ascii_img, (width, height))

        # Convert the resized ASCII image back to BGR to write into video
        # ascii_bgr = cv2.cvtColor(ascii_img_resized, cv2.COLOR_GRAY2BGR)
        if len(ascii_img_resized.shape) == 2:  # Ensure it's grayscale
            ascii_bgr = cv2.cvtColor(ascii_img_resized, cv2.COLOR_GRAY2BGR)
        else:
            ascii_bgr = ascii_img_resized  # If already 3-channel, no conversion needed

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
