# Day 4: Patterns (Nested Loops)

# 1. Square Pattern
# Print a square pattern of stars

for i in range(3):
    for j in range(3):
        print("*", end=' ')
    print()


# 2. Right Triangle Pattern
# Print a right triangle pattern of stars

for i in range(4):
    for j in range(i + 1):
        print("*", end=' ')
    print()


# 3. Inverted Triangle Pattern
# Print an inverted triangle pattern of stars

for i in range(4):
    for j in range(4 - i):
        print("*", end=' ')
    print()


# 4. Number Pattern
# Print numbers in increasing triangular pattern

for i in range(4):
    for j in range(1, i + 2):
        print(j, end=' ')
    print()


# 5. Reverse Number Pattern
# Print numbers in decreasing triangular pattern

for i in range(4):
    for j in range(1, 5 - i):
        print(j, end=' ')
    print()

# Day 4: Pyramid Patterns

# 1. Increasing Pyramid 
for i in range(5):
    for j in range(5 - i):
        print("  ", end=' ')
    for k in range(0, (i * 2) + 1):
        print("* ", end=' ')
    print()


# 2. Inverted Pyramid
for i in range(5, 0, -1):
    for j in range(5 - i):
        print("  ", end=' ')
    for k in range(0, (i * 2) - 1):
        print("* ", end=' ')
    print()


