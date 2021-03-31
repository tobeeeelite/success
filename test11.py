import os, subprocess

"""
用linkscape软件将png转svg 效果没有potrace好

"""


def png_to_svg(img_path, **kwargs):
    lnkscape_path = kwargs.get('Inkscape', r"E:\lnkscape\Inkscape\inkscape.exe")

    png_filepath = img_path

    # svg_filepath = r"C:\Users\Administrator\Downloads"

    subprocess.call([lnkscape_path, png_filepath, '--export-plain-svg=c1.svg'])


if __name__ == "__main__":
    png_to_svg('c.ppm')
