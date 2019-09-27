from PIL import Image


def make_preview(size, n_colors):
    original_image = Image.open("image.jpg")
    resized_image = original_image.resize(size)
    # resized_image.quantize(n_colors)
    resized_image = resized_image.convert('RGB', palette=original_image.getpalette(), colors=n_colors)
    resized_image.save("res.bmp", "BMP")
    resized_image.show()

make_preview((400, 200), 64)

# http://haru-atari.com/ru/blog/26/write-elementary-image-filters-in-python
