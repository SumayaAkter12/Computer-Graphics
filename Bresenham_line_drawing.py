"""
Bresenham's Line Drawing Algorithm:
-----------------------------------
This algorithm draws a straight line between two given points (x0, y0) and (x1, y1)
on a pixel grid using only integer calculations.

Steps:
1. Calculate the differences: dx = |x1 - x0|, dy = |y1 - y0|
2. Determine the direction of step for x (sx) and y (sy)
   - sx = 1 if x0 < x1 else -1
   - sy = 1 if y0 < y1 else -1
3. Initialize error term: err = dx - dy
4. Loop until the current point (x0, y0) reaches (x1, y1):
   a. Plot (x0, y0)
   b. Calculate e2 = 2 * err
   c. If e2 > -dy, then:
      - err -= dy
      - x0 += sx
   d. If e2 < dx, then:
      - err += dx
      - y0 += sy

This handles all 8 octants without needing special cases.
"""

import matplotlib.pyplot as plt

def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return points

# Draw a line from (2, 2) to (10, 6)
x0, y0 = 2, 2
x1, y1 = 10, 6
line_points = bresenham_line(x0, y0, x1, y1)

# Plot the result
x_vals = [p[0] for p in line_points]
y_vals = [p[1] for p in line_points]

plt.plot(x_vals, y_vals, marker='o', color='blue')
plt.title("Bresenham's Line Drawing")
plt.grid(True)
plt.gca().set_aspect('equal')
plt.show()
