import re
from .fetch_data import Extractdata

class ExtractAadhaarData(Extractdata):
    def __init__(self,imagepath, tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe", preprocess=False):
        super().__init__(imagepath, tesseract_cmd=tesseract_cmd, preprocess=preprocess)
        
    def get_aadhaar(self):
        aadhaar = self.aadhaar_data()
        aadhaar_no = re.search(r"\b\d{4}[ ]\d{4}[ ]\d{4}", aadhaar)
        aadhaar_dob = re.search("[0-9]{2}[/][0-9]{2}[/]\d{4}", aadhaar)
        aadhaar_gender = re.search("female|male", aadhaar, re.IGNORECASE)

        result = [
            aadhaar_no.group() if aadhaar_no else "Aadhaar Number Not Found", 
            aadhaar_dob.group() if aadhaar_dob else "Aadhaar DOB Not Found",
            aadhaar_gender.group() if aadhaar_gender else "Aadhaar Gender Not Found"
        ]
        return result