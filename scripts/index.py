import os
import re
import cv2
import pytesseract
import shutil

INPUT_FOLDER = "photos"
OUTPUT_FOLDER = "renamed_photos"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

pytesseract.pytesseract.tesseract_cmd = \
r"C:\Program Files\Tesseract-OCR\tesseract.exe"

for filename in os.listdir(INPUT_FOLDER):

    if not filename.lower().endswith(
        (".jpg", ".jpeg", ".png")
    ):
        continue

    path = os.path.join(INPUT_FOLDER, filename)

    img = cv2.imread(path)

    if img is None:
        continue

    h, w = img.shape[:2]

    # Bottom 25%
    crop = img[int(h * 0.75):h, :]

    gray = cv2.cvtColor(
        crop,
        cv2.COLOR_BGR2GRAY
    )

    gray = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    text = pytesseract.image_to_string(gray)

    # Extract long numeric ID
    match = re.search(r"\d{4,}", text)

    if not match:
        print(f"ID not found: {filename}")
        continue

    person_id = match.group()

    ext = os.path.splitext(filename)[1]

    new_name = f"{person_id}{ext}"

    dst = os.path.join(
        OUTPUT_FOLDER,
        new_name
    )

    counter = 1

    while os.path.exists(dst):
        dst = os.path.join(
            OUTPUT_FOLDER,
            f"{person_id}_{counter}{ext}"
        )
        counter += 1

    shutil.copy2(path, dst)

    print(
        f"{filename} -> {os.path.basename(dst)}"
    )

print("\nRenaming completed.")
