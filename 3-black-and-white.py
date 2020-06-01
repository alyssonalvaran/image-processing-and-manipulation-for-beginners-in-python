from PIL import Image

og_image = Image.open("img/pikachu.png")
image = og_image.copy()

for col in range(image.width):
    for row in range(image.height):
        coords = (col, row,)
        pixel = image.getpixel(coords)

        average = sum(pixel) / 3

        if average < 128:
            average = 0
        else:
            average = 255

        masked_colors = (average,) * 3 + (pixel[-1],)
        image.putpixel(coords, masked_colors)

image.show()
image.save("img/pikachu-black-and-white.png")
