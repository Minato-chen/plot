from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
from lab_to_rgb import lab_to_rgb
from rgb_to_lab import rgb_to_lab
from rgb_to_xyz import rgb_to_xyz

# D65, 2/10°观察
# LAB -> RGB -> LAB
original_lab = LabColor(50, 10, 10)
print("Original LAB:", original_lab)
rgb = lab_to_rgb(original_lab)
print("Converted RGB:", rgb)
converted_lab = rgb_to_lab(rgb)
print("Re-converted LAB:", converted_lab)

# rgb-> xyz(差了100倍)-> xyz_normalized(准确)
xyz = rgb_to_xyz(rgb)
print("Converted xyz:", tuple(round(x, 3) for x in xyz))  # 保留三位小数
sum = xyz[0] + xyz[1] + xyz[2]
xyz_normalized = (
    round(xyz[0] / sum, 3),
    round(xyz[1] / sum, 3),
    round(xyz[2] / sum, 3),
)  # 保留三位小数
print("Converted xyz_normalized:", xyz_normalized)
