# ======================================================
# 3D ANIMATION GENERATOR
# One File Python Mini Project
# Uses VPython
# ======================================================

from vpython import *
import time
import math

# ---------------- SCENE SETUP ----------------
scene.title = "3D Animation Generator"
scene.width = 900
scene.height = 600
scene.background = color.black

# ---------------- UTILITY ----------------

def clear_scene():
    for obj in scene.objects:
        obj.visible = False
    scene.objects.clear()

# ---------------- ANIMATION 1: ROTATING CUBE ----------------

def rotating_cube():
    clear_scene()
    cube = box(size=vector(2,2,2), color=color.cyan)
    
    while True:
        rate(60)
        cube.rotate(angle=0.03, axis=vector(1,1,0))

# ---------------- ANIMATION 2: BOUNCING BALL ----------------

def bouncing_ball():
    clear_scene()
    floor = box(pos=vector(0,-2,0), size=vector(10,0.2,10), color=color.green)
    ball = sphere(pos=vector(0,2,0), radius=0.5, color=color.red)
    
    velocity = vector(0,-0.05,0)
    gravity = vector(0,-0.002,0)

    while True:
        rate(100)
        velocity += gravity
        ball.pos += velocity
        
        if ball.pos.y <= -1.5:
            velocity.y = abs(velocity.y)

# ---------------- ANIMATION 3: SOLAR SYSTEM ----------------

def solar_system():
    clear_scene()
    
    sun = sphere(radius=1.2, color=color.orange, emissive=True)
    planet = sphere(radius=0.4, color=color.blue, make_trail=True)
    
    angle = 0

    while True:
        rate(60)
        angle += 0.02
        planet.pos = vector(4*math.cos(angle), 0, 4*math.sin(angle))

# ---------------- ANIMATION 4: SPIRAL MOTION ----------------

def spiral_motion():
    clear_scene()
    ball = sphere(radius=0.3, color=color.magenta, make_trail=True)
    
    t = 0
    while True:
        rate(60)
        t += 0.05
        ball.pos = vector(
            math.cos(t)*t/3,
            math.sin(t)*t/3,
            t/4
        )

# ---------------- ANIMATION 5: WAVE MOTION ----------------

def wave_motion():
    clear_scene()
    balls = []
    
    for i in range(-10, 11):
        b = sphere(pos=vector(i,0,0), radius=0.2, color=color.cyan)
        balls.append(b)

    t = 0
    while True:
        rate(30)
        t += 0.1
        for i, b in enumerate(balls):
            b.pos.y = math.sin(t + i*0.5)

# ---------------- MENU ----------------

def show_menu():
    print("""
========= 3D ANIMATION GENERATOR =========
1. Rotating Cube
2. Bouncing Ball
3. Solar System
4. Spiral Motion
5. Wave Motion
=========================================
""")

show_menu()

choice = input("Enter animation number (1-5): ")

if choice == "1":
    rotating_cube()
elif choice == "2":
    bouncing_ball()
elif choice == "3":
    solar_system()
elif choice == "4":
    spiral_motion()
elif choice == "5":
    wave_motion()
else:
    print("Invalid choice!")
