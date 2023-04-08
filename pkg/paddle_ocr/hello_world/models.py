from paddleocr import PaddleOCR, paddleocr

img_path = "./imgs/example.png"

paddleocr.logging.disable()
ocr = PaddleOCR(lang="ch")

# 仅使用 Detection 检测模型
ocrResults = ocr.ocr(img_path, cls=False, det=True, rec=False)
print(ocrResults)

# 仅使用 Recognition 识别模型
ocrResults = ocr.ocr(img_path, cls=False, det=False, rec=True)
print(ocrResults)
