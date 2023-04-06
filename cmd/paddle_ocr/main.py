#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from paddleocr import PaddleOCR
import cv2

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(
    use_angle_cls=True, lang="ch"
)  # need to run only once to download and load model into memory
img_path = "D:\\Projects\\dtcg\\images\\cn\\EXC-01\\EX2-065.png"
# img_path = "imgs/EX2-065_01.png"

# 取出图片中高度12-26，宽度197-239 区域的图片
img = cv2.imread(img_path)
cardType = img[11:29, 191:239]
cv2.imwrite("imgs/messi5_new.jpg", cardType)

cardTypePath = "imgs/messi5_new.jpg"

result = ocr.ocr(cardTypePath, cls=True)

for line in result:
    print(line)
