from paddleocr import PaddleOCR, draw_ocr

img_path = "./25.pdf"

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch", page_num=2)
result = ocr.ocr(img_path, cls=True)

print(result)
