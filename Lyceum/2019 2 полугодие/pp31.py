from PIL import Image, ImageDraw


def makeanagliph(filename, delta):
    im = Image.open(filename)
    x, y = im.size

    new_image = Image.new('RGB', (x, y), (0, 0, 0))
    pixels2 = new_image.load()

    pixels = im.load()

    for i in range(x):
        for j in range(y):
            if i < delta:
                r, g, b = pixels[i, j]
                pixels2[i, j] = 0, g, b
            # else:
            #     g, b = pixels[i, j][1:]
            #     r = pixels[i - delta, j][0]
    new_image.save("res.jpg", "JPEG")

# makeanagliph('image.jpg', 10)
