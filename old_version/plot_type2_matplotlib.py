import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import random

output = "./output2"
os.makedirs(output, exist_ok=True)


def draw_alternating_squares(size, rgb_fg, rgb_bg):
    # 创建一个画布
    plt.figure(figsize=(64, 64))

    # 初始颜色
    color = rgb_fg

    # 逐步缩小正方形并画出
    while size >= 2:
        # 计算正方形左下角的坐标
        left_bottom_x = (64 - size) / 2
        left_bottom_y = (64 - size) / 2

        # 归一化颜色值
        normalized_color = (color[0] / 255, color[1] / 255, color[2] / 255)

        # 创建正方形
        square = patches.Rectangle(
            (left_bottom_x, left_bottom_y),
            size,
            size,
            edgecolor="none",
            facecolor=normalized_color,
        )

        # 添加到画布
        plt.gca().add_patch(square)

        # 切换颜色
        color = rgb_bg if color == rgb_fg else rgb_fg

        # 缩小正方形大小
        size -= 1

    # 设置坐标轴范围
    plt.xlim(0, 64)
    plt.ylim(0, 64)
    plt.axis("off")

    filename = (
        f"{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    )
    plt.savefig(
        os.path.join("./output2", filename),
        dpi=300,
        bbox_inches="tight",
        pad_inches=-0.1,
    )

    print(f"Saved image as {filename}")


def randomcolor():
    # 生成随机的 RGB 值
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # 返回包含 RGB 值的列表
    return [r, g, b]


def fgbgcolor():
    # 前景色：被影响
    rgb_fg = randomcolor()
    rgb_bg = randomcolor()

    while rgb_bg == rgb_fg:
        rgb_bg = randomcolor()

    return rgb_fg, rgb_bg


for i in range(0, 5):
    rgb_fg, rgb_bg = fgbgcolor()
    draw_alternating_squares(64, rgb_fg, rgb_bg)

# 影响色
# rgb_fg = (252, 152, 15)
# 中间色（被影响）
# rgb_bg = (177, 80, 255)
