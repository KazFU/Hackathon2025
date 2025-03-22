#Ryan Wong
import cv2
import os

# Ensure the 'images' directory exists
image_folder = 'images'
os.makedirs(image_folder, exist_ok=True)  # Create folder if it doesn't exist

# Open webcam
cap = cv2.VideoCapture(0)  # 0 for default webcam

# Set width and height (optional)
cap.set(3, 1500)  # Width
cap.set(4, 1500)  # Height

while True:
    ret, frame = cap.read()  # Capture new frame in each loop iteration

    if not ret:  # Check if the frame was successfully captured
        print("Failed to capture image")
        break

    cv2.imshow('Live Camera', frame)  # Display the live frame

    key = cv2.waitKey(1)  # Capture key press

    if key == ord('y'):  # Save image on pressing 'y'
        image_path = os.path.join(image_folder, 'c1.png')  # Correct file path
        cv2.imwrite(image_path, frame)
        print(f"Image saved as '{image_path}'")

        # Display the saved image
        saved_image = cv2.imread(image_path)
        if saved_image is not None:
            cv2.imshow('Saved Image', saved_image)
        else:
            print("Error: Could not load saved image.")

    # Close the window if the user clicks the "X" button
    if cv2.getWindowProperty('Live Camera', cv2.WND_PROP_VISIBLE) < 1:
        print("Window closed by user.")
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()