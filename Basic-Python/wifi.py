import cv2
import speedtest
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def get_wifi_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1000000  # convert to Mbps
    upload_speed = st.upload() / 1000000  # convert to Mbps
    return download_speed, upload_speed

def add_text_to_frame(frame, text):
    font = ImageFont.truetype("arial.ttf", 20)
    img_pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(img_pil)
    draw.text((10, 10), text, font=font, fill=(255, 255, 255))
    frame = np.array(img_pil)
    return frame

# Open USB camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Get WiFi speed
    download_speed, upload_speed = get_wifi_speed()
    wifi_speed_text = f"WiFi Speed: Download: {download_speed:.2f} Mbps, Upload: {upload_speed:.2f} Mbps"

    # Add WiFi speed text to frame
    frame = add_text_to_frame(frame, wifi_speed_text)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
