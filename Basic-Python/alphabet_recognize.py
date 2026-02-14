import cv2
import mediapipe as mp
import pytesseract
import numpy as np
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)  # Allow for up to 1 hand
drawing = mp.solutions.drawing_utils

# Function to recognize text from an image
def recognize_text_from_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply thresholding to get a binary image
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(binary_image, config='--psm 8')
    return text.strip()

# Start video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

output_text = ""
last_time = time.time()  # Track time for 2-second wait

while True:
    ret, frm = cap.read()
    frm = cv2.flip(frm, 1)
    res = hands.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:
        hand_keypoints = res.multi_hand_landmarks[0]
        drawing.draw_landmarks(frm, hand_keypoints, mp_hands.HAND_CONNECTIONS)

        # Draw a bounding box around the area of interest (where you will write)
        height, width, _ = frm.shape
        roi = frm[int(height/2):height, 0:int(width/2)]  # Lower half of the frame

        # Show the ROI for the user to write letters
        cv2.rectangle(frm, (0, int(height/2)), (int(width/2), height), (0, 255, 0), 2)

        # Check if 2 seconds have passed since the last recognition
        if (time.time() - last_time) > 2:
            recognized_text = recognize_text_from_image(roi)
            if recognized_text:
                output_text += recognized_text  # Append recognized text
                print(f"Current Output: {output_text}")  # Print to console or display

                last_time = time.time()  # Reset the last recognition time

    # Show the video feed
    cv2.imshow("Hand Writing Recognition", frm)

    if cv2.waitKey(1) == 27:  # Exit on ESC key
        break

# Clean up
cv2.destroyAllWindows()
cap.release()
