from PIL import Image, ImageDraw
import random
import os
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color


def randomcolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# 转换RGB到LAB
def rgb_to_lab(rgb):
    rgb = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True)
    lab = convert_color(rgb, LabColor)
    lab_values = (round(lab.lab_l), round(lab.lab_a), round(lab.lab_b))
    return lab_values


# 转换LAB到RGB
def lab_to_rgb(lab):
    rgb = convert_color(lab, sRGBColor)
    # Clamp the values to be between 0 and 1 before converting to 0-255 range
    rgb_values = (
        round(min(max(rgb.rgb_r, 0.0), 1.0) * 255),
        round(min(max(rgb.rgb_g, 0.0), 1.0) * 255),
        round(min(max(rgb.rgb_b, 0.0), 1.0) * 255),
    )
    return rgb_values


def opposite_color(c, a, b, r):
    while True:
        z = random.randint(0, 100)
        x = random.randint(-128, 127)
        y = random.randint(-128, 127)
        if (z - c) ** 2 + (x + a) ** 2 + (y + b) ** 2 <= r**2:
            return z, x, y


def color_distance(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5


# 生成前景色和背景色，确保两者不同且在A轴或B轴上相反
def fgbgcolor(r=20, min_distance=80):
    while True:
        # 随机生成前景色
        rgb_fg = randomcolor()
        lab_fg = rgb_to_lab(rgb_fg)  # （L，a，b）

        # 生成背景色
        opposite_lab = opposite_color(lab_fg[0], lab_fg[1], lab_fg[2], r)
        lab_bg = LabColor(opposite_lab[0], opposite_lab[1], opposite_lab[2])
        rgb_bg = lab_to_rgb(lab_bg)

        # 确保生成的颜色在RGB范围内有效
        if (
            all(0 <= c <= 255 for c in rgb_bg)
            and min_distance < color_distance(rgb_fg, rgb_bg) < 235
            and opposite_lab[0] > lab_fg[0]
        ):
            break

    return rgb_fg, rgb_bg


def plot_type1(rgb_fg, rgb_bg, size, n, output_dir="./output_type_1_opposite"):
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
    length = round(size / n, 1)
    filename = (
        f"{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    )
    output_dir = os.path.join(output_dir, "{}_{}_{}".format(size, n, length))
    os.makedirs(output_dir, exist_ok=True)
    image.save(os.path.join(output_dir, filename))
    print(f"Saved image as {filename}")


# Generate 720x720 images
for i in range(20):
    rgb_fg, rgb_bg = fgbgcolor()
    plot_type1(rgb_fg, rgb_bg, 640, 32)
# 这里的32是指长或宽上的小方块个数为32，所以32*32=1024个小方块，用来控制间隔大小

# Generate 640x640 images
# for i in range(2):
#     rgb_fg, rgb_bg = fgbgcolor()
#     plot_pillow(rgb_fg, rgb_bg, 640, 32)
