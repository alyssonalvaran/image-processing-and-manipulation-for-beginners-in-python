from PIL import Image

og_image = Image.open("img/pikachu.png")
image = og_image.copy()

for col in range(int(image.width / 2)):
    for row in range(image.height):
        coords = (col, row,)
        mirror_coords = (image.width - col - 1, row,)
        pixel = image.getpixel(mirror_coords)

        image.putpixel(coords, pixel)

image.show()
image.save("img/pikachu-mirror.png")
