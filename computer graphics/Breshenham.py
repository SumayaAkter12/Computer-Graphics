import matplotlib.pyplot as plt

def bresenham_line(x1, y1, x2, y2):
    # Store all the pixels to draw
    points = []

    # Swap points if drawing from right to left
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = abs(y2 - y1)
    p = 2 * dy - dx

    x, y = x1, y1
    y_step = 1 if y1 < y2 else -1

    while x <= x2:
        points.append((x, y))
        if p >= 0:
            y += y_step
            p += 2 * (dy - dx)
        else:
            p += 2 * dy
        x += 1

    return points

# Example usage
x1, y1 = 100, 100
x2, y2 = 400, 370

line_points = bresenham_line(x1, y1, x2, y2)

# Split x and y for plotting
x_vals, y_vals = zip(*line_points)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, 'ko')  # 'ko' means black circle (pixel)
plt.title("Bresenham's Line Drawing")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis('equal')
plt.show()
