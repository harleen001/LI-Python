import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='google.protobuf')

import cv2
import numpy as np
import HandTracking_GestureRecognition_Module as hgm

def draw_on_feed(frame, canvas):
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
    # Combine the canvas with the frame
    combined = cv2.bitwise_and(frame, img_inv)  # Keep frame visible where canvas is not
    combined = cv2.bitwise_or(combined, canvas)  # Overlay the canvas
    return combined

def draw_rectangle(canvas, start_point, end_point, color=(255, 0, 0), thickness=2):
    cv2.rectangle(canvas, start_point, end_point, color, thickness)

def draw_arrow(canvas, start_point, end_point, color=(0, 255, 0), thickness=2):
    cv2.arrowedLine(canvas, start_point, end_point, color, thickness, tipLength=0.05)

def draw_circle(canvas, center_point, radius, color=(0, 0, 255), thickness=2):
    cv2.circle(canvas, center_point, radius, color, thickness)

def show_face_on_canvas(frame, canvas, face_width=200, face_height=150):
    # Resize the frame to fit into a small rectangle on the side
    resized_face = cv2.resize(frame, (face_width, face_height))
    # Place the resized face onto the canvas at the top-right corner
    canvas[10:10 + face_height, canvas.shape[1] - face_width - 10:canvas.shape[1] - 10] = resized_face

def main():
    width, height = 1280, 720
    canvas = np.ones((height, width, 3), dtype='uint8') * 255  # White background canvas

    # Initialize video capture
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    detector = hgm.HandDetector()

    drawing_mode = 'rectangle'  # Default mode
    start_point = None
    end_point = None
    drawing = False  # To track if we're in the middle of drawing

    while True:
        success, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame = detector.FindHands(frame, True)
        lm_list = detector.FindPositions(frame, 0)

        if len(lm_list):
            fingers = detector.FindGesture()  # Hand gesture detection
            xi, yi = lm_list[8][1:]  # Index finger tip coordinates

            # Gesture: 10 fingers up (both hands) to clear the canvas
            if all(f == 1 for f in fingers) and len(lm_list) >= 21:  # Ensure it's both hands
                canvas = np.ones((height, width, 3), dtype='uint8') * 255  # Reset canvas to white
                drawing = False
                start_point = None
                end_point = None

            # Gesture: Index finger up - start or update shape
            elif fingers[0] == 1 and all(f == 0 for f in fingers[1:]):
                if not drawing:  # Start drawing only if not already drawing
                    start_point = (xi, yi)
                    drawing = True
                else:  # Update the shape dimensions while drawing
                    end_point = (xi, yi)

            # Gesture: Index + Middle fingers up - finish drawing
            elif fingers[0] == 1 and fingers[1] == 1 and all(f == 0 for f in fingers[2:]):
                if drawing and start_point:  # Only finalize if we have a valid start point
                    if end_point is not None:  # Only finalize if we have a valid end point
                        if drawing_mode == 'rectangle':
                            draw_rectangle(canvas, start_point, end_point)
                        elif drawing_mode == 'arrow':
                            draw_arrow(canvas, start_point, end_point)
                        elif drawing_mode == 'circle':
                            radius = int(np.hypot(end_point[0] - start_point[0], end_point[1] - start_point[1]))
                            draw_circle(canvas, start_point, radius)

                    # Reset drawing state
                    start_point = None
                    end_point = None
                    drawing = False  # Stop drawing after one shape is done

                    # Switch between shapes: rectangle -> arrow -> circle
                    if drawing_mode == 'rectangle':
                        drawing_mode = 'arrow'
                    elif drawing_mode == 'arrow':
                        drawing_mode = 'circle'
                    else:
                        drawing_mode = 'rectangle'

        # Draw the current shape in real-time before finalizing
        if drawing and start_point:
            temp_canvas = canvas.copy()  # Use a temporary canvas to visualize the current shape
            if end_point is not None:  # Only draw if we have an end point
                if drawing_mode == 'rectangle':
                    draw_rectangle(temp_canvas, start_point, end_point)
                elif drawing_mode == 'arrow':
                    draw_arrow(temp_canvas, start_point, end_point)
                elif drawing_mode == 'circle':
                    radius = int(np.hypot(end_point[0] - start_point[0], end_point[1] - start_point[1]))
                    draw_circle(temp_canvas, start_point, radius)

            # Instead of modifying the frame, just overlay the canvas to the original frame
            combined_frame = draw_on_feed(frame, temp_canvas)
            cv2.imshow('Flowchart Drawing', combined_frame)

        # Show the small rectangle with the face on the side
        show_face_on_canvas(frame, canvas)

        if cv2.waitKey(20) & 0xFF == ord('x'):
            break

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()
