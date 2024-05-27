from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color


# 元组入,元组出
def rgb_to_lab(rgb):
    rgb_color = sRGBColor(
        rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0, is_upscaled=False
    )
    lab = convert_color(rgb_color, LabColor)
    lab_values = (round(lab.lab_l, 2), round(lab.lab_a, 2), round(lab.lab_b, 2))
    return lab_values


# rgb = (255, 0, 0)
# lab = rgb_to_lab(rgb)
# print("RGB:", rgb, "-> LAB :", lab)
# 期望输出: LAB: (53, 80, 67)
