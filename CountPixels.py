from PIL import Image
im = Image.open('place-1690285095445.png')

# all counts of the color
pixel_count = {
    "burgundy": 0, "dark_red": 0, "red": 0, "orange": 0, "yellow": 0, "pale_yellow": 0, "dark_green": 0,
    "green": 0, "light_green": 0, "dark_teal": 0, "teal": 0, "light_teal": 0, "dark_blue": 0, "blue": 0,
    "light_blue": 0, "indigo": 0, "periwinkle": 0, "lavender": 0, "dark_purple": 0, "purple": 0, "pale_purple": 0,
    "magenta": 0, "pink": 0, "light_pink": 0, "dark_brown": 0, "brown": 0, "beige": 0, "black": 0, "dark_gray": 0,
    "gray": 0, "light_gray": 0, "white": 0
    }

#region Colors
# if your image is RGB (if RGBA, (0, 0, 0, 255) or so
burgundy = (109, 0, 26, 255)         # 0
dark_red = (190, 0, 57, 255)         # 1
red = (255, 69, 0, 255)              # 2
orange = (255, 168, 0, 255)          # 3
yellow = (255, 214, 53, 255)         # 4
pale_yellow = (255, 248, 184, 255)   # 5
dark_green = (0, 163, 104, 255)      # 6
green = (0, 204, 120, 255)           # 7
light_green = (126, 237, 86, 255)    # 8
dark_teal = (0, 117, 111, 255)       # 9
teal = (0, 158, 170, 255)            # 10
light_teal = (0, 204, 192, 255)      # 11
dark_blue = (36, 80, 164, 255)       # 12
blue = (54, 144, 234, 255)           # 13
light_blue = (81, 232, 244, 255)     # 14
indigo = (73, 58, 193, 255)          # 15
periwinkle = (106, 92, 255, 255)     # 16
lavender = (148, 179, 255, 255)      # 17
dark_purple = (129, 30, 159, 255)    # 18
purple = (180, 74, 192, 255)         # 19
pale_purple = (228, 171, 255, 255)   # 20
magenta = (222, 16, 127, 255)        # 21
pink = (255, 56, 129, 255)           # 22
light_pink = (255, 153, 170, 255)    # 23
dark_brown = (109, 72, 47, 255)      # 24
brown = (156, 105, 38, 255)          # 25
beige = (255, 180, 112, 255)         # 26
black = (0, 0, 0, 255)               # 27
dark_gray = (81, 82, 82, 255)        # 28
gray = (137, 141, 144, 255)          # 29
light_gray = (212, 215, 217, 255)    # 30
white = (255, 255, 255, 255)         # 31
#endregion

# go through pixels and sort them into the dict
for pixel in im.getdata():
    if pixel == burgundy:
        pixel_count["burgundy"] += 1
    elif pixel == dark_red:
        pixel_count["dark_red"] += 1
    elif pixel == dark_red:
        pixel_count["red"] += 1
    elif pixel == orange:
        pixel_count["orange"] += 1
    elif pixel == yellow:
        pixel_count["yellow"] += 1
    elif pixel == pale_yellow:
        pixel_count["pale_yellow"] += 1
    elif pixel == dark_green:
        pixel_count["dark_green"] += 1
    elif pixel == green:
        pixel_count["green"] += 1
    elif pixel == light_green:
        pixel_count["light_green"] += 1
    elif pixel == dark_teal:
        pixel_count["dark_teal"] += 1
    elif pixel == teal:
        pixel_count["teal"] += 1
    elif pixel == light_teal:
        pixel_count["light_teal"] += 1
    elif pixel == dark_blue:
        pixel_count["dark_blue"] += 1
    elif pixel == blue:
        pixel_count["blue"] += 1
    elif pixel == light_blue:
        pixel_count["light_blue"] += 1
    elif pixel == indigo:
        pixel_count["indigo"] += 1
    elif pixel == periwinkle:
        pixel_count["periwinkle"] += 1
    elif pixel == lavender:
        pixel_count["lavender"] += 1
    elif pixel == dark_purple:
        pixel_count["dark_purple"] += 1
    elif pixel == purple:
        pixel_count["purple"] += 1
    elif pixel == pale_purple:
        pixel_count["pale_purple"] += 1
    elif pixel == magenta:
        pixel_count["magenta"] += 1
    elif pixel == pink:
        pixel_count["pink"] += 1
    elif pixel == light_pink:
        pixel_count["light_pink"] += 1
    elif pixel == dark_brown:
        pixel_count["dark_brown"] += 1
    elif pixel == brown:
        pixel_count["brown"] += 1
    elif pixel == beige:
        pixel_count["beige"] += 1
    elif pixel == black:
        pixel_count["black"] += 1
    elif pixel == dark_gray:
        pixel_count["dark_gray"] += 1
    elif pixel == gray:
        pixel_count["gray"] += 1
    elif pixel == light_gray:
        pixel_count["light_gray"] += 1
    elif pixel == white:
        pixel_count["white"] += 1
    else:
        continue



print(pixel_count)
