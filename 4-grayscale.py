from PIL import Image

og_image = Image.open("img/pikachu.png")
image = og_image.copy()

for col in range(image.width):
    for row in range(image.height):
        coords = (col, row,)
        pixel = image.getpixel(coords)

        average = int(sum(pixel) / 3)

        grayscale_colors = (average,) * 3 + (pixel[-1],)
        image.putpixel(coords, grayscale_colors)

image.show()
image.save("img/pikachu-grayscale.png")
