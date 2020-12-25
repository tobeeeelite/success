##PIL图像增强
from PIL import Image,ImageEnhance
image=Image.open('hello1.png')
#亮度增强
enh_bri=ImageEnhance.Brightness(image)
brightness=0.8
image_brightened=enh_bri.enhance(brightness)
image_brightened.show()
image_brightened.save('ldhello1.png','PNG')
##色度增强
enh_col=ImageEnhance.Color(image)
color=5
image_colored=enh_col.enhance(color)
image_colored.show()
image_colored.save('cohello1.png','PNG')
#对比度增强
enh_con=ImageEnhance.Contrast(image)
contrast=1.5
image_contrasted=enh_con.enhance(contrast)
image_contrasted.show()
image_contrasted.save('cnhello1.png','PNG')
#锐度增强
enh_sha=ImageEnhance.Sharpness(image)
sharpness=3
image_sharpnessed=enh_sha.enhance(sharpness)
image_sharpnessed.show()
image_sharpnessed.save('shahello.png','PNG')