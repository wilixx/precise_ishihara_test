from PIL import Image, ImageDraw, ImageFont
# get an image
# base = Image.open('Pillow/Tests/images/lena.png').convert('RGBA')
base = Image.new('RGBA', (128,128), (255,255,255,0))

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (15,126,255,0))

# get a font
# fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
fnt = ImageFont.truetype('SIMHEI.TTF', 40)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
# d.text(xy, text, fill, font, anchor)
d.text((10,10), "Hello", font=fnt, fill=(105,22,25,128))
# draw text, full opacity
d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

out = Image.alpha_composite(base, txt)

out.show()
Image.Image.save(out, "hello_image.png", "png")