import numpy as np

# 定义区间
x_min = 1.8
x_max = 4

# 定义均匀分割的数量
n = 4

# 计算 y 的范围
y_min = 1 / x_max
y_max = 1 / x_min

# 生成均匀分割的 y 值
y_values = np.linspace(y_min, y_max, n)

# 计算对应的 x 值
x_values = 1 / y_values

print("均匀分割的 y 值:", y_values)
print("对应的 x 值:", x_values)
