

'''
Enter number of vertices: 4
Enter coordinates (x y):
100 100
100 200
200 200
200 100
Enter rotation angle (degrees): 45
Enter pivot point (xp yp): 200 200
'''








import matplotlib.pyplot as plt
import math

# Draw polygon
def draw_polygon(x, y, color='black', label=''):
    x_closed = x + [x[0]]
    y_closed = y + [y[0]]
    plt.plot(x_closed, y_closed, color=color, label=label, linewidth=2)

# Rotate polygon
def rotate_polygon(x, y, angle_deg, xp, yp):
    angle_rad = math.radians(angle_deg)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    x_rotated = []
    y_rotated = []
    for xi, yi in zip(x, y):
        x_shift = xi - xp
        y_shift = yi - yp
        xr = xp + x_shift * cos_a - y_shift * sin_a
        yr = yp + x_shift * sin_a + y_shift * cos_a
        x_rotated.append(xr)
        y_rotated.append(yr)
    return x_rotated, y_rotated

# Input
n = int(input("Enter number of vertices: "))
x = []
y = []
print("Enter coordinates (x y):")
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

angle = float(input("Enter rotation angle (degrees): "))
xp, yp = map(float, input("Enter pivot point (xp yp): ").split())

x_rot, y_rot = rotate_polygon(x, y, angle, xp, yp)

plt.figure(figsize=(8, 6))
draw_polygon(x, y, color='blue', label='Original')
draw_polygon(x_rot, y_rot, color='orange', label='Rotated')

plt.title("2D Polygon Rotation")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
