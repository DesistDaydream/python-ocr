#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import msvcrt

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    if msvcrt.kbhit():  # 检测是否有按键输入
        key = msvcrt.getch()
        if key == b"q":  # 如果输入 'q'，退出程序
            break
        else:
            print("输入的按键是：", key)

# 退出程序时释放摄像头
cap.release()
