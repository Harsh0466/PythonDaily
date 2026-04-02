# Day 1: Python Basics

# 1. Hello World
print("Hello, World!")


# 2. Name and Age
name = 'Harsh'
age = 21
print("Hey my name is", name, "and I am", age, "years old") #this one is cleaner 
or 
print(("Hey my name is"),name,("and i am"),age,("years old"))

# 3. Addition
a = 10
b = 5
print("Sum is:", a + b)


# 4. User Input
name = input("Enter your name: ")
print("Hello", name)
or
print(("Hello"), name)

# 5. Square of a Number
a = int(input("Enter the value of a"))
print(a * a)

# 6. Basic Calculator

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("The addition is:", a + b)
print("The subtraction is:", a - b)
print("The multiplication is:", a * b)


# 7. Type Check

number = 15
decimal = 1.5
character = "harsh gupta"

print(type(number))
print(type(decimal))
print(type(character))


# 8. Swap Two Numbers

a = 5
b = 4

print("Before swapping:", a, b)

temp = a
a = b
b = temp

print("After swapping:", a, b)
