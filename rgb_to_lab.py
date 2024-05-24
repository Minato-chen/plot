from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color


# 本函数元组输入，元组输出
def rgb_to_lab(rgb):
    rgb = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True)

    lab = convert_color(rgb, LabColor)

    lab_values = (round(lab.lab_l), round(lab.lab_a), round(lab.lab_b))

    return lab_values


rgb = (63, 191, 166)

lab = rgb_to_lab(rgb)
print("RGB:", rgb, "-> LAB :", lab)
