from paddleocr import PaddleOCR, draw_ocr

img_path = "./imgs/example.png"

# 实例化 PaddleOCR
# 目前支持的多语言语种识别，可以通过修改 lang 参数进行切换。例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
# PaddleOCR 类的可用属性详见: https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_en/whl_en.md#6-parameter-description
ocr = PaddleOCR(use_angle_cls=True, lang="ch")
# 只需运行一次即可下载模型并将其加载到内存中，模型下默认下载目录在 %USERPROFILE%\.paddleocr\whl

# ocr 函数返回全部的识别结果，类型是 list，是一个图片列表，每个元素都是一张图片的识别结果信息
ocrResults = ocr.ocr(img_path, cls=True)
print("已识别完成 {} 张图片: ".format(len(ocrResults)))
# 若识别的是 图片，ocrResults 中只有一个元素，表示该图片
# 若识别的是 PDF，ocrResults 中的每个元素表示 PDF 的一页
# 也就是说，ocrResults 中的每个元素即表示一张图片的识别结果

# TODO: 有没有办法不通过 PDF 的方式同时识别多个图片？
# img_path = ["./imgs/example.png", "./imgs/example2.png"] 这样会报错：AttributeError: 'str' object has no attribute 'shape'

# 逐一处理识别到的每张图片
for indexResult, result in enumerate(ocrResults):
    print("######################################")
    # 每张图片的识别结果信息也是 list 类型，是一个文本块列表，每个元素都是这张图片中识别到的文本块，可以是一行文本或一列文本
    print("第 {} 张图片识别到了 {} 行信息 ".format(indexResult + 1, len(result)))

    # 文本块用矩形框框起来，可以从 result.jpg 图片中看到效果
    for index, textBox in enumerate(result):
        print("========================================")
        print("这是识别到的第 {} 块信息: ".format(index + 1))

        # 每个文本块只包含两个元素
        # 第一个元素是 list 类型，表示文本框的四个顶点坐标
        # 第二个元素是 tuple 类型，表示文本框内的文本和置信度
        print("文本框的四个顶点坐标: ", textBox[0])
        print("文本框中的文本和置信度: ", textBox[1])


# 显示结果
# 如果本地没有simfang.ttf，可以在doc/fonts目录下下载
from PIL import Image

result = ocrResults[0]
image = Image.open(img_path).convert("RGB")
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path="doc/fonts/simfang.ttf")
im_show = Image.fromarray(im_show)
im_show.save("imgs/result.jpg")
