# Peter Dorsaneo 
# Zen - Social Robotics - Robotics Club @ UCF
# 
# Webcam class for initializing and detecting images in the user webcam.
import cv2 
import sys
import os
import constants

class Webcam():
    # Initializes the webcam with indicated name as parameter.
    def __init__(self, name=""):
        self.name = name
        # Initializes the users webcam
        self.video_capture = cv2.VideoCapture(0)

    # Cascade detection and image outlining from webcam.
    # Function is used for detecting face and eye images in the webcam.
    def detect(self, cascPathFace, cascPathEye):

        # Create cascade classifiers
        cascFace = cv2.CascadeClassifier(cascPathFace)
        cascEye = cv2.CascadeClassifier(cascPathEye)

        # Initiate loop to capture each image from the webcam
        while (True):
            # Read the image
            ret, frame = self.video_capture.read()

            # Set the color space
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detected images in multi scale
            detectedFace = self.det_multi_scale(cascFace, gray)
            detectedEye = self.det_multi_scale(cascEye, gray) 

            self.label_detected_image(detectedFace, frame, self.name)
            self.label_detected_image(detectedEye, frame, "Eye")

            # Display the resulting frame
            cv2.imshow('Video', frame)

            # User presses 'q' key in order to quit webcam recording
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Destroy the webcam image processing once user (q)uits
        self.destroy_webcam()

    # Method for labeling the detected image.
    def label_detected_image(self, detectedImage, frame, text):
        font                   = constants.FONT
        fontScale              = 1
        fontColor              = (0,0,0)
        lineType               = 2

        for (x, y, w, h) in detectedImage:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(
                frame, 
                text, 
                (x, y-constants.ADJUST_TEXT_PUT), 
                font, 
                fontScale, 
                fontColor, 
                lineType
                )

    # Create a file path for holding the users facial images.
    def create_image_path(self):
        filePath = str(self.name)

        if not os.path.exists(filePath):
            os.makedirs(filePath)

    # Method for multi use of cascade classifiers. 
    # Function detects multiple scaled images for specified classifier. 
    # Classifier being the image(s) to detect.
    def det_multi_scale(self, casc_classifier, colorSpace):
        casc = casc_classifier.detectMultiScale(
            colorSpace,
            scaleFactor=constants.SCALE_FACTOR, # Change the scaleFactor as needed. Ideally between 1.1 and 1.2
            minNeighbors=constants.MIN_NEIGHBORS,
            minSize=(constants.MIN_SIZE, constants.MIN_SIZE),
            flags=constants.FLAGS
        )

        return casc

    # Method to save detected images.
    # To be utilized later...
    def save_detected_images(self, frame, filePath, k, x, y, w, h):
        crop = frame[y:y+h, x:x+w]
        cv2.imwrite(filePath + "/" + self.name + str(k) + ".png", crop)

    # Method to destroy webcam image capturing.
    def destroy_webcam(self):
        self.video_capture.release()
        cv2.destroyAllWindows()






