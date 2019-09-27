from PIL import Image

im = Image.open("image.bmp")
im.show
imgwidth, imgheight = im.size

print(im.size)

height = int(imgheight / 4)
width = int(imgwidth / 4)

print(height, width)

x = 1
for i in range(0, imgheight, height):
    y = 1
    for j in range(0, imgwidth, width):
        box = (j, i, j + width, i + height)
        a = im.crop(box)
        if x != 4 or y != 4:
            a.save("image{}{}.bmp".format(x, y))
        y += 1
    x += 1

