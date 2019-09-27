from PIL import Image, ImageDraw

im = Image.open("image.png")
im.show
x, y = im.size

pixels = im.load()
r0, g0, b0 = pixels[0, 0]

x1 = y1 = x2 = y2 = flag = 0


def coord_x1():
    for i in range(x):
        for j in range(y):
            if (r0, g0, b0) != pixels[i, j]:
                return i


def coord_x2():
    for i in range(x - 1, 0, -1):
        for j in range(y):
            if (r0, g0, b0) != pixels[i, j]:
                return i


def coord_y1():
    for i in range(y):
        for j in range(x):
            if (r0, g0, b0) != pixels[j, i]:
                return i


def coord_y2():
    for i in range(y - 1, 0, -1):
        for j in range(x):
            if (r0, g0, b0) != pixels[j, i]:
                return i


x1 = coord_x1()
x2 = coord_x2()
y1 = coord_y1()
y2 = coord_y2()

cropped = im.crop((x1, y1, x2 + 1, y2 + 1))
cropped.save("res.png", "PNG")
# cropped.show()
