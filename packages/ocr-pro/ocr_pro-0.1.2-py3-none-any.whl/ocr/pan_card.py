import re
from .fetch_data import Extractdata

class ExtractPanData(Extractdata):
    def __init__(self,imagepath, tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe", preprocess=False):
        super().__init__(imagepath, tesseract_cmd=tesseract_cmd, preprocess=preprocess)

    def get_pan(self):
        pan = self.pan_data()
        pan_no = re.search("[A-Z]{5}\d{4}[A-Z]{1}",pan)
        pan_dob = re.search("[0-9]{2}[/][0-9]{2}[/]\d{4}",pan)

        result = [
            pan_no.group() if pan_no else "PAN Number Not Found", 
            pan_dob.group() if pan_dob else "PAN DOB Not Found"
        ]
        return result