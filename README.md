# ArUco-Based Person Identification System

This project automatically:

1. Reads person IDs from the bottom of photos using OCR.
2. Renames images using the detected ID.
3. Generates unique ArUco markers for each person.
4. Creates a mapping between ArUco IDs and Person IDs.
5. Scans ArUco markers using a webcam and identifies the corresponding person.

---

# Prerequisites

## Python

Python 3.9+ is recommended.

Verify installation:

```bash
python --version
```

---

# Install Dependencies

## 1. Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 2. Install Python Packages

```bash
pip install opencv-contrib-python
pip install pytesseract
pip install numpy
pip install pandas
```

Or install everything at once:

```bash
pip install opencv-contrib-python pytesseract numpy pandas
```

---

# Install Tesseract OCR

This project uses Tesseract OCR to read IDs from images.

## Windows

Download and install:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update the path inside:

```python
pytesseract.pytesseract.tesseract_cmd = \
r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

# Workflow

---

## Step 1: Add Photos

Place all photos inside:

```text
photos/
```

Example:

```text
photos/
├── img1.jpg
├── img2.jpg
├── img3.jpg
```

The person's ID should be visible near the bottom of each image.

---

## Step 2: Rename Photos Using OCR

Run:

```bash
python 01_rename_from_photo.py
```

The script:

- Reads the bottom section of each image
- Extracts the ID using OCR
- Renames the image using the detected ID
- Stores the result in:

```text
renamed_photos/
```

Example:

Before:

```text
img1.jpg
img2.jpg
```

After:

```text
22011001.jpg
22011002.jpg
```

---

## Step 3: Generate ArUco Markers

Run:

```bash
python 02_generate_aruco.py
```

The script:

- Reads all files in:

```text
renamed_photos/
```

- Creates a unique ArUco marker for each person
- Saves markers in:

```text
aruco_markers/
```

- Creates:

```text
marker_mapping.csv
```

Example:

```csv
marker_id,person_id
0,22011001
1,22011002
2,22011003
```

Generated markers:

```text
aruco_markers/
├── 22011001_aruco.png
├── 22011002_aruco.png
├── 22011003_aruco.png
```

---

## Step 4: Print or Display Markers

You can:

- Print markers on paper
- Display them on phones
- Attach them to ID cards

Each marker uniquely identifies a person.

---

## Step 5: Scan ArUco Markers

Run:

```bash
python 03_scan_aruco.py
```

The script:

- Opens the webcam
- Detects ArUco markers
- Looks up the marker in:

```text
marker_mapping.csv
```

- Displays the corresponding Person ID

Example:

```text
Detected Person ID: 22011001
```

Press:

```text
ESC
```

to exit.

---

# Example End-to-End Flow

```text
Original Photo
      │
      ▼
OCR Reads ID
      │
      ▼
Photo Renamed
      │
      ▼
Generate ArUco Marker
      │
      ▼
Save Mapping CSV
      │
      ▼
Print Marker
      │
      ▼
Scan Marker
      │
      ▼
Retrieve Person ID
```

---

# Troubleshooting

## OCR Not Detecting IDs

Try:

- Increasing image quality
- Using higher contrast images
- Increasing crop area

Current crop:

```python
crop = img[int(h * 0.75):h, :]
```

Change if IDs are not located in the bottom 25%.

---

## Webcam Not Opening

Try changing:

```python
cap = cv2.VideoCapture(0)
```

to:

```python
cap = cv2.VideoCapture(1)
```

if multiple cameras are connected.

---

## Marker Not Detected

Ensure:

- Marker is fully visible
- Marker is not blurry
- Adequate lighting exists
- Marker is printed at a reasonable size

---

# Future Improvements

Possible enhancements:

- Attendance system
- Excel attendance export
- Student database integration
- Name and department lookup
- Face verification
- QR code support
- Web dashboard
- Real-time attendance tracking

---

# License

This project is provided for educational and research purposes.
