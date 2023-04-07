#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from paddleocr import PaddleOCR, paddleocr
import cv2
import msvcrt

paddleocr.logging.disable()

cap = cv2.VideoCapture(0)

while True:
    if msvcrt.kbhit():  # 检测是否有按键输入
        key = msvcrt.getch()
        if key == b"q":  # 如果输入 'q'，退出程序
            break
        else:
            f, frame = cap.read()  # 此刻拍照
            cv2.imwrite("imgs/example.png", frame)  # 将拍摄内容保存为png图片

            # 识别图片
            ocr = PaddleOCR(use_angle_cls=True, lang="ch")
            img_path = "imgs/example.png"

            img = cv2.imread(img_path)
            cardSerial = img[450:464, 335:398]

            # cv2.imwrite("imgs/cardTypeArea.png", cardType)
            # cv2.imwrite("imgs/cardSerialArea.png", cardSerial)

            cardSerialResult = ocr.ocr(img, cls=True)
            # print(cardSerialResult)
            for idx in range(len(cardSerialResult)):
                res = cardSerialResult[idx]
                for line in res:
                    # print(line)
                    # q: 如果 if line[1][0] 中包含 EX 字符串，就打印出来
                    if "EX" in line[1][0]:
                        print(line[1][0])
cap.release()
