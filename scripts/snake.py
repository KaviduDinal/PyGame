import turtle
import time
import random
import colorsys

# Movement speed configuration (increase INITIAL_DELAY to slow the snake)
INITIAL_DELAY = 0.15
MIN_DELAY = 0.05
DELAY_DECREMENT = 0.0005
delay = INITIAL_DELAY
score = 0
high_score = 0

# Screen
wn = turtle.Screen()
wn.title("Snake Game 🐍")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Create a compound shape for a more interesting snake head (with eyes)
def _register_snake_head_shape():
    head_shape = turtle.Shape("compound")
    # Main head square (20x20)
    main = [(-10, -10), (10, -10), (10, 10), (-10, 10)]
    head_shape.addcomponent(main, "#2ecc71", "#1e7a3a")

    # Left eye (white)
    left_eye = [(-6, 4), (-2, 4), (-2, 8), (-6, 8)]
    head_shape.addcomponent(left_eye, "white", "black")
    # Right eye (white)
    right_eye = [(2, 4), (6, 4), (6, 8), (2, 8)]
    head_shape.addcomponent(right_eye, "white", "black")

    # Left pupil (black)
    l_pupil = [(-5, 5), (-3, 5), (-3, 7), (-5, 7)]
    head_shape.addcomponent(l_pupil, "black", "black")
    # Right pupil (black)
    r_pupil = [(3, 5), (5, 5), (5, 7), (3, 7)]
    head_shape.addcomponent(r_pupil, "black", "black")

    try:
        turtle.register_shape('snake_head', head_shape)
    except Exception:
        pass


_register_snake_head_shape()
head = turtle.Turtle()
head.speed(0)
head.shape('snake_head')
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 16, "normal"))

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.setheading(90)

def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.setheading(270)

def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.setheading(180)

def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.setheading(0)

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Collision with wall
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        delay = INITIAL_DELAY
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center", font=("Courier", 16, "normal"))

    # Collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        # Slightly smaller segments for a smoother look
        new_segment.shapesize(stretch_wid=0.9, stretch_len=0.9)
        # Gradient green color: hue near green, darken as snake grows
        hue = max(0.15, 0.33 - min(len(segments), 20) * 0.015)
        r, g, b = colorsys.hsv_to_rgb(hue, 0.9, 0.9)
        new_segment.color((r, g, b))
        new_segment.penup()
        segments.append(new_segment)

        # Gradually speed up the snake as it grows, but don't go below MIN_DELAY
        delay = max(MIN_DELAY, delay - DELAY_DECREMENT)
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}",
                  align="center", font=("Courier", 16, "normal"))

    # Move snake body
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Collision with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            delay = INITIAL_DELAY
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}",
                      align="center", font=("Courier", 16, "normal"))

    time.sleep(delay)
