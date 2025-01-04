import os
os.chdir("/home/ibrazebra/src/github.com/PaddleOCR/ppocr_img")

# 1. Import PaddleOCR class from paddleocr
from paddleocr import PaddleOCR


# 2. Declare the PaddleOCR class
ocr = PaddleOCR()
img_path ='./imgs_en/img_12.jpg'
# 3. Perform inference
result = ocr.ocr(img_path, cls=True)
#print(f"The predicted text box of {img_path} are follows.")
print(result)
