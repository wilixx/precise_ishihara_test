# -*- coding: utf-8 -*-
"""
    colors-picker
    ~~~~~~~~~~
    Grabbing the color palette from images from a path.
    Then save it to "colors.json" as a form of 
    :[
        [(r,g,b),(r,g,b),(r,g,b),(r,g,b),(r,g,b),(r,g,b),...],
        [(r,g,b),(r,g,b),(r,g,b),(r,g,b),(r,g,b),(r,g,b),...],
        [(r,g,b),(r,g,b),(r,g,b),(r,g,b),(r,g,b),(r,g,b),...],
        [(r,g,b),(r,g,b),(r,g,b),(r,g,b),(r,g,b),(r,g,b),...],
        [(r,g,b),(r,g,b),(r,g,b),(r,g,b),(r,g,b),(r,g,b),...],
        ...
    ].
    :copyright: (c) 2018 by Allen Guo.
    :license: BSD, see LICENSE for more details.
"""
__version__ = '0.0.1'
import math
import glob, os
from PIL import Image
from PIL import ImageDraw
import json
import colorthief
import PIL
colors=[]
patterns=[]
print("start go")

for filename in glob.glob("ishihara-elbum/circle/*.jpg"):
    base=Image.open(filename)
    # base=base.convert("RGBA")
    color_o=colorthief.ColorThief(filename)
    p=color_o.get_palette(6, quality=10)
#     for x in p:
#         colors.append((x[0],x[1],x[2]))
        
    patterns.append(p)
#     im_blank=Image.new('RGB', base.size, (255,255,255))
#     i=0
#     image_=ImageDraw.ImageDraw(im_blank)
#     for item in p:
#         image_.polygon([(1,1+i),(1,10+i),(96,10+i),(96,1+i)], fill=item)
#         i=i+10
#     del image_
#     im_blank.show()
# print(patterns)
print("start write")
file = open('circle.json','w')
# json.dump(patterns,file,ensure_ascii=False)
json.dump(patterns, file, ensure_ascii=False)
# json.dump(obj, fp, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, encoding, default, sort_keys)