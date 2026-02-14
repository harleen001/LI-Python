import cv2
import pytesseract
import numpy as np

# Configure the path for Tesseract executable if it's not in your PATH
# Uncomment and set the path if required
# pytesseract.pytesseract.tesseract_cmd = r'C:\Path\To\tesseract.exe'

# Start video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Set a blank output text variable
output_text = ""

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Pre-process the image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)  # Thresholding

    # Use Tesseract to do OCR on the processed frame
    recognized_text = pytesseract.image_to_string(thresh, config='--psm 6')

    # Clean and store the recognized text
    if recognized_text.strip():  # Check if there is any recognized text
        output_text += recognized_text.strip()  # Append recognized text
        print(f"Recognized Text: {recognized_text.strip()}")  # Print to console

    # Draw the recognized text on the frame
    cv2.putText(frame, output_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow('Writing Recognition', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Exit on ESC key
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
