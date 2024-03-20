from AksharaJaana.main import OCREngine
from AksharaJaana.utils import ModelTypes, FileOperationUtils

ocr = OCREngine(modelType=ModelTypes.Easyocr)
# choices are Paddleocr, Easyocr, Tesseract

text = ocr.get_text_from_file("./Images/ss.jpg")
print(text)