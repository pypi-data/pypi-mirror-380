# OCR Extractor

[![PyPI version](https://img.shields.io/pypi/v/ocr-pro?color=green)](https://pypi.org/project/ocr-pro/)
[![Python versions](https://img.shields.io/pypi/pyversions/ocr-pro.svg)](https://pypi.org/project/ocr-pro/)
[![License](https://img.shields.io/pypi/l/ocr-pro?color=yellow)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/pypi/dm/ocr-pro?color=orange)](https://pypi.org/project/ocr-pro/)

A simple and efficient OCR-based data extraction tool for Indian PAN and
Aadhaar cards using [Tesseract
OCR](https://github.com/tesseract-ocr/tesseract).

## 🆕 What's New in v0.1.2

- Added `tesseract_cmd` parameter to `ExtractAadhaarData` and `ExtractPanData` for custom Tesseract paths.  
- Fixed issue with preprocessing argument (`preprocess`) in child classes not being passed correctly.  

*(For full version history, see [CHANGELOG.md](CHANGELOG.md))*

## ✨ Features

- Extract PAN card data with a single function call
- Extract Aadhaar card data with a single function call
- Built-in preprocessing option for better OCR accuracy
- Cross-platform support (Windows, Linux, macOS) with configurable
  Tesseract path

## 📦 Installation

```bash
pip install ocr-pro
```

## 🚀 Usage

### Extract PAN Card Data

```python
from ocr import ExtractPanData

# Default usage (preprocess=False by default)
pan_data = ExtractPanData("pan_image.jpg", tesseract_cmd="/usr/bin/tesseract")

print(pan_data)
```

### Extract Aadhaar Card Data

```python
from ocr import ExtractAadhaarData

# You can also enable preprocessing
aadhaar_data = ExtractAadhaarData("aadhaar_image.jpg", tesseract_cmd="/usr/bin/tesseract", preprocess=True)

print(aadhaar_data)
```

### Arguments

- **filepath** *(str)* → Path to the image file
- **tesseract_cmd** *(str, optional)* → Path to the Tesseract
  executable (default: system auto-detection or
  `"C:\Program Files\Tesseract-OCR\tesseract.exe"` on Windows)
- **preprocess** *(bool, default=False)* → Whether to apply
  preprocessing for better OCR results

## ⚙️ Requirements

- Python 3.7+
- [Tesseract OCR](https://tesseract-ocr.github.io/) installed on your
  system

## 📜 License

MIT License
