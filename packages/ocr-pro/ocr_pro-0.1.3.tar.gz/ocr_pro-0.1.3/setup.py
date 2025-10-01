from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ocr-pro",   # PyPI name
    version="0.1.3",
    author="KoustubhPK",
    author_email="koustubhpk@gmail.com",
    packages=find_packages(),
    install_requires=[
        "pytesseract",
        "pillow",
    ],
    description="OCR extractor for PAN and Aadhaar card details",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KoustubhPK/ocr-pro",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.8",
    license_files = 'LICENSE'
)