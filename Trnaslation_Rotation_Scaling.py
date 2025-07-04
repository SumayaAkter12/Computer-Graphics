import matplotlib.pyplot as plt
import math

# Original triangle points
x = [0, 1, 0.5, 0]
y = [0, 0, 1, 0]

# Translation
def translate(x, y, tx, ty):
    return [xi + tx for xi in x], [yi + ty for yi in y]

# Rotation (around origin)
def rotate(x, y, angle_deg):
    angle_rad = math.radians(angle_deg)
    xr = [xi * math.cos(angle_rad) - yi * math.sin(angle_rad) for xi, yi in zip(x, y)]
    yr = [xi * math.sin(angle_rad) + yi * math.cos(angle_rad) for xi, yi in zip(x, y)]
    return xr, yr

# Scaling
def scale(x, y, sx, sy):
    return [xi * sx for xi in x], [yi * sy for yi in y]

# Apply transformations
x_trans, y_trans = translate(x, y, 2, 1)
x_rot, y_rot = rotate(x, y, 90)
x_scl, y_scl = scale(x, y, 2, 0.5)

# Plot all
plt.plot(x, y, label='Original', linewidth=2)
plt.plot(x_trans, y_trans, '--', label='Translated (2,1)')
plt.plot(x_rot, y_rot, '-.', label='Rotated 45°')
plt.plot(x_scl, y_scl, ':', label='Scaled (2x, 0.5y)')
plt.legend()
plt.title('Easy 2D Transformations')
plt.axis('equal')
plt.grid(True)
plt.show()
