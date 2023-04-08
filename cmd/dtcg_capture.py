from paddleocr import PaddleOCR, paddleocr
import cv2
import msvcrt


class CardQuantity:
    def __init__(self, serial, quantity):
        self.serial = serial
        self.quantity = quantity


if __name__ == "__main__":
    paddleocr.logging.disable()

    cap = cv2.VideoCapture(0)
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
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
                    ocrResultLines = ocrResults[idx]
                    for line in ocrResultLines:
                        if "EX" in line[1][0]:
                            cardSerial: str = line[1][0]
                            cardSerial = cardSerial[:7]
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
