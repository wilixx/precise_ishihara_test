"""
  author£º Allen
  This file to make 10 images with differnt color and different color.
  The color is taken from the d_pickle, which contains maps using a dict.
  
  d_colorPairs.pkl = {
                        "colorset1": [[r, g, b]
                                      [r, g, b]
                                      ]
                        "colorset2":[[r, g, b]
                                      [r, g, b]
                                      ]
                        }
"""


import math
import random
import sys
import pickle
from PIL import Image, ImageDraw

try:
    from scipy.spatial import cKDTree as KDTree
    import numpy as np
    IMPORTED_SCIPY = True
except ImportError:
    IMPORTED_SCIPY = False

BACKGROUND = (255, 255, 255)
TOTAL_CIRCLES = 1500
'''Change here
'''

color_pair = pickle.load(open( "d_colorPairs.pkl", "rb"))


color = lambda c: ((c >> 16) & 255, (c >> 8) & 255, c & 255)

COLORS_ON = []
COLORS_OFF = []
for color1 in color_pair["colorset1"]:
    COLORS_ON.append((color1[0],color1[1],color1[2]))
for color2 in color_pair["colorset2"]:
    COLORS_ON.append((color2[0],color2[1],color2[2]))
#     color(0xF9BB82), color(0xEBA170), color(0xFCCD84)
# (162,186,218),(91,126,45),(210,215,160)
# (164,  62,  58),(164,  62,  58),(164,  62,  58)
# ]
#     color(0x9CA594), color(0xACB4A5), color(0xBBB964),
#     color(0xD7DAAA), color(0xE5D57D), color(0xD1D6AF)
# (255,83,51),(239,196,199),(249,241,234)
# '''
# (69, 98, 52),(69, 98, 52),(100,  89,  57)
# '''

# (174,  50, 125),(174,  50, 125),(174,  50, 125)

# ]


def generate_circle(image_width, image_height, min_diameter, max_diameter):
    radius = random.triangular(min_diameter, max_diameter,
                               max_diameter * 0.8 + min_diameter * 0.2) / 2

    angle = random.uniform(0, math.pi * 2)
    distance_from_center = random.uniform(0, image_width * 0.48 - radius)
    x = image_width  * 0.5 + math.cos(angle) * distance_from_center
    y = image_height * 0.5 + math.sin(angle) * distance_from_center

    return x, y, radius


def overlaps_motive(image, (x, y, r)):
    points_x = [x, x, x, x-r, x+r, x-r*0.93, x-r*0.93, x+r*0.93, x+r*0.93]
    points_y = [y, y-r, y+r, y, y, y+r*0.93, y-r*0.93, y+r*0.93, y-r*0.93]

    for xy in zip(points_x, points_y):
        if image.getpixel(xy)[:3] != BACKGROUND:
            return True

    return False


def circle_intersection((x1, y1, r1), (x2, y2, r2)):
    return (x2 - x1)**2 + (y2 - y1)**2 < (r2 + r1)**2


def circle_draw(draw_image, image, (x, y, r)):
    fill_colors = COLORS_ON_Use if overlaps_motive(image, (x, y, r)) else COLORS_OFF_Use
    fill_color = random.choice(fill_colors)

    draw_image.ellipse((x - r, y - r, x + r, y + r),
                       fill=fill_color,
                       outline=fill_color)


def main():
    COLORS_ON = []
    COLORS_OFF = []
    
    color_pair = pickle.load(open( "d_colorPairs.pkl", "rb"))
    print len(color_pair["colorset1"])
    print color_pair["colorset1"]
    color = lambda c: ((c >> 16) & 255, (c >> 8) & 255, c & 255)

    for color1 in color_pair["colorset1"]:
        COLORS_ON.append((int(color1[0]),int(color1[1]),int(color1[2])))
    for color2 in color_pair["colorset2"]:
        COLORS_OFF.append((int(color2[0]),int(color2[1]),int(color2[2])))
    
    print COLORS_ON
    print COLORS_OFF
    
    for go in range(10):
        global COLORS_ON_Use
        global COLORS_OFF_Use
        
        COLORS_ON_Use =  [COLORS_ON[go+1]]
        COLORS_OFF_Use = [COLORS_OFF[go+1]]
        
        this_num=str(go)
        image = Image.open('number_img/number_'+this_num+'.png')
        
        image2 = Image.new('RGB', image.size, BACKGROUND)
        draw_image = ImageDraw.Draw(image2)
    
        width, height = image.size
    
        min_diameter = (width + height) / 200
        max_diameter = (width + height) / 75
    
        circle = generate_circle(width, height, min_diameter, max_diameter)
        circles = [circle]
    
        circle_draw(draw_image, image, circle)
    
        try:
            for i in xrange(TOTAL_CIRCLES):
                tries = 0
                if IMPORTED_SCIPY:
                    kdtree = KDTree([(x, y) for (x, y, _) in circles])
                    while True:
                        circle = generate_circle(width, height, min_diameter, max_diameter)
                        elements, indexes = kdtree.query([(circle[0], circle[1])], k=12)
                        for element, index in zip(elements[0], indexes[0]):
                            if not np.isinf(element) and circle_intersection(circle, circles[index]):
                                break
                        else:
                            break
                        tries += 1
                else:
                    while any(circle_intersection(circle, circle2) for circle2 in circles):
                        tries += 1
                        circle = generate_circle(width, height, min_diameter, max_diameter)
    
                print '{}/{} {}'.format(i, TOTAL_CIRCLES, tries)
    
                circles.append(circle)
                circle_draw(draw_image, image, circle)
        except (KeyboardInterrupt, SystemExit):
            pass
    
        image2.show()
        image2.save('number_plate/number_'+this_num+'.png','PNG')
        print("Okay")

if __name__ == '__main__':
    main()
