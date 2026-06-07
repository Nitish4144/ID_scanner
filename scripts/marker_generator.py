import os
import cv2
import csv
import numpy as np

INPUT_FOLDER = "renamed_photos"
OUTPUT_FOLDER = "aruco_markers"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

aruco_dict = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_7X7_1000
)

MARKER_SIZE = 600

mapping_file = "marker_mapping.csv"

with open(
    mapping_file,
    "w",
    newline=""
) as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "marker_id",
        "person_id"
    ])

    marker_id = 0

    for filename in sorted(
        os.listdir(INPUT_FOLDER)
    ):

        if not filename.lower().endswith(
            (".jpg", ".jpeg", ".png")
        ):
            continue

        person_id = os.path.splitext(
            filename
        )[0]

        marker = np.zeros(
            (MARKER_SIZE, MARKER_SIZE),
            dtype=np.uint8
        )

        cv2.aruco.generateImageMarker(
            aruco_dict,
            marker_id,
            MARKER_SIZE,
            marker,
            1
        )

        marker_path = os.path.join(
            OUTPUT_FOLDER,
            f"{person_id}_aruco.png"
        )

        cv2.imwrite(
            marker_path,
            marker
        )

        writer.writerow([
            marker_id,
            person_id
        ])

        print(
            f"Marker {marker_id} -> {person_id}"
        )

        marker_id += 1

print("\nMarker generation completed.")
