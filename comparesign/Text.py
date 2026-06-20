import cv2
import numpy as np
import keras
import matplotlib.pyplot as plt

def process_image_cv2(image_path, img_size=(128, 32)):
    """
    Reads, resizes, pads, and normalizes an image using OpenCV and NumPy,
    matching the exact distortion-free logic of the training pipeline.
    """
    target_w, target_h = img_size
    
    # 1. Read image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Could not read image at {image_path}. Check the path.")
        
    h, w = img.shape
    
    # 2. Calculate scaling factor to preserve aspect ratio
    scale = min(target_w / w, target_h / h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    
    # 3. Resize image
    img_resized = cv2.resize(img, (new_w, new_h))
    
    # 4. Calculate padding
    pad_h = target_h - new_h
    pad_w = target_w - new_w
    
    top, bottom = pad_h // 2, pad_h - (pad_h // 2)
    left, right = pad_w // 2, pad_w - (pad_w // 2)
    
    # 5. Pad the image with black pixels (0)
    img_padded = cv2.copyMakeBorder(
        img_resized, top, bottom, left, right, cv2.BORDER_CONSTANT, value=0
    )
    
    # 6. Match original preprocessing: transpose (swap width and height) and flip left-right
    img_padded = img_padded.T
    img_padded = np.fliplr(img_padded)
    
    # 7. Add channel dimension and normalize to [0, 1]
    img_padded = np.expand_dims(img_padded, axis=-1)
    img_padded = img_padded.astype(np.float32) / 255.0
    
    return img_padded

def predict_custom_image(image_path):
    """
    Predicts handwriting text using NumPy and Keras backend operations.
    """
    # 1. Process the image
    img_processed = process_image_cv2(image_path)
    
    # 2. Add batch dimension -> Shape becomes (1, 128, 32, 1)
    image_batch = np.expand_dims(img_processed, axis=0)
    
    # 3. Make prediction using the Keras model
    preds = prediction_model.predict(image_batch, verbose=0)
    
    # 4. Decode the CTC predictions using Keras ops (backend agnostic)
    input_len = np.ones(preds.shape[0]) * preds.shape[1]
    results = keras.ops.nn.ctc_decode(preds, sequence_lengths=input_len)[0][0][:, :max_len]
    
    # 5. Clean up the numeric tokens and convert back to a string using pure NumPy
    res = results[0].numpy()  # Extract the single prediction array
    res = res[res != -1]      # Filter out the padding/blank tokens (-1)
    
    # Map indices back to characters using the existing num_to_char layer
    chars = num_to_char(res).numpy()
    decoded_text = "".join([c.decode("utf-8") for c in chars]).replace("[UNK]", "")
    
    # --- Display the image and the result ---
    plt.figure(figsize=(5, 2))
    # Revert the transpose and flip purely for visualization so it reads normally
    display_img = np.fliplr(img_processed[:, :, 0]).T
    
    plt.imshow(display_img, cmap="gray")
    plt.title(f"Predicted Text: {decoded_text}")
    plt.axis("off")
    plt.show()
    
    return decoded_text