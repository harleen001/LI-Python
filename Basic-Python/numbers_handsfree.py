import cv2
import mediapipe as mp
import time

def count_fingers(lst):
    cnt = 0
    # Threshold to detect finger positions
    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2
    # Count raised fingers
    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
        cnt += 1  # Index finger
    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        cnt += 1  # Middle finger
    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        cnt += 1  # Ring finger
    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        cnt += 1  # Pinky finger
    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
        cnt += 1  # Thumb (using x-axis)
    return cnt

# Function to map finger counts to numbers (0-9)
def gesture_to_number(total_count):
    gestures = {
        0: "0",  # Closed fist (no fingers up)
        1: "1",  # One finger up
        2: "2",  # Two fingers up
        3: "3",  # Three fingers up
        4: "4",  # Four fingers up
        5: "5",  # Five fingers up
        6: "6",  # One hand (five fingers up) + one on the other hand (1 finger up)
        7: "7",  # One hand (five fingers up) + two on the other hand (2 fingers up)
        8: "8",  # One hand (five fingers up) + three on the other hand (3 fingers up)
        9: "9",  # One hand (five fingers up) + four on the other hand (4 fingers up)
    }
    return gestures.get(total_count, "")

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)  # Allow for up to 2 hands
drawing = mp.solutions.drawing_utils

# Start video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

output_text = ""
last_time = time.time()  # Track time for 2-second wait

while True:
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)
    res = hands.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:
        total_count = 0  # Initialize total finger count for both hands

        for hand_keyPoints in res.multi_hand_landmarks:
            cnt = count_fingers(hand_keyPoints)  # Count fingers for the current hand
            total_count += cnt  # Add to total count

            # Draw landmarks on the frame for each hand
            drawing.draw_landmarks(frm, hand_keyPoints, mp_hands.HAND_CONNECTIONS)

        # Check if a number is recognized and if 2 seconds have passed since the last recognition
        if (time.time() - last_time) > 2:
            number = gesture_to_number(total_count)
            if number:
                output_text += number  # Append recognized number
                print(f"Current Output: {output_text}")  # Print to console or display
                # Optionally, you could simulate key presses for numbers
                # pyautogui.press(number)  # Simulating typing
                last_time = time.time()  # Reset the last recognition time

    # Show the video feed
    cv2.imshow("Hand Gesture Recognition", frm)

    if cv2.waitKey(1) == 27:  # Exit on ESC key
        break

# Clean up
cv2.destroyAllWindows()
cap.release()
