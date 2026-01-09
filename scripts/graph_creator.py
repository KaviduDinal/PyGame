# =====================================================
# GRAPH CREATOR SYSTEM
# One File Python Mini Project
# =====================================================

import matplotlib.pyplot as plt
import os
import time

# ---------------- UTILITY FUNCTIONS ----------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress ENTER to continue...")

def save_graph(name):
    filename = f"{name}_{int(time.time())}.png"
    plt.savefig(filename)
    print(f"\nGraph saved as: {filename}")

def get_numeric_list(prompt):
    print(prompt)
    print("Enter numbers separated by commas (e.g., 10,20,30)")
    data = input(">> ")
    return list(map(float, data.split(",")))

# ---------------- GRAPH FUNCTIONS ----------------

def line_graph():
    x = get_numeric_list("Enter X values")
    y = get_numeric_list("Enter Y values")

    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title("Line Graph")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True)
    save_graph("line_graph")
    plt.show()

def bar_graph():
    labels = input("Enter labels separated by commas: ").split(",")
    values = get_numeric_list("Enter values")

    plt.figure()
    plt.bar(labels, values)
    plt.title("Bar Chart")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    save_graph("bar_chart")
    plt.show()

def pie_chart():
    labels = input("Enter labels separated by commas: ").split(",")
    values = get_numeric_list("Enter values")

    plt.figure()
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Pie Chart")
    save_graph("pie_chart")
    plt.show()

def scatter_plot():
    x = get_numeric_list("Enter X values")
    y = get_numeric_list("Enter Y values")

    plt.figure()
    plt.scatter(x, y)
    plt.title("Scatter Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    save_graph("scatter_plot")
    plt.show()

def histogram():
    data = get_numeric_list("Enter data values")

    plt.figure()
    plt.hist(data, bins=10)
    plt.title("Histogram")
    plt.xlabel("Data Range")
    plt.ylabel("Frequency")
    save_graph("histogram")
    plt.show()

# ---------------- MENU ----------------

def show_menu():
    print("""
============= GRAPH CREATOR SYSTEM =============
1. Line Graph
2. Bar Chart
3. Pie Chart
4. Scatter Plot
5. Histogram
0. Exit
===============================================
""")

# ---------------- MAIN PROGRAM ----------------

while True:
    clear_screen()
    show_menu()
    choice = input("Select graph type: ")

    if choice == "1":
        line_graph()
        pause()

    elif choice == "2":
        bar_graph()
        pause()

    elif choice == "3":
        pie_chart()
        pause()

    elif choice == "4":
        scatter_plot()
        pause()

    elif choice == "5":
        histogram()
        pause()

    elif choice == "0":
        print("Exiting Graph Creator System...")
        break

    else:
        print("Invalid choice!")
        pause()

print("\nThank you for using Graph Creator System!")
