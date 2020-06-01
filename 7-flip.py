from PIL import Image

og_image = Image.open("img/pikachu.png")
image = Image.new(og_image.mode, og_image.size)

for col in range(image.width):
    for row in range(image.height):
        coords = (col, row,)
        flip_coords = (image.width - col - 1, row,)
        pixel = og_image.getpixel(flip_coords)

        image.putpixel(coords, pixel)

image.show()
image.save("img/pikachu-flip.png")
