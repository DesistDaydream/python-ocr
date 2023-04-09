from dataclasses import dataclass
from paddleocr import PaddleOCR, paddleocr
import cv2
import msvcrt


@dataclass
class CardQuantity:
    serial: str
    quantity: int


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", show_log=False)
    card_quantities = {}

    while True:
        if msvcrt.kbhit():  # 检测是否有按键输入
            key = msvcrt.getch()
            if key == b"q":  # 如果输入 'q'，退出程序
                break
            else:
                retval, frame = cap.read()  # 此刻拍照
                if not retval:
                    print("无法接收到帧，请重试")

                if key == b"s":
                    file = "imgs/example.png"
                    cv2.imwrite(file, frame)
                    img = cv2.imread(file)
                    # cardSerial = img[450:464, 335:398]

                ocrResults = ocr.ocr(frame, cls=True)
                for idx in range(len(ocrResults)):
                    ocrResult = ocrResults[idx]
                    for textBox in ocrResult:
                        text = textBox[1][0]
                        if "EX" in text:
                            cardSerial: str = text[:7]
                            print("已识别卡牌:", cardSerial)
                            if cardSerial in card_quantities:  # 如果已经有过记录，则将数量加1
                                card_quantities[cardSerial].quantity += 1
                            else:
                                cq = CardQuantity(
                                    cardSerial, 1
                                )  # 如果是新的卡牌，创建一个 CardQuantity 对象
                                card_quantities[cardSerial] = cq
                            print("当前已添加卡牌信息:")
                            for key in card_quantities:
                                cq = card_quantities[key]
                                print("卡牌序列号: ", cq.serial, ", 数量: ", cq.quantity)

    cap.release()
