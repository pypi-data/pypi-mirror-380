import io
from PIL import Image, ImageEnhance
class ImagePreprocessor:
    @staticmethod
    def process(filepath):
        """Preprocess image and return file-like object (not saved)."""
        img = Image.open(filepath)
        img_sharp = ImageEnhance.Sharpness(img).enhance(2.5)
        brightened = ImageEnhance.Brightness(img_sharp).enhance(2)
        img_bytes = io.BytesIO()
        brightened.save(img_bytes, format=img.format)
        img_bytes.seek(0)
        return img_bytes