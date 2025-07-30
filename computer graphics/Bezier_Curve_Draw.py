import matplotlib.pyplot as plt
import numpy as np
import math

# Calculate factorial for binomial coefficient
def factorial(n):
    return math.factorial(n)

# Calculate binomial coefficient "n choose i"
def binomial_coeff(n, i):
    return factorial(n) // (factorial(i) * factorial(n - i))

# Bezier curve function
def bezier_curve(control_points, num_points=100):
    n = len(control_points) - 1
    t_vals = np.linspace(0, 1, num_points)
    curve_points = []

    for t in t_vals:
        x, y = 0, 0
        for i, (px, py) in enumerate(control_points):
            coeff = binomial_coeff(n, i) * (t ** i) * ((1 - t) ** (n - i))
            x += coeff * px
            y += coeff * py
        curve_points.append((x, y))
    return curve_points

# Input control points
n = int(input("Enter number of control points: "))
control_points = []
print("Enter control point coordinates (x y):")
for _ in range(n):
    x, y = map(float, input().split())
    control_points.append((x, y))

# Generate Bezier curve points
curve = bezier_curve(control_points)

# Separate x and y for plotting
control_x, control_y = zip(*control_points)
curve_x, curve_y = zip(*curve)

# Plot
plt.figure(figsize=(7, 6))
plt.plot(control_x, control_y, 'ro--', label='Control Polygon')
plt.plot(curve_x, curve_y, 'b-', linewidth=2, label='Bezier Curve')
plt.title("Bezier Curve")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
