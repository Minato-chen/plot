from PIL import Image, ImageDraw
import os


def plot_type1(rgb_fg, rgb_bg, size, n, output_dir="./output_type_1"):
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
    width = round(size / n, 1)
    filename = (
        f"{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    )
    output_dir = os.path.join(output_dir, "{}_{}_{}".format(size, n, width))
    os.makedirs(output_dir, exist_ok=True)
    image.save(os.path.join(output_dir, filename))
    print(f"Saved image as {filename}")


def plot_type2(rgb_fg, rgb_bg, size, n, output_dir="./output_type_2"):
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
    width = round(size / n, 1)
    filename = (
        f"{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    )
    output_dir = os.path.join(
        output_dir,
        "{}_{}_{}".format(size, n, width),
    )
    os.makedirs(output_dir, exist_ok=True)
    image.save(os.path.join(output_dir, filename))
    print(f"Saved image as {filename}")


def plot_type3(
    rgb_fg, rgb_bg, size, n, grid_line_factor=8, output_dir="./output_type_3"
):
    # 创建一个填充前景色的图像
    image = Image.new("RGB", (size, size), rgb_fg)
    draw = ImageDraw.Draw(image)

    # 计算网格线的宽度
    stripe_width = round(size / (n * grid_line_factor), 1)
    square_width = round((size - stripe_width * n) / n, 1)

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
    output_dir = os.path.join(
        output_dir,
        "{}_{}_{}_{}_{}".format(size, n, grid_line_factor, square_width, stripe_width),
    )
    os.makedirs(output_dir, exist_ok=True)
    image.save(os.path.join(output_dir, filename))
    print(f"image saved as {filename}")
