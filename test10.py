"""
将png转成pnm
"""
from PIL import Image

im = Image.open(r"E:\work\segmentation\企业微信截图_16170666933106.png")
im.save("07.ppm")
# from PIL import Image
# import os, sys
#
# im = Image.open("000.png")
# bg = Image.new("RGB", im.size, (255,255,255))
# bg.paste(im,im)
# bg.save("colors.jpg")
