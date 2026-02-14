import cv2
import mediapipe as mp
import time

def count_fingers(lst):
    cnt = 0
    # Count fingers on one hand based on their positions
    if lst.landmark[5].y < lst.landmark[8].y:  # Thumb
        cnt += 1
    if lst.landmark[9].y < lst.landmark[12].y:  # Index
        cnt += 1
    if lst.landmark[13].y < lst.landmark[16].y:  # Middle
        cnt += 1
    if lst.landmark[17].y < lst.landmark[20].y:  # Ring
        cnt += 1
    if lst.landmark[5].x < lst.landmark[4].x:  # Pinky
        cnt += 1

    return cnt

# Function to map finger counts to letters (A-Z)
def gesture_to_letter(cnt):
    gestures = {
        1: "A",  # Index finger
        2: "B",  # Index + Middle
        3: "C",  # Index + Middle + Ring
        4: "D",  # Index + Middle + Ring + Pinky
        5: "E",  # All fingers up
        6: "F",  # Thumb
        7: "G",  # Thumb + Index
        8: "H",  # Thumb + Index + Middle
        9: "I",  # Thumb + Index + Middle + Ring
        10: "J", # Thumb + Index + Middle + Ring + Pinky
        11: "K", # Index + Ring
        12: "L", # Index + Pinky
        13: "M", # Index + Middle + Pinky
        14: "N", # Index + Middle + Ring + Pinky
        15: "O", # All fingers curled
        16: "P", # Middle
        17: "Q", # Middle + Ring
        18: "R", # Middle + Ring + Pinky
        19: "S", # Middle + Ring + Pinky + Index
        20: "T", # All fingers straight
        21: "U", # Index + Thumb
        22: "V", # Index + Thumb in a V shape
        23: "W", # Index + Middle + Thumb
        24: "X", # Index + Middle + Ring + Thumb
        25: "Y", # Index + Middle + Ring + Pinky + Thumb
        26: "Z", # All fingers closed, thumb up
    }
    return gestures.get(cnt, "")

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)  # Allow for up to 2 hands
drawing = mp.solutions.drawing_utils

# Start video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

output_text = ""
last_recognition_time = time.time()  # Time of the last letter recognized
recognition_delay = 2  # Delay in seconds before recognizing the next letter

while True:
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)  # Flip the frame horizontally
    res = hands.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:
        for hand_keyPoints in res.multi_hand_landmarks:
            cnt = count_fingers(hand_keyPoints)
            letter = gesture_to_letter(cnt)

            # Check if a letter is recognized and if the delay time has passed
            if letter and (time.time() - last_recognition_time) > recognition_delay:
                output_text += letter  # Append recognized letter
                print(f"Current Output: {output_text}")  # Print to console or display
                last_recognition_time = time.time()  # Reset the last recognition time
            
            # Draw landmarks on the frame for each hand
            drawing.draw_landmarks(frm, hand_keyPoints, mp_hands.HAND_CONNECTIONS)

    # Show the video feed
    cv2.imshow("Hand Gesture Recognition", frm)

    if cv2.waitKey(1) == 27:  # Exit on ESC key
        break

# Clean up
cv2.destroyAllWindows()
cap.release()
