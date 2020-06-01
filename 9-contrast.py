from PIL import Image

og_image = Image.open("img/pikachu.png")
image = og_image.copy()

for col in range(image.width):
    for row in range(image.height):
        coords = (col, row,)
        pixel = og_image.getpixel(coords)

        contrast_pixel = ()
        for color in pixel[:-1]:
            if color < 128:
                color = int(color / 2)
            else:
                color = color * 2

                if color > 255:
                    color = 255
            
            contrast_pixel += (color,)

        contrast_pixel += (pixel[-1],)

        image.putpixel(coords, contrast_pixel)

image.show()
image.save("img/pikachu-contrast.png")
