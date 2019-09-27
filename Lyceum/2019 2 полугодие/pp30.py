from PIL import Image
from PIL import ImageDraw


def board(num, size):
    new_image = Image.new("RGB", (num * size, num * size), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for j in range(0, num * size, size):
        for i in range(0, num * size, size * 2):
            if j % (size * 2) == 0:
                draw.rectangle((i + size, j, i + size * 2, j + size), fill=(255, 255, 255))
            else:
                draw.rectangle((i, j, i + size, j + size), fill=(255, 255, 255))
    new_image.save("res.png", "PNG")

#  board(5, 30)
