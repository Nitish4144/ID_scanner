import os
import cv2
import numpy as np

# Folder containing renamed images
INPUT_FOLDER = "photos"

# Folder to save ArUco markers
OUTPUT_FOLDER = "aruco_markers"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Select ArUco dictionary
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Marker size in pixels
MARKER_SIZE = 500

for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):

        # Use filename (without extension) as person ID
        person_id = os.path.splitext(filename)[0]

        try:
            marker_id = int(person_id) % 250  # Dictionary supports IDs 0-249
        except ValueError:
            print(f"Skipping {filename}: filename is not numeric")
            continue

        # Generate marker
        marker = np.zeros((MARKER_SIZE, MARKER_SIZE), dtype=np.uint8)
        cv2.aruco.generateImageMarker(
            aruco_dict,
            marker_id,
            MARKER_SIZE,
            marker,
            1
        )

        output_path = os.path.join(
            OUTPUT_FOLDER,
            f"{person_id}_aruco.png"
        )

        cv2.imwrite(output_path, marker)

        print(f"Created marker for {person_id} -> ID {marker_id}")

print("Done!")
