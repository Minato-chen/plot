from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color


# 元组LabColor函数转化为字典,字典入,元组出
def lab_to_rgb(lab):
    rgb = convert_color(lab, sRGBColor)
    # Clamp the values to be between 0 and 1 before converting to 0-255 range
    rgb_values = (
        round(min(max(rgb.rgb_r, 0.0), 1.0) * 255),
        round(min(max(rgb.rgb_g, 0.0), 1.0) * 255),
        round(min(max(rgb.rgb_b, 0.0), 1.0) * 255),
    )
    return rgb_values


# lab = LabColor(53, 80, 67)  # 预期: (254, 1, 0)
# rgb = lab_to_rgb(lab)
# print("LAB:", lab, "-> RGB:", rgb)
# 期望输出: RGB: (250, 0, 7)
