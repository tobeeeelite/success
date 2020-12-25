from PIL import Image, ImageDraw,ImageFont


msg_english = u'1,SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO'

font_size = 16
fillColor = "black"  # 设置字体颜色
setFont = ImageFont.truetype('C:/windows/fonts/Dengl.ttf', font_size)
W, H = setFont.getsize(msg_english)
im = Image.new("RGBA",(W,H),"white")
draw = ImageDraw.Draw(im)

draw.text((0,0), msg_english,font=setFont, fill="black")
im.show()
im.save("hello.png", "PNG")