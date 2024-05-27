import numpy as np


def rgb_to_xyz(rgb):
    """
    Convert an RGB color to XYZ color space.

    Parameters:
    rgb (list or tuple): A list or tuple with three elements representing the RGB values,
                         where each value is in the range [0, 255].

    Returns:
    tuple: A tuple with three elements representing the XYZ values.
    """

    # Normalize the RGB values to the range [0, 1]
    rgb = [x / 255.0 for x in rgb]

    # Apply the inverse gamma correction (sRGB)
    def inv_gamma_correction(c):
        return (c / 12.92) if (c <= 0.04045) else (((c + 0.055) / 1.055) ** 2.4)

    rgb = [inv_gamma_correction(c) for c in rgb]

    # Convert the normalized RGB values to linear RGB
    rgb = np.array(rgb)

    # sRGB to XYZ conversion matrix
    M = np.array(
        [
            [0.4124564, 0.3575761, 0.1804375],
            [0.2126729, 0.7151522, 0.0721750],
            [0.0193339, 0.1191920, 0.9503041],
        ]
    )

    # Perform the matrix multiplication
    xyz = np.dot(M, rgb)

    # Return the XYZ values
    return tuple(xyz)


# rgb_color = (255, 0, 0)  # Red color in RGB
# xyz_color = rgb_to_xyz(rgb_color)
# print(f"RGB: {rgb_color} -> XYZ: {xyz_color}")
# 期望输出: XYZ: (41, 21, 2)
