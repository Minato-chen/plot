import matplotlib.pyplot as plt
import random
import os

output = "./output1"
os.makedirs(output, exist_ok=True)


def plot(rgb, rgb_fg, rgb_bg, figsize, dpi, output_dir="./output1"):
    plt.figure(figsize=figsize, dpi=dpi)

    for i in range(0, 64, 1):
        for j in range(0, 64, 1):
            color = rgb[(i + j) % len(rgb)]
            plt.fill([i, i + 1, i + 1, i], [j, j, j + 1, j + 1], color=color)

    plt.xlim(0, 64)
    plt.ylim(0, 64)
    plt.axis("off")

    filename = (
        f"{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    )
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(
        os.path.join(output_dir, filename), dpi=dpi, bbox_inches="tight", pad_inches=0
    )

    print(f"Saved image as {filename}")
    plt.close()


def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return [r, g, b]


def fgbgcolor():
    rgb_fg = randomcolor()
    rgb_bg = randomcolor()

    while rgb_bg == rgb_fg:
        rgb_bg = randomcolor()

    rgb_fg_nor = [rgb_fg[0] / 255.0, rgb_fg[1] / 255.0, rgb_fg[2] / 255.0]
    rgb_bg_nor = [rgb_bg[0] / 255.0, rgb_bg[1] / 255.0, rgb_bg[2] / 255.0]

    return rgb_fg, rgb_bg, rgb_fg_nor, rgb_bg_nor


# Generate 720x720 images
for i in range(2):
    rgb_fg, rgb_bg, rgb_fg_nor, rgb_bg_nor = fgbgcolor()
    rgb = [rgb_fg_nor, rgb_bg_nor]
    plot(rgb, rgb_fg, rgb_bg, figsize=(4.8, 4.8), dpi=150)

# Generate 640x640 images
# for i in range(2):
#     rgb_fg, rgb_bg, rgb_fg_nor, rgb_bg_nor = fgbgcolor()
#     rgb = [rgb_fg_nor, rgb_bg_nor]
#     plot(rgb, rgb_fg, rgb_bg, figsize=(4.2667, 4.2667), dpi=150)
