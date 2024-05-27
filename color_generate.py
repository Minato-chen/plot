import random
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color


# 基于lab反向的颜色选择策略
class CG_opp:
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
            rgb_fg = CG_opp.randomcolor()
            lab_fg = CG_opp.rgb_to_lab(rgb_fg)  # （L，a，b）

            # 生成背景色
            opposite_lab = CG_opp.opposite_color(lab_fg[0], lab_fg[1], lab_fg[2], r)
            lab_bg = LabColor(opposite_lab[0], opposite_lab[1], opposite_lab[2])
            rgb_bg = CG_opp.lab_to_rgb(lab_bg)

            # 确保生成的颜色在RGB范围内有效
            if (
                all(0 <= c <= 255 for c in rgb_bg)
                and min_distance < CG_opp.color_distance(rgb_fg, rgb_bg) < 235
                and opposite_lab[0] > lab_fg[0]
            ):
                break

        return rgb_fg, rgb_bg


# 基于距离的颜色选择策略
class CG_dist:
    @staticmethod
    def randomcolor():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    @staticmethod
    def color_distance(c1, c2):
        return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5

    @staticmethod
    def calculate_luminance(r, g, b):
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    @staticmethod
    def fgbgcolor(min_distance=200):
        rgb_fg = CG_dist.randomcolor()
        rgb_bg = CG_dist.randomcolor()
        while CG_dist.color_distance(
            rgb_fg, rgb_bg
        ) < min_distance and CG_dist.calculate_luminance(
            rgb_fg[0], rgb_fg[1], rgb_fg[2]
        ) > CG_dist.calculate_luminance(
            rgb_bg[0], rgb_bg[1], rgb_bg[2]
        ):
            rgb_fg = CG_dist.randomcolor()
        return rgb_fg, rgb_bg
