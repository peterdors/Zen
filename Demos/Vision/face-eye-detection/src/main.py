# Peter Dorsaneo 
# Zen - Social Robotics - Robotics Club @ UCF
# 
# Main file for implementing demo of the Webcam class.
import cv2 
import sys
import os
import constants
from webcam import Webcam

# Our paths to the cascade and Webcam is implemented under the main function.
# Function returns 0 for no error, and returns 1 for indicating error. 
def main():
    # Get absolute file paths.
    cascPathFace = os.path.abspath(
        "../haarcascades/haarcascade_frontalface_default.xml"
        )
    cascPathEye = os.path.abspath(
        "../haarcascades/haarcascade_eye.xml"
        )

    # Check for correct number of command line arguments
    if (len(sys.argv) < 2):
        print("Correct terminal command: python webcam.py <first_name>")
        return 1

    # Call the Webcam class with a single parameter for the users name. 
    # This only initializes the users webcam, it does not initialize 
    # the image recognition/detection.
    cam = Webcam(sys.argv[1])
    # Call the detect() function implemented in the Webcam class.
    cam.detect(cascPathFace, cascPathEye)

    return 0

# Get things going.
if __name__ == "__main__":
	main()
