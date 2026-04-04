# Day 2: Conditions

# 1. Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# 2. Positive, Negative, or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")


# 3. Largest of Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Number 1 is greater than Number 2")
elif num1 == num2:
    print("Both the numbers are equal")
else:
    print("Number 2 is greater than Number 1")


# 4. Largest of Three Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 == num2 == num3:
    print("All three numbers are equal")
elif num1 == num2 > num3:
    print("Number 1 and Number 2 are equal and greater than Number 3")
elif num1 == num3 > num2:
    print("Number 1 and Number 3 are equal and greater than Number 2")
elif num2 == num3 > num1:
    print("Number 2 and Number 3 are equal and greater than Number 1")
elif num1 >= num2 and num1 >= num3:
    print("Number 1 is the greatest")
elif num2 >= num1 and num2 >= num3:
    print("Number 2 is the greatest")
else:
    print("Number 3 is the greatest")


# 5. Voting Eligibility
age = int(input("Enter your age:"))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 6. Pass or Fail
marks = int(input("Enter the marks:"))
if marks >= 40:
    print("The student passes")
else:
    print("The student fails")


