from PIL import Image
im = Image.open('place.png')

# all counts of the color
pixel_count = [0]*32
color_name = [
    "burgundy", "dark_red", "red", "orange", "yellow", "pale_yellow", "dark_green",
    "green", "light_green", "dark_teal", "teal", "light_teal", "dark_blue", "blue",
    "light_blue", "indigo", "periwinkle", "lavender", "dark_purple", "purple", "pale_purple",
    "magenta", "pink", "light_pink", "dark_brown", "brown", "beige", "black", "dark_gray",
    "gray", "light_gray", "white"]

#region Colors
# if your image is RGB (if RGBA, (0, 0, 0) or so
colors = []
colors.append((109, 0, 26, 255))         # 0
colors.append((190, 0, 57, 255))         # 1
colors.append((255, 69, 0, 255))              # 2
colors.append((255, 168, 0, 255))          # 3
colors.append((255, 214, 53, 255))         # 4
colors.append((255, 248, 184, 255))   # 5
colors.append((0, 163, 104, 255))      # 6
colors.append((0, 204, 120, 255))           # 7
colors.append((126, 237, 86, 255))    # 8
colors.append((0, 117, 111, 255))       # 9
colors.append((0, 158, 170, 255))            # 10
colors.append((0, 204, 192, 255))      # 11
colors.append((36, 80, 164, 255))       # 12
colors.append((54, 144, 234, 255))           # 13
colors.append((81, 232, 244, 255))     # 14
colors.append((73, 58, 193, 255))          # 15
colors.append((106, 92, 255, 255))     # 16
colors.append((148, 179, 255, 255))      # 17
colors.append((129, 30, 159, 255))    # 18
colors.append((180, 74, 192, 255))         # 19
colors.append((228, 171, 255, 255))   # 20
colors.append((222, 16, 127, 255))        # 21
colors.append((255, 56, 129, 255))           # 22
colors.append((255, 153, 170, 255))    # 23
colors.append((109, 72, 47, 255))      # 24
colors.append((156, 105, 38, 255))          # 25
colors.append((255, 180, 112, 255))         # 26
colors.append((0, 0, 0, 255))               # 27
colors.append((81, 82, 82, 255))        # 28
colors.append((137, 141, 144, 255))          # 29
colors.append((212, 215, 217, 255))    # 30
colors.append((255, 255, 255, 255))         # 31
#endregion

# go through pixels and sort them into the dict
for pixel in im.getdata():
    place = 0
    for color in colors:
        if pixel == color:
            pixel_count[place] += 1
        place += 1

count = 0
result = []
for color in color_name:
    result.append({color:pixel_count[count]})
    count += 1

if __name__ == "__main__":
    print(result)