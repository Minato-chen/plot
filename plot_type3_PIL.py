from PIL import Image, ImageDraw
import random
import os

output = "./output_pillow_3"
os.makedirs(output, exist_ok=True)


# 随机生成颜色
def randomcolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# 生成前景色和背景色，确保两者不同
def fgbgcolor():
    rgb_fg = randomcolor()
    rgb_bg = randomcolor()
    while rgb_bg == rgb_fg:
        rgb_bg = randomcolor()
    return rgb_fg, rgb_bg


# 绘制图案函数
def plot_pillow(
    rgb_fg, rgb_bg, size, n, grid_line_factor=8, output_dir="./output_pillow_3"
):
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
    rgb_fg, rgb_bg = fgbgcolor()
    plot_pillow(rgb_fg, rgb_bg, 720, 20, 4)
# size = 720指的是720x720的图像
# n = 16指的是长或宽为16个小正方形
# grid_line_factor = 4指的是网格线的宽度影响因子，值越大，网格线越细
# 4和16或20左右是比较好的一种组合
