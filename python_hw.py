# -*- coding: utf-8 -*-
"""python_HW.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iyqabe6oIK8xi_A05XfVFrYQVROznBFi

# Code
"""

import matplotlib.pyplot as plt
import numpy as np

def visualize_trapped_water(height):
    n = len(height)

    # Compute trapped water
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = height[0]
    right_max[n - 1] = height[n - 1]

    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    water_levels = [max(0, min(left_max[i], right_max[i]) - height[i]) for i in range(n)]
    water_trapped = np.sum(water_levels)

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.suptitle("Trapping Water", fontsize=14, fontweight='bold', ha='center', y=1.03)
    ax.set_xlabel("Position")
    ax.set_ylabel("Height")

    # Add height and trapped water text centered
    plt.figtext(0.5, 0.96, f"Height = {height}", ha="center", fontsize=10)
    plt.figtext(0.5, 0.92, f"Trapped Water = {water_trapped}", ha="center", fontsize=10)

    x = np.arange(n)

    # Plot terrain & trapped water
    ax.bar(x, height, color='black', label='Terrain', width=1.0)
    ax.bar(x, water_levels, bottom=height, color='blue', label='Trapped Water', width=1.0)
    ax.legend()

    # Adjust limits to add margin above highest bar
    ax.set_ylim(0, max(height) + 3)

    plt.show()

"""# Test Cases"""

# Test cases
test_cases = [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],  # Expected water trapped: 6
    [4, 2, 0, 3, 2, 5, 1, 0, 2, 3, 1, 4],  # Expected water trapped: 22
    [3, 0, 0, 2, 0, 4, 1, 0, 3, 2, 5, 2]  # Expected water trapped: 20
]

visualize_trapped_water(test_cases[0])

visualize_trapped_water(test_cases[1])

visualize_trapped_water(test_cases[2])

print("\nEnd of file\n")

"""---
---
"""