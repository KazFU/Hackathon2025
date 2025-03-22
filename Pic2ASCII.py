from PIL import Image

# Define ASCII characters from lightest to darkest
ASCII_CHARS = [chr(i) for i in range(32, 127)]

# Function to resize image
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Function to convert image to grayscale
def grayscale_image(image):
    return image.convert("L")  # Convert to grayscale

# Function to convert each pixel to an ASCII character
def pixel_to_ascii(pixel_value):
    return ASCII_CHARS[(pixel_value * len(ASCII_CHARS)) // 256]  # Map pixel to one of the 10 characters

# Function to convert image to ASCII art
def image_to_ascii(image_path, new_width=100):
    try:
        # Open the image
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}: {e}")
        return
    
    # Resize and convert to grayscale
    image = resize_image(image, new_width)
    grayscale_conversion = grayscale_image(image)

    # Create ASCII art
    ascii_art = ""
    for y in range(grayscale_conversion.height):
        for x in range(grayscale_conversion.width):
            pixel_value = grayscale_conversion.getpixel((x, y))  # Get pixel value (brightness)
            ascii_char = pixel_to_ascii(pixel_value)
            ascii_art += ascii_char
        ascii_art += "\n"  # Newline at the end of each row

    return ascii_art

# Function to save ASCII art to a file
def save_ascii_art(ascii_art, filename="ascii_art.txt"):
    with open(filename, "w") as f:
        f.write(ascii_art)