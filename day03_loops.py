# Day 3: Loops

# 1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


# 2. Print even numbers from 1 to 20
for i in range(2, 21, 2):
    print(i)

# 3. Sum of first n numbers
n = int(input("Enter the number"))
okay = 0

for i in range(1, n+1):
    okay = okay + i

print(okay)


# 4. Multiplication table
n = int(input("Enter the number"))

for i in range(1, 11):
    print(n, "x", i, '=', n * i)

# 5. Factorial of a Number
n = int(input("Enter the number"))
total = 1

for i in range(1, n+1):
    total = total * i
    
print(total)


