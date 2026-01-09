# ============================================
# AUTO DRAW DESIGN SYSTEM
# Single File Python Project
# Uses Turtle Graphics
# ============================================

import turtle
import math
import random

# ---------------- SCREEN SETUP ----------------
screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.bgcolor("white")
screen.title("Auto Draw Design System")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# ---------------- UTILITY FUNCTIONS ----------------

def reset_pen():
    pen.penup()
    pen.home()
    pen.pendown()

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    pen.color(r, g, b)

# ---------------- BASIC SHAPES ----------------

def draw_square(size):
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

def draw_rectangle(w, h):
    for _ in range(2):
        pen.forward(w)
        pen.right(90)
        pen.forward(h)
        pen.right(90)

def draw_triangle(size):
    for _ in range(3):
        pen.forward(size)
        pen.left(120)

def draw_circle(radius):
    pen.circle(radius)

# ---------------- COMPLEX SHAPES ----------------

def draw_star(size):
    for _ in range(5):
        pen.forward(size)
        pen.right(144)

def draw_polygon(sides, size):
    angle = 360 / sides
    for _ in range(sides):
        pen.forward(size)
        pen.right(angle)

def draw_spiral():
    length = 5
    for _ in range(60):
        pen.forward(length)
        pen.right(20)
        length += 3

def draw_flower():
    for _ in range(8):
        pen.circle(60)
        pen.right(45)

def draw_sun():
    draw_circle(60)
    for _ in range(12):
        pen.forward(80)
        pen.backward(80)
        pen.right(30)

def draw_heart():
    pen.left(50)
    pen.forward(100)
    pen.circle(40, 180)
    pen.right(100)
    pen.circle(40, 180)
    pen.forward(100)
    pen.setheading(0)

# ---------------- PATTERN DESIGNS ----------------

def draw_square_pattern():
    for _ in range(36):
        random_color()
        draw_square(120)
        pen.right(10)

def draw_circle_pattern():
    for _ in range(36):
        random_color()
        draw_circle(80)
        pen.right(10)

def draw_star_pattern():
    for _ in range(20):
        random_color()
        draw_star(150)
        pen.right(18)

def draw_spirograph():
    for _ in range(72):
        random_color()
        draw_circle(100)
        pen.right(5)

# ---------------- TEXT DRAWING ----------------

def draw_text():
    pen.penup()
    pen.goto(-200, 0)
    pen.pendown()
    pen.write("AUTO DRAW SYSTEM",
              font=("Arial", 28, "bold"))

# ---------------- MENU ----------------

def show_menu():
    print("\n===== AUTO DRAW MENU =====")
    print("square")
    print("rectangle")
    print("triangle")
    print("circle")
    print("star")
    print("polygon")
    print("flower")
    print("sun")
    print("heart")
    print("spiral")
    print("square_pattern")
    print("circle_pattern")
    print("star_pattern")
    print("spirograph")
    print("text")
    print("==========================")

# ---------------- MAIN PROGRAM ----------------

show_menu()

choice = screen.textinput(
    "Auto Draw",
    "Enter design name from menu:"
)

if choice:
    choice = choice.lower()
    reset_pen()
    random_color()

    if choice == "square":
        draw_square(150)

    elif choice == "rectangle":
        draw_rectangle(200, 100)

    elif choice == "triangle":
        draw_triangle(150)

    elif choice == "circle":
        draw_circle(100)

    elif choice == "star":
        draw_star(180)

    elif choice == "polygon":
        sides = int(screen.numinput("Polygon", "Enter number of sides:", 6))
        draw_polygon(sides, 100)

    elif choice == "flower":
        draw_flower()

    elif choice == "sun":
        draw_sun()

    elif choice == "heart":
        draw_heart()

    elif choice == "spiral":
        draw_spiral()

    elif choice == "square_pattern":
        draw_square_pattern()

    elif choice == "circle_pattern":
        draw_circle_pattern()

    elif choice == "star_pattern":
        draw_star_pattern()

    elif choice == "spirograph":
        draw_spirograph()

    elif choice == "text":
        draw_text()

    else:
        pen.write("Invalid Design!",
                  font=("Arial", 20, "bold"))

pen.hideturtle()
screen.mainloop()
