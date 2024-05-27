from PIL import Image, ImageDraw
import random
import os

def randomcolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def color_distance(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5


def fgbgcolor(min_distance=200):
    rgb_fg = randomcolor()
    rgb_bg = randomcolor()
    while color_distance(rgb_fg, rgb_bg) < min_distance:
        rgb_fg = randomcolor()
    return rgb_fg, rgb_bg


def plot_pillow(rgb_fg, rgb_bg, size, n, output_dir="./output_type_2"):
    image = Image.new("RGB", (size, size), rgb_bg)
    draw = ImageDraw.Draw(image)

    for i in range(n):
        color = rgb_fg if i % 2 == 0 else rgb_bg
        draw.rectangle(
            [
                i * size // n,  # Left
                0,  # Top
                (i + 1) * size // n,  # Right
                size,  # Bottom
            ],
            fill=color,
        )

    filename = (
        f"{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    )
    output_dir = os.path.join(
    output_dir,
    "{}_{}".format(size, n),
    )
    os.makedirs(output_dir, exist_ok=True)
    image.save(os.path.join(output_dir, filename))
    print(f"Saved image as {filename}")


# Generate 720x720 images
for i in range(10):
    rgb_fg, rgb_bg = fgbgcolor()
    plot_pillow(rgb_fg, rgb_bg, 720, 20)
