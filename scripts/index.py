import os
import re
import cv2
import pytesseract

# Path containing images
IMAGE_FOLDER = r"photos"

# Tesseract path (Windows only)
# Uncomment and modify if needed:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

for filename in os.listdir(IMAGE_FOLDER):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):

        image_path = os.path.join(IMAGE_FOLDER, filename)

        # Read image
        img = cv2.imread(image_path)

        if img is None:
            continue

        h, w = img.shape[:2]

        # Crop bottom 25% of image
        bottom_part = img[int(h * 0.75):h, :]

        # Convert to grayscale
        gray = cv2.cvtColor(bottom_part, cv2.COLOR_BGR2GRAY)

        # Threshold for better OCR
        gray = cv2.threshold(
            gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        # OCR
        text = pytesseract.image_to_string(gray)

        print(f"{filename} -> OCR: {text}")

        # Extract ID (adjust regex to your format)
        match = re.search(r'\b\d{4,}\b', text)

        if match:
            person_id = match.group()

            ext = os.path.splitext(filename)[1]
            new_name = f"{person_id}{ext}"
            new_path = os.path.join(IMAGE_FOLDER, new_name)

            # Avoid overwriting existing files
            counter = 1
            while os.path.exists(new_path):
                new_name = f"{person_id}_{counter}{ext}"
                new_path = os.path.join(IMAGE_FOLDER, new_name)
                counter += 1

            os.rename(image_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
        else:
            print(f"No ID found in {filename}")
