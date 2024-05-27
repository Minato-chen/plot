size = 640
n = [16, 24, 32]
grid_line_factor = [1.8, 2.2, 2.8, 4]


for i in range(len(n)):
    for j in range(len(grid_line_factor)):
        print(n[i], grid_line_factor[j])

        stripe_width = round(size / (n[i] * grid_line_factor[j]), 1)
        square_width = round((size - stripe_width * n[i]) / n[i], 1)
        print(stripe_width, square_width)

# stripe_width = round(size / (n * grid_line_factor), 1)
# square_width = round((size - stripe_width * n) / n, 1)
