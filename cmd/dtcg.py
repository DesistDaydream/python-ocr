#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import cv2
from paddleocr import PaddleOCR

# 在其他代码中，读取一张卡牌中感兴趣的文字块的坐标信息
# TODO: 卡牌编号的位置不一样，怎么确定呢？
cardTypeCoord = [[190.0, 10.0], [243.0, 10.0], [243.0, 28.0], [190.0, 28.0]]
cardSerialCoord = [[325.0, 450.0], [400.0, 450.0], [400.0, 468.0], [325.0, 468.0]]
# 将坐标转换为 NumPy 数组
cardTypeVertices = np.array(cardTypeCoord, dtype=np.int32)
cardSeriaVertices =  np.array(cardSerialCoord, dtype=np.int32)
# print(cardTypeVertices)
# print(cardSeriaVertices)

img_path = "D:\\Projects\\dtcg\\images\\cn\\BTC-06\\BT11-112.png"
# img_path = "imgs/EX2-065_01.png"

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch")

img = cv2.imread(img_path)
cardType = img[cardTypeVertices[0][1]:cardTypeVertices[2][1], cardTypeVertices[0][0]:cardTypeVertices[1][0]]
cardSerial = img[cardSeriaVertices[0][1]:cardSeriaVertices[2][1], cardSeriaVertices[0][0]:cardSeriaVertices[1][0]]

# 将感兴趣区域的像素写入到新的文件中，用以检查图片裁切是否正常
# cv2.imwrite("imgs/cardTypeArea.png", cardType)
# cv2.imwrite("imgs/cardSerialArea.png", cardSerial)

cardTypeResult = ocr.ocr(cardType)
cardSerialResult = ocr.ocr(cardSerial)
# print(cardTypeResult,cardSerialResult)

for idx in range(len(cardTypeResult)):
    res = cardTypeResult[idx]
    for line in res:
        print("类型: ",line[1][0]) # 文本
for idx in range(len(cardSerialResult)):
    res = cardSerialResult[idx]
    for line in res:
        print("编号: ",line[1][0]) # 文本
