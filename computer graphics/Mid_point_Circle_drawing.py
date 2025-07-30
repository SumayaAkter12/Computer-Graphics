import matplotlib.pyplot as plt

def midpoint_circle(xc, yc, radius):
    x = 0
    y = radius
    p = 1 - radius

    points = []

    while x <= y:
        # Storing all 8 symmetrical points
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ])

        x += 1
        if p >= 0:
            y -= 1
            p += 2 * (x - y) + 1
        else:
            p += 2 * x + 1

    return points

# Input
xc, yc = 200, 200
radius = 150

# Generate circle points
circle_points = midpoint_circle(xc, yc, radius)
x_vals, y_vals = zip(*circle_points)

# Plot
plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, 'ko')  # black points
plt.title("Midpoint Circle Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.show()
