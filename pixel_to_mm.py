def pixels_to_mm(pixels, dpi):
    inches = pixels / dpi
    mm = inches * 25.4
    return mm


# 720x720 pixels at different DPIs
dpi_values = [
    72,
    96,
    300,
    141,
    176,
]  # 在不同的 DPI（每英寸像素数）下计算图像的物理尺寸。
# DPI计算https://dpi.lv/
pixels = 720
# 1920x1080像素的分辨率，15.6英寸的显示器，DPI=141

for dpi in dpi_values:
    size_mm = pixels_to_mm(pixels, dpi)
    print(f"At {dpi} DPI: {size_mm:.2f} mm × {size_mm:.2f} mm")

# 720对应129.70mm
# 32个小方块对应129.70/32=4.05mm
# 48个小方块对应129.70/48=2.70mm
# 64个小方块对应129.70/64=2.03mm
