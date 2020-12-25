import random
import string
from PIL import Image, ImageDraw, ImageFont

step = 8
b = []
d = []

##符号

##随机生成汉字
for j in range(8 * 224):
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x}{body:x}'
    str1 = bytes.fromhex(val).decode('gb2312', errors='ignore')
    b.append(str1)
    # print(b)
print(b)
c = [b[i:i + step] for i in range(0, len(b), step)]
print(len(c))
print(c[0])
punc = string.punctuation
for n in range(0, len(c)):

    num = random.randint(1, 224)
    c[n].insert(0, num)
    # c[n].insert(1, punc)
    # c[n].append(punc)
    c[n].insert(1, punc[13])
    c[n].append(punc[15])
print(c[0])
##将列表元素都转成字符串
for k in range(0, 224):
    c[k][0] = str(c[k][0])
print(c[0])
# 将列表里面的元素合成一个元素
d = [''.join(c[i]) for i in range(0, len(c))]
print(len(d))
print(d[0])
msg_hanzi = d
font_size = 48
fillColor = "black"  # 设置字体颜色
setFont = ImageFont.truetype('C:/windows/fonts/simhei.ttf', font_size)  # 设置字体以及字体大小
for a in range(0, len(d)):
    W, H = setFont.getsize(msg_hanzi[a])
    print(W, H)

    im = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(im)

    # for i in range(len(msg_list)):
    draw.text((0, 0), msg_hanzi[a], font=setFont, fill=fillColor)

    im.save('D:\pycharm\work\hanzi/%d.png' % (a), "PNG")
