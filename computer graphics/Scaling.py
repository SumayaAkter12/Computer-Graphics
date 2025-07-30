
'''
Enter number of vertices: 4
Enter coordinates (x y):
100 100
100 150
150 150
150 100
Enter scaling factors (sfx sfy): 2 2
'''





import matplotlib.pyplot as plt

# Function to draw a polygon
def draw_polygon(x, y, color='black', label=''):
    x_closed = x + [x[0]]
    y_closed = y + [y[0]]
    plt.plot(x_closed, y_closed, color=color, label=label, linewidth=2)

# Function to apply scaling
def scale_polygon(x, y, sfx, sfy):
    x_scaled = [xi * sfx for xi in x]
    y_scaled = [yi * sfy for yi in y]
    return x_scaled, y_scaled

# Input
n = int(input("Enter number of vertices: "))
x = []
y = []
print("Enter coordinates (x y):")
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

sfx, sfy = map(float, input("Enter scaling factors (sfx sfy): ").split())

# Apply scaling
x_scaled, y_scaled = scale_polygon(x, y, sfx, sfy)

# Plotting
plt.figure(figsize=(8, 6))
draw_polygon(x, y, color='blue', label='Original Polygon')
draw_polygon(x_scaled, y_scaled, color='orange', label='Scaled Polygon')

plt.title("2D Polygon Scaling")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
