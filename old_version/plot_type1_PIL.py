from PIL import Image, ImageDraw
import random
import os

output = "./output_pillow_1"
os.makedirs(output, exist_ok=True)


def randomcolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def color_distance(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5


def calculate_luminance(r, g, b):
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def fgbgcolor(min_distance=200):
    rgb_fg = randomcolor()
    rgb_bg = randomcolor()
    while color_distance(rgb_fg, rgb_bg) < min_distance and calculate_luminance(
        rgb_fg[0], rgb_fg[1], rgb_fg[2]
    ) > calculate_luminance(rgb_bg[0], rgb_bg[1], rgb_bg[2]):
        rgb_fg = randomcolor()
    return rgb_fg, rgb_bg


def plot_pillow(rgb_fg, rgb_bg, size, n, output_dir=output):
    image = Image.new("RGB", (size, size), rgb_bg)
    draw = ImageDraw.Draw(image)

    for i in range(n):
        for j in range(n):
            color = rgb_fg if (i + j) % 2 == 0 else rgb_bg
            draw.rectangle(
                [
                    i * size // n,
                    j * size // n,
                    (i + 1) * size // n,
                    (j + 1) * size // n,
                ],
                fill=color,
            )

    filename = (
        f"{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    )
    image.save(os.path.join(output_dir, filename))
    print(f"Saved image as {filename}")


# Generate 720x720 images
for i in range(20):
    rgb_fg, rgb_bg = fgbgcolor()
    plot_pillow(rgb_fg, rgb_bg, 720, 32)
# 这里的32是指长或宽上的小方块个数为32，所以32*32=1024个小方块，用来控制间隔大小

# Generate 640x640 images
# for i in range(2):
#     rgb_fg, rgb_bg = fgbgcolor()
#     plot_pillow(rgb_fg, rgb_bg, 640, 32)
