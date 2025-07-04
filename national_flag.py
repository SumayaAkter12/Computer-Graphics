import turtle

# Setup turtle
flag = turtle.Turtle()
flag.speed(2)
turtle.bgcolor("white")

# Flag dimensions (approx ratio 10:6)
flag_width = 300
flag_height = 180
circle_radius = 60

# Draw green rectangle (flag background)
flag.penup()
flag.goto(-flag_width // 2, flag_height // 2)
flag.pendown()
flag.color("green")
flag.begin_fill()
for _ in range(2):
    flag.forward(flag_width)
    flag.right(90)
    flag.forward(flag_height)
    flag.right(90)
flag.end_fill()

# Draw red circle (perfectly centered)
flag.penup()
flag.goto(0, -circle_radius)  # Circle center at (0,0)
flag.setheading(0)
flag.pendown()
flag.color("red")
flag.begin_fill()
flag.circle(circle_radius)
flag.end_fill()

# Finish
flag.hideturtle()
turtle.done()
