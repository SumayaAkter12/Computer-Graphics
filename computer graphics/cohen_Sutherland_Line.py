import matplotlib.pyplot as plt

# Clipping window boundaries
x_left, x_right = 120, 500
y_bottom, y_top = 100, 350

# Region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Function to compute region code
def compute_code(x, y):
    code = INSIDE
    if x < x_left:
        code |= LEFT
    elif x > x_right:
        code |= RIGHT
    if y < y_bottom:
        code |= BOTTOM
    elif y > y_top:
        code |= TOP
    return code

# Cohen-Sutherland clipping algorithm
def cohen_sutherland_clip(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            x, y = 0.0, 0.0
            code_out = code1 if code1 != 0 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_top - y1) / (y2 - y1)
                y = y_top
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_bottom - y1) / (y2 - y1)
                y = y_bottom
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_right - x1) / (x2 - x1)
                x = x_right
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_left - x1) / (x2 - x1)
                x = x_left

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        return (x1, y1, x2, y2)
    else:
        return None

# Define original line
x1, y1 = 50, 200
x2, y2 = 500, 400

# Clip the line
clipped_line = cohen_sutherland_clip(x1, y1, x2, y2)

# Draw using matplotlib
fig, ax = plt.subplots()
# Draw clipping window
ax.plot([x_left, x_right, x_right, x_left, x_left],
        [y_bottom, y_bottom, y_top, y_top, y_bottom], 'y-', label='Clipping Window')

# Draw original line in red
ax.plot([x1, x2], [y1, y2], 'r--', label='Original Line')

# Draw clipped line in white (black for visibility)
if clipped_line:
    cx1, cy1, cx2, cy2 = clipped_line
    ax.plot([cx1, cx2], [cy1, cy2], 'k-', linewidth=2, label='Clipped Line')

ax.set_aspect('equal')
ax.grid(True)
ax.legend()
plt.title("Cohen-Sutherland Line Clipping")
plt.show()
