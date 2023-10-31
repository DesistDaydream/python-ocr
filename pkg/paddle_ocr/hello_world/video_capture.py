from dataclasses import dataclass
from paddleocr import PaddleOCR
import cv2
import msvcrt


@dataclass
class CardQuantity:
    serial: str
    quantity: int


card_quantities: dict[str, CardQuantity] = {}


def run():
    cap = cv2.VideoCapture(0)
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", show_log=False)

    while True:
        if msvcrt.kbhit():  # 检测是否有按键输入
            key = msvcrt.getch()
            if key == b"q":  # 如果输入 'q'，退出程序
                break
            else:
                # 按任意键开始拍照
                retval, frame = cap.read()  # 拍照
                if not retval:
                    print("无法接收到帧，请重试")

                # 如果按的是 s 则保存图片
                if key == b"s":
                    file = "imgs/example.png"
                    cv2.imwrite(file, frame)
                    # img = cv2.imread(file)
                    # cardSerial = img[450:464, 335:398]

                # 开始识别图片。用 for 是 PaddleOCR 的官方写法
                ocrResults = ocr.ocr(frame, cls=True)
                for idx in range(len(ocrResults)):
                    ocrResult = ocrResults[idx]
                    ocrCard(ocrResult)

    cap.release()


# 识别
def ocrCard(ocrResult):
    # TODO: 有没有更好的方式来判断是否识别到了卡牌信息？
    print(ocrResult)


if __name__ == "__main__":
    run()
