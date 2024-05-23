from PIL import Image, ImageDraw
import random
import os

output = "./output_pillow_3"
os.makedirs(output, exist_ok=True)


def randomcolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def fgbgcolor():
    rgb_fg = randomcolor()
    rgb_bg = randomcolor()
    while rgb_bg == rgb_fg:
        rgb_bg = randomcolor()
    return rgb_fg, rgb_bg


def plot_pillow(rgb_fg, rgb_bg, size, n, output_dir="./output_pillow_3"):
    image = Image.new("RGB", (size, size), rgb_fg)
    draw = ImageDraw.Draw(image)

    stripe_width = size / (
        n * 4
    )  # 比较好的效果是1.5~6之间，这里数字越大n应该要越小效果比较好，如4和16
    # Adjust the divisor to control the width of the grid lines
    for i in range(n + 1):
        draw.rectangle(
            [
                i * size // n - stripe_width // 2,  # Left
                0,  # Top
                i * size // n + stripe_width // 2,  # Right
                size,  # Bottom
            ],
            fill=rgb_bg,
        )
        draw.rectangle(
            [
                0,  # Left
                i * size // n - stripe_width // 2,  # Top
                size,  # Right
                i * size // n + stripe_width // 2,  # Bottom
            ],
            fill=rgb_bg,
        )

    filename = (
        f"{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    )
    os.makedirs(output_dir, exist_ok=True)
    image.save(os.path.join(output_dir, filename))
    print(f"Saved image as {filename}")


# Generate 720x720 images
for i in range(1):
    # rgb_fg, rgb_bg = fgbgcolor()
    rgb_fg = (0, 255, 0)
    rgb_bg = (0, 0, 255)
    plot_pillow(rgb_fg, rgb_bg, 720, 16)  # Adjust n to change the number of squares
