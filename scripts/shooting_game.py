import tkinter as tk
import random

# Window setup
WIDTH = 600
HEIGHT = 500

root = tk.Tk()
root.title("2D Shooting Game (No Pygame)")
root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Player
# Try to load a custom shooter image (shooter.png). If unavailable, use a polygon fallback.
shooter_img = None
try:
    shooter_img = tk.PhotoImage(file="shooter.png")
except tk.TclError:
    shooter_img = None

player_speed = 20
if shooter_img:
    player = canvas.create_image(WIDTH // 2, HEIGHT - 50, image=shooter_img)
else:
    # Triangle fallback roughly matching previous rectangle position
    player = canvas.create_polygon(
        WIDTH // 2, HEIGHT - 70,
        WIDTH // 2 - 20, HEIGHT - 30,
        WIDTH // 2 + 20, HEIGHT - 30,
        fill="green"
    )

# Lists
bullets = []
enemies = []

score = 0
score_text = canvas.create_text(10, 10, anchor="nw", fill="white", font=("Arial", 14),
                                text="Score: 0")

game_running = True

# Move player
def move_left(event):
    bbox = canvas.bbox(player)
    if bbox and bbox[0] > 0:
        canvas.move(player, -player_speed, 0)

def move_right(event):
    bbox = canvas.bbox(player)
    if bbox and bbox[2] < WIDTH:
        canvas.move(player, player_speed, 0)

# Shoot bullet
def shoot(event):
    if not game_running:
        return
    bbox = canvas.bbox(player)
    if not bbox:
        return
    x1, y1, x2, y2 = bbox
    bullet = canvas.create_rectangle(
        (x1 + x2) / 2 - 3, y1 - 10,
        (x1 + x2) / 2 + 3, y1,
        fill="white"
    )
    bullets.append(bullet)

# Create enemy
def create_enemy():
    if not game_running:
        return
    x = random.randint(20, WIDTH - 40)
    enemy = canvas.create_rectangle(x, 0, x + 30, 30, fill="red")
    enemies.append(enemy)
    root.after(1000, create_enemy)

# Move bullets
def move_bullets():
    global score, game_running
    if not game_running:
        return

    for bullet in bullets[:]:
        canvas.move(bullet, 0, -10)
        if canvas.coords(bullet)[1] < 0:
            canvas.delete(bullet)
            bullets.remove(bullet)

        for enemy in enemies[:]:
            if check_collision(bullet, enemy):
                canvas.delete(bullet)
                canvas.delete(enemy)
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                canvas.itemconfig(score_text, text=f"Score: {score}")
                break

    root.after(50, move_bullets)

# Move enemies
def move_enemies():
    global game_running
    if not game_running:
        return

    for enemy in enemies[:]:
        canvas.move(enemy, 0, 5)
        if canvas.coords(enemy)[3] > HEIGHT:
            game_over()

        if check_collision(enemy, player):
            game_over()

    root.after(100, move_enemies)

# Collision detection
def check_collision(a, b):
    a_bbox = canvas.bbox(a)
    b_bbox = canvas.bbox(b)
    if not a_bbox or not b_bbox:
        return False
    ax1, ay1, ax2, ay2 = a_bbox
    bx1, by1, bx2, by2 = b_bbox
    return ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1

# Game over
def game_over():
    global game_running
    game_running = False
    canvas.create_text(WIDTH/2, HEIGHT/2 - 20,
                       fill="white", font=("Arial", 24),
                       text="GAME OVER")
    canvas.create_text(WIDTH/2, HEIGHT/2 + 20,
                       fill="white", font=("Arial", 16),
                       text=f"Final Score: {score}")

# Key bindings
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<space>", shoot)

# Start game loops
create_enemy()
move_bullets()
move_enemies()

root.mainloop()
