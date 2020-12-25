##生成单行文本
import random
import string
from PIL import Image, ImageDraw,ImageFont
b= []
msg_hanzi=[]
step=8
punc=string.punctuation
num = random.randint(1, 224)
for j in range(8):
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x}{body:x}'
    str1 = bytes.fromhex(val).decode('gb2312', errors='ignore')
    b.append(str1)
print(b)
c=[b[i:i+step] for i in range(0,len(b),step)]
print(c)
print(len(c))
b.insert(0, num)
b.insert(1, punc[13])
b.append(punc[15])

for aa in b:
    print(str(str(aa)), end='')






