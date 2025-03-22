
# Hackathon 2025 Camera portion
# program to capture single image from webcam in python 
# 
# Initial code by Ryan Wong
# edits by Emma Wang
# 3.21.2025

import cv2
import os
from datetime import datetime

def webcamShot():
    image_dir = 'images'
    os.makedirs(image_dir, exist_ok=True)  # create folder if it doesn't exist

    # Initialize the camera
    # If you have multiple cameras connected with current device, assign a value in cam_port variable according to that 
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)

    # Set width and height (optional)
    cam.set(3, 1500)  # Width
    cam.set(4, 1500)  # Height

    solidCHEESE_open = False # track if solidCHEESE has been opened

    while True:
        ret, frame = cam.read()  # capture new frame in each loop iteration

        if not ret:  # check if the frame was successfully captured
            print("Failed to capture image")
            break

        cv2.imshow('CHEESE', frame)  # display the live frame

        key = cv2.waitKey(1)  # capture key press

        # Check if the "X" button is clicked or ESC (27) is pressed
        if cv2.getWindowProperty('CHEESE', cv2.WND_PROP_VISIBLE) < 1 or key == 27:
            print("Window closed by user.")
            break  # Exit the loop and end the program

        if key == ord(' '):  # Save image on pressing space
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            img = timestamp + '.png'
            img_path = os.path.join(image_dir, img) # correct file path
            cv2.imwrite(img_path, frame) # save
            print(f"Image saved as '{img_path}!'")

            # Display the saved image
            saved_image = cv2.imread(img_path)
            if saved_image is not None:
                cv2.imshow('solidCHEESE', saved_image)
            else:
                print("Error: Could not load saved image.")

            # Close camera window
            cv2.destroyWindow("CHEESE")
            print('CHEESE destroyed (?)')

            # Wait for space key again before resuming live video
            while solidCHEESE_open:
                key = cv2.waitKey(1)
                if key == ord(' '):  # Press space again to resume
                    cv2.destroyWindow("solidCHEESE")  # Close saved image window
                    solidCHEESE_open = False
                    print("solidCHEESE closed. Resuming video feed.")
                    break  # Exit inner loop, resume live video
                elif key == 27:
                    print("Program exited by user.")
                    cam.release()
                    cv2.destroyAllWindows()
                    return img_path
                
def webcamVideo():
    video_dir = 'videos'
    os.makedirs(video_dir, exist_ok=True)  # Ensure video directory exists

    cam = cv2.VideoCapture(0)
    cam.set(3, 1500)  # Width
    cam.set(4, 1500)  # Height

    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Define video codec
    out = None  # Initialize video writer
    recording = False  # Track recording state

    print("Press 'R' to start recording\nPress 'S' to stop recording\nPress 'Esc' to exit")

    while cam.isOpened():
        ret, frame = cam.read()
        if not ret:
            print("Failed to capture video")
            break

        cv2.imshow('RECORDING', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('r') and not recording:
            # Start recording
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            video_path = os.path.join(video_dir, f"{timestamp}.avi")
            out = cv2.VideoWriter(video_path, fourcc, 20.0, (int(cam.get(3)), int(cam.get(4))))
            recording = True
            print(f"Recording started... Press 'S' to stop. Saving to {video_path}")

        if key == ord('s') and recording:
            # Stop recording
            recording = False
            out.release()
            print(f"Recording stopped. Video saved at: {video_path}")

        if recording and out is not None:
            out.write(frame)

        if key == 27:  # Escape key to exit
            break

    cam.release()
    if out is not None:
        out.release()
    cv2.destroyAllWindows()

#    return video_path