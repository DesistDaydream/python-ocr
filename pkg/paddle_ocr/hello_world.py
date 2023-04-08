from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(
    use_angle_cls=True, lang="ch"
)  # need to run only once to download and load model into memory
img_path = "./imgs/example.png"
ocrResult = ocr.ocr(img_path, cls=True)
# ocrResult 是一个 list 类型
# 其中每个元素是一个 list
# list 中的每个元素是一个 tuple
# tuple 中
# - 第一个元素是一个 list，表示识别到的文本框的四个顶点坐标
# - 第二个元素是一个 tuple，表示识别到的文本框中的文本和可信度
for idx in range(len(ocrResult)):
    res = ocrResult[idx]
    for line in res:
        print("这是识别到的文本框的四个顶点坐标: ", type(line[0]), line[0])
        print("这是识别到的文本框中的文本和可信度: ", type(line[1]), line[1])

# 显示结果
# 如果本地没有simfang.ttf，可以在doc/fonts目录下下载
from PIL import Image

ocrResult = ocrResult[0]
image = Image.open(img_path).convert("RGB")
boxes = [line[0] for line in ocrResult]
txts = [line[1][0] for line in ocrResult]
scores = [line[1][1] for line in ocrResult]
im_show = draw_ocr(image, boxes, txts, scores, font_path="doc/fonts/simfang.ttf")
im_show = Image.fromarray(im_show)
im_show.save("result.jpg")
