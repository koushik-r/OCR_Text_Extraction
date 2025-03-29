📄 Image to Text (OCR) - Python Project

This is a Python-based Optical Character Recognition (OCR) project that extracts text from images using **Tesseract-OCR**.

📌 Features
- Extract text from images.
- It can easily extract text files from grayscale images.
- Easy to set up and use.

---

⚡ Installation & Setup
1️⃣ Clone the Repository
```sh
git clone [https://github.com/koushik-r/OCR_Text_Extraction]
cd OCR_Text_Extraction

2️⃣ Create a Virtual Environment
```sh
python -m venv ocr-venv

Activate the virtual environment:

Windows: ocr-venv\Scripts\activate
Mac/Linux: source ocr-venv/bin/activate

3️⃣ Install Required Dependencies
```sh
pip install -r requirements.txt
4️⃣ Install Tesseract OCR
Windows: Download and install Tesseract.

Linux: Install via package manager:
```sh
sudo apt install tesseract-ocr

Mac: Install using Homebrew:
```sh
brew install tesseract

5️⃣ Run the OCR Script

python ocr_script.py

📦 Required Packages

These are listed in requirements.txt:

pytesseract
Pillow
opencv-python
numpy

Install them using:
```sh
pip install -r requirements.txt

**NOTE IF THE requirements.txt IS MISSING INSTALL ALL THE PACKAGES MANUALLY**
