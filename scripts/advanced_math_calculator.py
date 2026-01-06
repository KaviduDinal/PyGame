import math
import statistics

history = []

# ---------- BASIC OPERATIONS ----------
def basic_calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("1.Add  2.Subtract  3.Multiply  4.Divide")
    ch = input("Choose: ")

    if ch == "1":
        res = a + b
    elif ch == "2":
        res = a - b
    elif ch == "3":
        res = a * b
    elif ch == "4":
        res = a / b if b != 0 else "Error"
    else:
        print("Invalid choice")
        return

    history.append(res)
    print("Result:", res)

# ---------- POWER & ROOT ----------
def power_root():
    x = float(input("Enter number: "))
    print("1.Power  2.Square Root  3.Factorial")
    ch = input("Choose: ")

    if ch == "1":
        p = int(input("Enter power: "))
        res = x ** p
    elif ch == "2":
        res = math.sqrt(x)
    elif ch == "3":
        res = math.factorial(int(x))
    else:
        print("Invalid")
        return

    history.append(res)
    print("Result:", res)

# ---------- TRIGONOMETRY ----------
def trigonometry():
    angle = float(input("Enter angle in degrees: "))
    rad = math.radians(angle)
    print("1.sin  2.cos  3.tan")
    ch = input("Choose: ")

    if ch == "1":
        res = math.sin(rad)
    elif ch == "2":
        res = math.cos(rad)
    elif ch == "3":
        res = math.tan(rad)
    else:
        print("Invalid")
        return

    history.append(res)
    print("Result:", res)

# ---------- LOGARITHMS ----------
def logarithms():
    x = float(input("Enter number: "))
    print("1.log10  2.ln")
    ch = input("Choose: ")

    if ch == "1":
        res = math.log10(x)
    elif ch == "2":
        res = math.log(x)
    else:
        print("Invalid")
        return

    history.append(res)
    print("Result:", res)

# ---------- STATISTICS ----------
def statistics_calc():
    nums = list(map(float, input("Enter numbers separated by space: ").split()))
    print("1.Mean  2.Median  3.Variance")
    ch = input("Choose: ")

    if ch == "1":
        res = statistics.mean(nums)
    elif ch == "2":
        res = statistics.median(nums)
    elif ch == "3":
        res = statistics.variance(nums)
    else:
        print("Invalid")
        return

    history.append(res)
    print("Result:", res)

# ---------- MATRIX ----------
def matrix_calc():
    print("Matrix size 2x2 only")
    print("Enter matrix A:")
    A = [[int(input()) for _ in range(2)] for _ in range(2)]
    print("Enter matrix B:")
    B = [[int(input()) for _ in range(2)] for _ in range(2)]

    print("1.Add  2.Multiply")
    ch = input("Choose: ")

    if ch == "1":
        res = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
    elif ch == "2":
        res = [[A[i][0]*B[0][j] + A[i][1]*B[1][j] for j in range(2)] for i in range(2)]
    else:
        print("Invalid")
        return

    history.append(res)
    print("Result:", res)

# ---------- QUADRATIC EQUATION ----------
def quadratic_solver():
    print("ax² + bx + c = 0")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    d = b*b - 4*a*c
    if d < 0:
        print("No real roots")
        return

    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    history.append((r1, r2))
    print("Roots:", r1, r2)

# ---------- HISTORY ----------
def show_history():
    print("Calculation History:")
    for i, h in enumerate(history, 1):
        print(i, ":", h)

# ---------- MAIN MENU ----------
while True:
    print("\n==== ADVANCED MATH CALCULATOR ====")
    print("1.Basic Calculator")
    print("2.Power / Root / Factorial")
    print("3.Trigonometry")
    print("4.Logarithms")
    print("5.Statistics")
    print("6.Matrix Operations")
    print("7.Quadratic Equation Solver")
    print("8.View History")
    print("9.Exit")

    choice = input("Choose option: ")

    if choice == "1":
        basic_calculator()
    elif choice == "2":
        power_root()
    elif choice == "3":
        trigonometry()
    elif choice == "4":
        logarithms()
    elif choice == "5":
        statistics_calc()
    elif choice == "6":
        matrix_calc()
    elif choice == "7":
        quadratic_solver()
    elif choice == "8":
        show_history()
    elif choice == "9":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
