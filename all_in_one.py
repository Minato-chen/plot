from plot_type import plot_type1, plot_type2, plot_type3
from color_generate import CG_dist, CG_opp

size = 640
# type1, type2
# n = [16, 24, 32, 64]
n = 16

# type3
# m = [16, 24, 32]
# grid_line_factor = [1.8, 2.2, 2.8, 4]
m = 24
g = 2.2

# 基于距离的颜色选择策略
for i in range(100):
    rgb_fg, rgb_bg = CG_dist.fgbgcolor()
    # rgb_fg, rgb_bg = (0, 255, 0), (0, 0, 255)
    plot_type1(rgb_fg, rgb_bg, size, n, output_dir="./output_type_1")
    plot_type2(rgb_fg, rgb_bg, size, n, output_dir="./output_type_2")
    plot_type3(rgb_fg, rgb_bg, size, m, g, output_dir="./output_type_3")

    # plot_type1(rgb_bg, rgb_fg, size, 32, output_dir="./output_type_1_converse")
    # plot_type2(rgb_bg, rgb_fg, size, 32, output_dir="./output_type_2_converse")
    # plot_type3(rgb_bg, rgb_fg, size, 16, 2, output_dir="./output_type_3_converse")

# 基于lab反向的颜色选择策略
for i in range(100):
    rgb_fg_opp, rgb_bg_opp = CG_opp.fgbgcolor()
    # rgb_fg, rgb_bg = (0, 255, 0), (0, 0, 255)
    plot_type1(rgb_fg_opp, rgb_bg_opp, size, n, output_dir="./output_type_1_opp")
    plot_type2(rgb_fg_opp, rgb_bg_opp, size, n, output_dir="./output_type_2_opp")
    plot_type3(rgb_fg_opp, rgb_bg_opp, size, m, g, output_dir="./output_type_3_opp")

    # plot_type1(rgb_bg_opp, rgb_fg_opp, 640, 32, output_dir="./output_type_1_opp_converse")
    # plot_type2(rgb_bg_opp, rgb_fg_opp, 640, 32, output_dir="./output_type_2_opp_converse")
    # plot_type3(rgb_bg_opp, rgb_fg_opp, 640, 16, 2, output_dir="./output_type_3_opp_converse")
