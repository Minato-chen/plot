from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color


# 本函数字典输入，元组输出
def lab_to_rgb(lab):
    rgb = convert_color(lab, sRGBColor)
    rgb_values = (
        round(min(max(rgb.rgb_r, 0.0), 1.0) * 255),
        round(min(max(rgb.rgb_g, 0.0), 1.0) * 255),
        round(min(max(rgb.rgb_b, 0.0), 1.0) * 255),
    )
    return rgb_values


lab = LabColor(50, 101, 0)  # 元组转化成字典

rgb = lab_to_rgb(lab)
print("LAB:", lab, "-> RGB:", rgb)
