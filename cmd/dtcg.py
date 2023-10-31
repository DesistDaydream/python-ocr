#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
from paddleocr import PaddleOCR

# 在其他代码中，读取一张卡牌，并获取感兴趣的文字块的坐标信息
cardTypeCoord = [[200.0, 12.0], [226.0, 10.0], [228.0, 23.0], [202.0, 26.0]]
cardSerialCoord = [[337.0, 451.0], [398.0, 451.0], [398.0, 465.0], [337.0, 465.0]]
# 将坐标转换为 NumPy 数组
cardTypeVertices = np.array(cardTypeCoord, dtype=np.int32)
cardSeriaVertices =  np.array(cardSerialCoord, dtype=np.int32)

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(
    use_angle_cls=True, lang="ch"
)  # need to run only once to download and load model into memory
img_path = "D:\\Projects\\dtcg\\images\\cn\\EXC-01\\EX1-068.png"
# img_path = "imgs/EX2-065_01.png"

img = cv2.imread(img_path)
# cardType = img[10:28, 191:239]
# cardSerial = img[450:464, 335:398]
cardType = img[cardTypeVertices[0][1]:cardTypeVertices[2][1], cardTypeVertices[0][0]:cardTypeVertices[1][0]]
cardSerial = img[cardSeriaVertices[0][1]:cardSeriaVertices[2][1], cardSeriaVertices[0][0]:cardSeriaVertices[1][0]]


# cv2.imwrite("imgs/cardTypeArea.png", cardType)
# cv2.imwrite("imgs/cardSerialArea.png", cardSerial)

cardTypeResult = ocr.ocr(cardType, cls=True)
cardSerialResult = ocr.ocr(cardSerial, cls=True)

# print(cardTypeResult,cardSerialResult)

for idx in range(len(cardTypeResult)):
    res = cardTypeResult[idx]
    for line in res:
        print(line[0]) # 位置
        print(line[1][0]) # 文本
for idx in range(len(cardSerialResult)):
    res = cardSerialResult[idx]
    for line in res:
        print(line[0]) # 位置
        print(line[1][0]) # 文本

# [[2.0, 2.0], [60.0, 2.0], [60.0, 13.0], [2.0, 13.0]], ("EX2-060R", 0.9803146123886108)
