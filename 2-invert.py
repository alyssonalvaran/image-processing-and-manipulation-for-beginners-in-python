from PIL import Image

og_image = Image.open("img/pikachu.png")
image = og_image.copy()

for col in range(image.width):
    for row in range(image.height):
        coords = (col, row,)
        pixel = image.getpixel(coords)

        inverted_colors = ()
        for color in pixel[:-1]:
            inverted_colors += (255 - color,)
        
        inverted_colors += (pixel[-1],)

        image.putpixel(coords, inverted_colors)

image.show()
image.save("img/pikachu-invert.png")
