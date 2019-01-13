import math
import random
import sys

from PIL import Image, ImageDraw

try:
    from scipy.spatial import cKDTree as KDTree
    import numpy as np
    IMPORTED_SCIPY = True
except ImportError:
    IMPORTED_SCIPY = False

BACKGROUND = (255, 255, 255)
TOTAL_CIRCLES = 2000

color = lambda c: ((c >> 16) & 255, (c >> 8) & 255, c & 255)

COLORS_ON = [
#     color(0xF9BB82), color(0xEBA170), color(0xFCCD84)
(162,186,218),(91,126,45),(210,215,160)
]
COLORS_OFF = [
#     color(0x9CA594), color(0xACB4A5), color(0xBBB964),
#     color(0xD7DAAA), color(0xE5D57D), color(0xD1D6AF)
(255,83,51),(239,196,199),(249,241,234)
]


def generate_circle(image_width, image_height, min_diameter, max_diameter):
    radius = random.triangular(min_diameter, max_diameter,
                               max_diameter * 0.8 + min_diameter * 0.2) / 2

    angle = random.uniform(0, math.pi * 2)
    distance_from_center = random.uniform(0, image_width * 0.48 - radius)
    x = image_width  * 0.5 + math.cos(angle) * distance_from_center+2
    y = image_height * 0.5 + math.sin(angle) * distance_from_center+2

    return x, y, radius


def overlaps_motive(image, (x, y, r)):
    points_x = [x, x, x, x-r, x+r, x-r*0.93, x-r*0.93, x+r*0.93, x+r*0.93]
#     points_x = [x, x, x, x-r, x+r, x-r*0.99, x-r*0.99, x+r*0.99, x+r*0.99]
    points_y = [y, y-r, y+r, y, y, y+r*0.93, y-r*0.93, y+r*0.93, y-r*0.93]
#     points_y = [y, y-r, y+r, y, y, y+r*0.99, y-r*0.99, y+r*0.99, y-r*0.99]

    for xy in zip(points_x, points_y):
        if image.getpixel(xy)[:3] != BACKGROUND:
            return True

    return False


def circle_intersection((x1, y1, r1), (x2, y2, r2)):
    return (x2 - x1)**2 + (y2 - y1)**2 < (r2 + r1)**2


def circle_draw(draw_image, image, (x, y, r)):
#     fill_colors = COLORS_ON if overlaps_motive(image, (x, y, r)) else COLORS_OFF
#     fill_colors = image.getpixel(xy)
#     fill_color = random.choice(fill_colors)
    for xy in zip([x],[y]):
        
        fill_color = image.getpixel(xy)
        print(x,y,r)
        print(fill_color)
        fill_color = image.getpixel(xy)[:3]
        


#     fill_color = image.getpixel(zip(x,y))

    draw_image.ellipse((x - r, y - r, x + r, y + r),
                       fill=fill_color,
                       outline=fill_color)


def main():
#     image = Image.open(sys.argv[1])
    image = Image.open('this_is_6.png')
    image = Image.open('new-black-frog.png')

    image = Image.open('k_means_flower.png')
    image2 = Image.new('RGB', image.size, BACKGROUND)
    draw_image = ImageDraw.Draw(image2)

    width, height = image.size

    min_diameter = (width + height) / 300
    max_diameter = (width + height) / 50

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
    image2.save("k_means_flower_ishihara.png",'PNG')
    print("Okay")

if __name__ == '__main__':
    main()