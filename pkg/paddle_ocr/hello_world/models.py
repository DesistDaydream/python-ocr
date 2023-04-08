from paddleocr import PaddleOCR, paddleocr, draw_ocr

img = "./imgs/example.png"
img_word = "./imgs/word/cardSerialArea.png"

paddleocr.logging.disable()
ocr = PaddleOCR(lang="ch")


# 仅使用 Detection 检测模型
def DetectionModel():
    result = ocr.ocr(img, cls=False, det=True, rec=False)
    print(result)


# 仅使用 Recognition 识别模型
def RecognitionModel():
    ocrResults = ocr.ocr(img, cls=False, det=False, rec=True)
    print("一张完整的图片，背景信息较多，无法识别出有价值的信息: ", ocrResults)
    ocrResultsWord = ocr.ocr(img_word, cls=False, det=False, rec=True)
    print("一张图片中，背景信息较少，基本都是文本，可以识别出文本信息: ", ocrResultsWord)


if __name__ == "__main__":
    # 检测模型用来检查一个图片中，哪些地方可以被识别模型识别，该模型通常只是返回一组坐标。
    # DetectionModel()
    # 通常来说图片中只包含文本，背景信息非常少时，才能通过识别模型识别出来，若背景信息过多，那么识别出来的结果一般为空。比如 imgs/word/ 目录中的图片，就属于整张图片中，绝大部分都是文件的情况。
    RecognitionModel()
    # 整个 OCR 模型，通常由检测模型检测到需要识别的目标（即兴趣点，或者说图片中部分位置的坐标），然后将这些坐标传递给识别模型，识别模型识别出文本。
