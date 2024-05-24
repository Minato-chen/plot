from PIL import Image, ImageDraw
import random
import os
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color

output = "./output_pillow_3_new"
os.makedirs(output, exist_ok=True)


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


def opposite_color(a, b, r):
    while True:
        x = random.randint(-128, 127)
        y = random.randint(-128, 127)
        if (x + a) ** 2 + (y + b) ** 2 <= r**2:
            return x, y


# 生成前景色和背景色，确保两者不同且在A轴或B轴上相反
def fgbgcolor(r):
    # 生成前景色
    rgb_fg = randomcolor()
    lab_fg = rgb_to_lab(rgb_fg)  # （L，a，b）

    # 生成背景色
    opposite_ab = opposite_color(lab_fg[1], lab_fg[2], r)
    lab_bg = LabColor(lab_fg[0], opposite_ab[0], opposite_ab[1])
    rgb_bg = lab_to_rgb(lab_bg)

    # 确保生成的颜色在RGB范围内有效
    while any(c < 0 or c > 255 for c in rgb_bg):
        fgbgcolor(r)

    return rgb_fg, rgb_bg


# 绘制图案函数
def plot_pillow(rgb_fg, rgb_bg, size, n, grid_line_factor=8, output_dir=output):
    # 创建一个填充前景色的图像
    image = Image.new("RGB", (size, size), rgb_fg)
    draw = ImageDraw.Draw(image)

    # 计算网格线的宽度
    stripe_width = size // (n * grid_line_factor)

    # 画垂直网格线
    for i in range(n + 1):
        left = i * size // n - stripe_width // 2
        right = i * size // n + stripe_width // 2
        draw.rectangle([left, 0, right, size], fill=rgb_bg)

    # 画水平网格线
    for i in range(n + 1):
        top = i * size // n - stripe_width // 2
        bottom = i * size // n + stripe_width // 2
        draw.rectangle([0, top, size, bottom], fill=rgb_bg)

    # 保存图像
    filename = (
        f"{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    )
    os.makedirs(output_dir, exist_ok=True)
    image.save(os.path.join(output_dir, filename))
    print(f"image saved as {filename}")


# 生成720x720的图像
for i in range(2):
    rgb_fg, rgb_bg = fgbgcolor(r=5)
    plot_pillow(rgb_fg, rgb_bg, 720, 16, 2)
# size = 720指的是720x720的图像
# n = 16指的是长或宽为16个小正方形
# grid_line_factor = 4指的是网格线的宽度影响因子，值越大，网格线越细
# 2和16是比较好的一种组合(网格线越细效果越弱)
