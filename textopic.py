###将文本数据画在图片上
from PIL import Image, ImageFont, ImageDraw
import cv2 as cv
text = u"这是一段测试文本，test 123。"
font = ImageFont.truetype('C:/windows/fonts/Dengl.ttf', 16)
W,H=font.getsize(text)
print(font.getsize(text))
im = Image.new("RGB", (W, H), 'white')
dr = ImageDraw.Draw(im)

dr.text((0, 0), text, font=font, fill="#000000")
im.show()
im.save("t.png")
