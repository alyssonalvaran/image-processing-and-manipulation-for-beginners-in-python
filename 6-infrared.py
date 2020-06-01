from PIL import Image

og_image = Image.open("img/pikachu.png")
image = og_image.copy()

for col in range(image.width):
    for row in range(image.height):
        coords = (col, row,)
        red, green, blue, alpha = image.getpixel(coords)

        infrared_colors = (blue, red, green, alpha,)

        image.putpixel(coords, infrared_colors)

image.show()
image.save("img/pikachu-infrared.png")
