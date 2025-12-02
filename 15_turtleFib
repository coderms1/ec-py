# Import Necessary Library
import turtle

# Screen Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

# Turtle Setup
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Loop Drawing
for i in range(0, 360, 4):
    t.pencolor(colors[i % len(colors)])
    t.width(i / 150 + 1)
    t.forward(i * 1.5)
    t.left(61)
    turtle.update()

# Keep Window Open Until User Clicks
screen.mainloop()
