import cv2
import dlib
import numpy as np

# Initialize dlib's face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def get_gaze_ratio(eye_points, facial_landmarks, frame, gray):
    # Get the region of the eye
    eye_region = np.array([(facial_landmarks.part(point).x, facial_landmarks.part(point).y) for point in eye_points], np.int32)
    
    # Create a mask for the eye
    height, width, _ = frame.shape
    mask = np.zeros((height, width), np.uint8)
    cv2.polylines(mask, [eye_region], True, 255, 2)
    cv2.fillPoly(mask, [eye_region], 255)
    eye = cv2.bitwise_and(gray, gray, mask=mask)

    # Thresholding to isolate the iris (dark part)
    min_x = np.min(eye_region[:, 0])
    max_x = np.max(eye_region[:, 0])
    min_y = np.min(eye_region[:, 1])
    max_y = np.max(eye_region[:, 1])
    
    gray_eye = eye[min_y: max_y, min_x: max_x]
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY_INV)
    
    # Split threshold eye into left and right half to compare density
    h, w = threshold_eye.shape
    left_side_threshold = threshold_eye[0: h, 0: int(w / 2)]
    right_side_threshold = threshold_eye[0: h, int(w / 2): w]
    
    left_side_white = cv2.countNonZero(left_side_threshold)
    right_side_white = cv2.countNonZero(right_side_threshold)
    
    if left_side_white == 0: return 1
    elif right_side_white == 0: return 5
    return left_side_white / right_side_white

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        landmarks = predictor(gray, face)
        
        # Gaze detection (Landmarks 36-41 are left eye, 42-47 are right eye)
        gaze_ratio_left = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks, frame, gray)
        gaze_ratio_right = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks, frame, gray)
        gaze_ratio = (gaze_ratio_right + gaze_ratio_left) / 2

        # Display Logic based on Gaze Ratio
        if gaze_ratio <= 1:
            cv2.putText(frame, "LOOKING RIGHT", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        elif 1 < gaze_ratio < 1.7:
            cv2.putText(frame, "CENTER", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        else:
            cv2.putText(frame, "LOOKING LEFT", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cv2.imshow("Gaze Detector for Coding", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()