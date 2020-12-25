from PIL import Image, ImageDraw,ImageFont

msg_hanzi = u'''1,如公式所示：'''
font_size =16
fillColor = "black"  # 设置字体颜色
setFont = ImageFont.truetype('C:/windows/fonts/Dengl.ttf', font_size) #设置字体以及字体大小
W,H=setFont.getsize(msg_hanzi)
print(H)
# W, H = (335,16)
im = Image.new("RGBA",(W,H),"white")
draw = ImageDraw.Draw(im)
msg_list = msg_hanzi.split('\n')  # 分割字符串成列表
print(msg_list)
# for i in range(len(msg_list)):
draw.text((0, 0 ), msg_hanzi, font=setFont,fill = fillColor)
im.show()
im.save("hello1.png", "PNG")