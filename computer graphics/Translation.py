
'''
Enter number of vertices: 4
Enter coordinates (x y):
100 100
100 200
200 200
200 100
Enter translation (tx ty): 150 150
'''


import matplotlib.pyplot as plt

# Function to draw a polygon
def draw_polygon(x, y, color='black', label=''):
    x_closed = x + [x[0]]
    y_closed = y + [y[0]]
    plt.plot(x_closed, y_closed, color=color, label=label, linewidth=2)

# Function to translate the polygon
def translate_polygon(x, y, tx, ty):
    x_translated = [xi + tx for xi in x]
    y_translated = [yi + ty for yi in y]
    return x_translated, y_translated

# Input
n = int(input("Enter number of vertices: "))
x = []
y = []
print("Enter coordinates (x y):")
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

tx, ty = map(int, input("Enter translation (tx ty): ").split())

# Translate polygon
x_translated, y_translated = translate_polygon(x, y, tx, ty)

# Plotting
plt.figure(figsize=(8, 6))
draw_polygon(x, y, color='blue', label='Original Polygon')
draw_polygon(x_translated, y_translated, color='orange', label='Translated Polygon')

plt.title("2D Polygon Translation")
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
