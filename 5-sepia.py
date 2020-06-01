from PIL import Image

og_image = Image.open("img/pikachu.png")
image = og_image.copy()

for col in range(image.width):
    for row in range(image.height):
        coords = (col, row,)
        red, green, blue, alpha = image.getpixel(coords)

        sepia_colors = []

        sepia_colors.append(int((red * .393) + (green *.769) + (blue * .189)))
        sepia_colors.append(int((red * .349) + (green *.686) + (blue * .168)))
        sepia_colors.append(int((red * .272) + (green *.534) + (blue * .131)))
        sepia_colors.append(alpha)

        for index, color in enumerate(sepia_colors):
            if color > 255:
                sepia_colors[index] = 255
        
        sepia_colors = tuple(sepia_colors)

        image.putpixel(coords, sepia_colors)

image.show()
image.save("img/pikachu-sepia.png")
