from PIL import Image

im = Image.open('place-1690285095445.png')

colors = {
    'burgundy': (109, 0, 26, 255),
    'dark_red': (190, 0, 57, 255),
    'red': (255, 69, 0, 255),
    'orange': (255, 168, 0, 255),
    'yellow': (255, 214, 53, 255),
    'pale_yellow': (255, 248, 184, 255),
    'dark_green': (0, 163, 104, 255),
    'green': (0, 204, 120, 255),
    'light_green': (126, 237, 86, 255),
    'dark_teal': (0, 117, 111, 255),
    'teal': (0, 158, 170, 255),
    'light_teal': (0, 204, 192, 255),
    'dark_blue': (36, 80, 164, 255),
    'blue': (54, 144, 234, 255),
    'light_blue': (81, 232, 244, 255),
    'indigo': (73, 58, 193, 255),
    'periwinkle': (106, 92, 255, 255),
    'lavender': (148, 179, 255, 255),
    'dark_purple': (129, 30, 159, 255),
    'purple': (180, 74, 192, 255),
    'pale_purple': (228, 171, 255, 255),
    'magenta': (222, 16, 127, 255),
    'pink': (255, 56, 129, 255),
    'light_pink': (255, 153, 170, 255),
    'dark_brown': (109, 72, 47, 255),
    'brown': (156, 105, 38, 255),
    'beige': (255, 180, 112, 255),
    'black': (0, 0, 0, 255),
    'dark_gray': (81, 82, 82, 255),
    'gray': (137, 141, 144, 255),
    'light_gray': (212, 215, 217, 255),
    'white': (255, 255, 255, 255),
}

pixel_count = {}
for color, pixel in colors.items():
    pixel_count[color] = 0

for pixel in im.getdata():
    for color, pixel_value in colors.items():
        if pixel == pixel_value:
            pixel_count[color] += 1

print(pixel_count)
