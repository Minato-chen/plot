from PIL import Image, ImageDraw
import random
import os
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color


# 随机生成颜色
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
            and opposite_lab[0] < lab_fg[0]
        ):
            break

    return rgb_fg, rgb_bg


# 绘制图案函数
def plot_pillow(rgb_fg, rgb_bg, size, n, grid_line_factor, output_dir="./output_type_3"):
    # 创建一个填充前景色的图像
    image = Image.new("RGB", (size, size), rgb_fg)
    draw = ImageDraw.Draw(image)

    # 计算网格线的宽度
    stripe_width = round(size / (n * grid_line_factor), 1)
    square_width = round((size - stripe_width * n) / n, 1)

    # 画垂直网格线
    for i in range(n + 1):
        left = i * size / n - stripe_width / 2
        right = i * size / n + stripe_width / 2
        draw.rectangle([left, 0, right, size], fill=rgb_bg)

    # 画水平网格线
    for i in range(n + 1):
        top = i * size / n - stripe_width / 2
        bottom = i * size / n + stripe_width / 2
        draw.rectangle([0, top, size, bottom], fill=rgb_bg)

    # 保存图像
    filename = (
        f"{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    )
    output_dir = os.path.join(
        output_dir,
        "{}_{}_{}_{}_{}".format(size, n, grid_line_factor, square_width, stripe_width),
    )
    os.makedirs(output_dir, exist_ok=True)
    image.save(os.path.join(output_dir, filename))
    print(f"Image saved as {filename}")


# size = 720  # 指的是720x720的图像
# n = 16  # 指的是长或宽为16个小正方形
# grid_line_factor = 2  # 指的是网格线的宽度影响因子，值越大，网格线越细[1.8~4]

for i in range(40):
    rgb_fg, rgb_bg = fgbgcolor(r=40, min_distance=60)
    # rgb_fg = (255, 0, 150)
    # rgb_bg = (255, 255, 0)
    plot_pillow(rgb_fg, rgb_bg, 640, 16, 2.8)

