# Description: Extract text from images using Tesseract OCR
import subprocess
import cv2
import pytesseract
import os
import matplotlib.pyplot as plt
from PIL import Image

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Define the folder path containing images
image_folder = r"D:\Python1\Bank Statement"  # Use raw string (r"") to avoid path issues

# Define the folder to save extracted text files
output_folder = r"D:\Python1\Image-Text"
os.makedirs(output_folder, exist_ok=True)  # Create folder if not exists

# Ensure the image folder exists
if not os.path.exists(image_folder):
    print(f"Error: Folder '{image_folder}' does not exist!")
else:
    # List all JPG files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith(".jpg") or f.endswith(".jpeg")]

    # Check if any images are found
    if len(image_files) == 0:
        print("No JPG images found in the folder!")
    else:
        print(f"Found {len(image_files)} images. Processing...\n")

        # Loop through each image and extract text
        for image_name in image_files:
            image_path = os.path.join(image_folder, image_name)

            # Load the image
            img = cv2.imread(image_path)

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply adaptive thresholding
            gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY, 11, 2)

            # Display the processed image
            plt.figure(figsize=(10,6))
            plt.imshow(gray, cmap='gray')
            plt.axis('off')
            plt.title(f"Processed Image: {image_name}")
            plt.show()

            # Run OCR using Tesseract
            custom_config = r'--oem 3 --psm 6'  # Best for structured text
            extracted_text = pytesseract.image_to_string(gray, config=custom_config)

            # Save extracted text to a .txt file
            text_filename = os.path.join(output_folder, image_name.replace(".jpg", ".txt").replace(".jpeg", ".txt"))
            with open(text_filename, "w", encoding="utf-8") as text_file:
                text_file.write(extracted_text)

            # Print confirmation
            print(f"Extracted text saved to: {text_filename}")
            print("-" * 50)  # Separator for readability
