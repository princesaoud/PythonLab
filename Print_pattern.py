print("print pattern")


def left_triangle(x):
    for i in range(1, x):
        print("x"),

    print("")
    for n in range(1, x - 1):
        print("x"),

    print("")
    for n in range(1, x - 2):
        print("x"),

    print("")
    for n in range(1, x - 3):
        print("x"),

    print("")
    for n in range(1, x - 4):
        print("x"),


def right_triangle(x):
    for i in range(1, x - 4):
        print("x"),

    print("")
    for n in range(1, x - 3):
        print("x"),

    print("")
    for n in range(1, x - 2):
        print("x"),

    print("")
    for n in range(1, x - 1):
        print("x"),

    print("")
    for n in range(1, x):
        print("x"),


def num_triangle(x):
    for i in range(1, x - 4):
        print(i),

    print("")
    for n in range(1, x - 3):
        print(n),

    print("")
    for n in range(1, x - 2):
        print(n),

    print("")
    for n in range(1, x - 1):
        print(n),

    print("")
    for n in range(1, x):
        print(n),


print("Pattern 1")

left_triangle(5)

print("")
print("Pattern 2 ")

right_triangle(5)

print("")
print("Pattern 3 ")

num_triangle(5)
