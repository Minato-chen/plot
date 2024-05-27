size = 640
n = [16, 24, 32]
square_width = [10, 14, 18, 22, 26]

# stripe_width = (size - square_width * n) / n
# grid_line_factor = size / (n * stripe_width)

for i in range(len(n)):
    for j in range(len(square_width)):
        stripe_width = (size - square_width[j] * n[i]) / n[i]
        grid_line_factor = size / (n[i] * stripe_width)
        print(
            f"n: {n[i]}, square_width: {square_width[j]}, stripe_width: {stripe_width}, grid_line_factor: {grid_line_factor}"
        )
