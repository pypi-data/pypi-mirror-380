import os
import pytesseract
from PIL import Image
from .image_preprocessor import ImagePreprocessor

class Extractdata():
    def __init__(self, filepath, tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe", preprocess=False):
        """
        filepath: str (path to image file)
        preprocess: bool -> if True, preprocess before OCR
        """
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

        self.filepath = filepath
        self.preprocess = preprocess

    def pan_data(self):
        if self.preprocess:
            img = Image.open(ImagePreprocessor.process(self.filepath))
            base_name = os.path.basename(self.filepath).split(".")[0]
        else:
            img = Image.open(self.filepath)
            base_name = os.path.basename(self.filepath).split(".")[0]

        # OCR
        self.text = pytesseract.image_to_string(img)

        # Save extracted text
        create_folder = "result/pan_data"
        os.makedirs(create_folder, exist_ok=True)

        create_file = f"{base_name}.txt"
        full_path = os.path.join(create_folder, create_file)

        with open(full_path, "w+", encoding="utf-8") as f:
            f.write(self.text)

        return self.text

    
    def aadhaar_data(self):
        if self.preprocess:
            img = Image.open(ImagePreprocessor.process(self.filepath))
            base_name = os.path.basename(self.filepath).split(".")[0]
        else:
            img = Image.open(self.filepath)
            base_name = os.path.basename(self.filepath).split(".")[0]

        # OCR
        self.text = pytesseract.image_to_string(img)

        create_folder = "result/aadhaar_data"
        os.makedirs(create_folder, exist_ok=True)

        create_file = f"{base_name}.txt"
        full_path = os.path.join(create_folder, create_file)

        with open(full_path, "w+", encoding="utf-8") as f:
            f.write(self.text)

        return self.text