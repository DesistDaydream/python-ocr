#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from paddleocr import PaddleOCR
import cv2

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(
    use_angle_cls=True, lang="ch"
)  # need to run only once to download and load model into memory
img_path = "D:\\Projects\\dtcg\\images\\cn\\EXC-01\\EX2-060.png"
# img_path = "imgs/EX2-065_01.png"

img = cv2.imread(img_path)
cardType = img[10:28, 191:239]
cardSerial = img[450:464, 335:398]

# cv2.imwrite("imgs/cardTypeArea.png", cardType)
# cv2.imwrite("imgs/cardSerialArea.png", cardSerial)

cardTypeResult = ocr.ocr(cardType, cls=True)
cardSerialResult = ocr.ocr(cardSerial, cls=True)

for idx in range(len(cardTypeResult)):
    res = cardTypeResult[idx]
    for line in res:
        print(line[1][0])
for idx in range(len(cardSerialResult)):
    res = cardSerialResult[idx]
    for line in res:
        print(line[1][0])

# [[2.0, 2.0], [60.0, 2.0], [60.0, 13.0], [2.0, 13.0]], ("EX2-060R", 0.9803146123886108)
