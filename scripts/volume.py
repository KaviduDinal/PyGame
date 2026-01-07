import math
import datetime

# ==============================
# GLOBAL HISTORY LIST
# ==============================
history = []

# ==============================
# UTILITY FUNCTIONS
# ==============================
def record_history(shape, formula, volume):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append({
        "time": time,
        "shape": shape,
        "formula": formula,
        "volume": volume
    })

def show_history():
    if not history:
        print("\nNo calculations done yet.\n")
        return
    print("\n======= CALCULATION HISTORY =======")
    for h in history:
        print(f"{h['time']} | {h['shape']} | Volume = {h['volume']:.4f}")
    print("===================================\n")

def get_positive_float(msg):
    while True:
        try:
            value = float(input(msg))
            if value <= 0:
                print("❌ Enter a positive number!")
            else:
                return value
        except ValueError:
            print("❌ Invalid input! Enter a number.")

# ==============================
# VOLUME FUNCTIONS
# ==============================
def volume_cube():
    a = get_positive_float("Enter side length: ")
    v = a ** 3
    record_history("Cube", "a³", v)
    print(f"Volume of Cube = {v:.4f}")

def volume_cuboid():
    l = get_positive_float("Enter length: ")
    w = get_positive_float("Enter width: ")
    h = get_positive_float("Enter height: ")
    v = l * w * h
    record_history("Cuboid", "l × w × h", v)
    print(f"Volume of Cuboid = {v:.4f}")

def volume_sphere():
    r = get_positive_float("Enter radius: ")
    v = (4/3) * math.pi * r**3
    record_history("Sphere", "(4/3)πr³", v)
    print(f"Volume of Sphere = {v:.4f}")

def volume_cylinder():
    r = get_positive_float("Enter radius: ")
    h = get_positive_float("Enter height: ")
    v = math.pi * r**2 * h
    record_history("Cylinder", "πr²h", v)
    print(f"Volume of Cylinder = {v:.4f}")

def volume_cone():
    r = get_positive_float("Enter radius: ")
    h = get_positive_float("Enter height: ")
    v = (1/3) * math.pi * r**2 * h
    record_history("Cone", "(1/3)πr²h", v)
    print(f"Volume of Cone = {v:.4f}")

def volume_hemisphere():
    r = get_positive_float("Enter radius: ")
    v = (2/3) * math.pi * r**3
    record_history("Hemisphere", "(2/3)πr³", v)
    print(f"Volume of Hemisphere = {v:.4f}")

def volume_rectangular_pyramid():
    l = get_positive_float("Enter base length: ")
    w = get_positive_float("Enter base width: ")
    h = get_positive_float("Enter height: ")
    v = (1/3) * l * w * h
    record_history("Rectangular Pyramid", "(1/3)lwh", v)
    print(f"Volume of Rectangular Pyramid = {v:.4f}")

def volume_triangular_prism():
    b = get_positive_float("Enter triangle base: ")
    h = get_positive_float("Enter triangle height: ")
    L = get_positive_float("Enter prism length: ")
    v = 0.5 * b * h * L
    record_history("Triangular Prism", "(1/2)bhL", v)
    print(f"Volume of Triangular Prism = {v:.4f}")

def volume_square_pyramid():
    a = get_positive_float("Enter base side: ")
    h = get_positive_float("Enter height: ")
    v = (1/3) * a**2 * h
    record_history("Square Pyramid", "(1/3)a²h", v)
    print(f"Volume of Square Pyramid = {v:.4f}")

def volume_ellipsoid():
    a = get_positive_float("Enter semi-axis a: ")
    b = get_positive_float("Enter semi-axis b: ")
    c = get_positive_float("Enter semi-axis c: ")
    v = (4/3) * math.pi * a * b * c
    record_history("Ellipsoid", "(4/3)πabc", v)
    print(f"Volume of Ellipsoid = {v:.4f}")

# ==============================
# MENU SYSTEM
# ==============================
def menu():
    print("""
========== VOLUME CALCULATOR ==========
1. Cube
2. Cuboid
3. Sphere
4. Cylinder
5. Cone
6. Hemisphere
7. Rectangular Pyramid
8. Triangular Prism
9. Square Pyramid
10. Ellipsoid
11. Show History
0. Exit
======================================
""")

# ==============================
# MAIN PROGRAM
# ==============================
def main():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            volume_cube()
        elif choice == "2":
            volume_cuboid()
        elif choice == "3":
            volume_sphere()
        elif choice == "4":
            volume_cylinder()
        elif choice == "5":
            volume_cone()
        elif choice == "6":
            volume_hemisphere()
        elif choice == "7":
            volume_rectangular_pyramid()
        elif choice == "8":
            volume_triangular_prism()
        elif choice == "9":
            volume_square_pyramid()
        elif choice == "10":
            volume_ellipsoid()
        elif choice == "11":
            show_history()
        elif choice == "0":
            print("👋 Exiting Volume Calculator. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

# ==============================
# RUN PROGRAM
# ==============================
if __name__ == "__main__":
    main()
