import cv2
import csv

mapping = {}

with open(
    "marker_mapping.csv",
    "r"
) as f:

    reader = csv.DictReader(f)

    for row in reader:
        mapping[
            int(row["marker_id"])
        ] = row["person_id"]

aruco_dict = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_7X7_1000
)

params = cv2.aruco.DetectorParameters()

detector = cv2.aruco.ArucoDetector(
    aruco_dict,
    params
)

cap = cv2.VideoCapture(0)

print("Press ESC to exit")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    corners, ids, _ = detector.detectMarkers(
        frame
    )

    if ids is not None:

        cv2.aruco.drawDetectedMarkers(
            frame,
            corners,
            ids
        )

        for marker_id, corner in zip(
            ids.flatten(),
            corners
        ):

            person_id = mapping.get(
                int(marker_id),
                "UNKNOWN"
            )

            x = int(corner[0][0][0])
            y = int(corner[0][0][1])

            cv2.putText(
                frame,
                f"ID: {person_id}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 0),
                2
            )

            print(
                f"Detected Person ID: "
                f"{person_id}"
            )

    cv2.imshow(
        "ArUco Attendance Scanner",
        frame
    )

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
