import matplotlib.pyplot as plt

def draw_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    points = []

    def plot_circle_points(x, y):
        # 8-way symmetry
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x),
        ])

    plot_circle_points(x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle_points(x, y)

    return points

# Example usage
xc, yc = 4, 4 # Center of the circle
r = 10         # Radius of the circle

circle_points = draw_circle(xc, yc, r)

# Plotting the result
x_vals, y_vals = zip(*circle_points)
plt.figure(figsize=(6, 6))
plt.scatter(x_vals, y_vals, color='blue', s=10)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Midpoint Circle Drawing Algorithm')
plt.grid(True)
plt.show()
