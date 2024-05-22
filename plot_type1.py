import matplotlib.pyplot as plt
import random
import os


def plot(rgb):
    plt.figure(figsize=(64, 64))

    #plt.fill([0, 64, 64, 0], [0, 0, 64, 64], color=(0.3, 0.3, 0.3))

    for i in range(0, 64, 1):
        for j in range(0, 64, 1):
            color = rgb[(i + j) % len(rgb)]
            plt.fill([i, i + 1, i + 1, i], [j, j, j + 1, j + 1], color=color)

    plt.xlim(0, 64)
    plt.ylim(0, 64)
    plt.axis("off")

    filename = f"{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    plt.savefig(os.path.join("./output", filename), dpi=300, bbox_inches="tight",pad_inches = -0.1)

    print(f"Saved image as {filename}")
    # plt.show()

def randomcolor():
     # 生成随机的 RGB 值
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    # 返回包含 RGB 值的列表
    return [r, g, b]

def fgbgcolor():
    #前景色：被影响
    rgb_fg=randomcolor()
    rgb_bg = randomcolor()

    while rgb_bg==rgb_fg:
        rgb_bg = randomcolor()

    rgb_fg_nor = [rgb_fg[0] / 255.0, rgb_fg[1] / 255.0, rgb_fg[2] / 255.0]
    rgb_bg_nor = [rgb_bg[0] / 255.0, rgb_bg[1] / 255.0, rgb_bg[2] / 255.0]

    return rgb_fg,rgb_bg,rgb_fg_nor,rgb_bg_nor


for i in range(0,2):
    rgb_fg,rgb_bg,rgb_fg_nor,rgb_bg_nor=fgbgcolor()
    rgb = [rgb_fg_nor, rgb_bg_nor]
    plot(rgb)
