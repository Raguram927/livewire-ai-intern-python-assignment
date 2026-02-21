#SECTION A: LOOPS
# Sum of Digits: Given an integer N, print the sum of its digits.
'''N = int(input("Enter an integer: "))
sum_digits = 0

while N > 0:
    sum_digits += N % 10   
    N //= 10        

print("Sum of digits:", sum_digits)'''
#Reverse a Number: Reverse the given integer without converting to string.
'''N = int(input("Enter an integer: "))
reverse_num = 0

while N > 0:
    digit = N % 10          
    reverse_num = reverse_num * 10 + digit
    N //= 10                
print("Reversed number:", reverse_num)'''
#Armstrong Number: Check whether a number is Armstrong or not.
'''N = int(input("Enter an integer: "))
num = N
sum_of_powers = 0
digits = len(str(N))  

while num > 0:
    digit = num % 10
    sum_of_powers += digit ** digits
    num //= 10

if sum_of_powers == N:
    print(N, "is an Armstrong number")
else:
    print(N, "is not an Armstrong number")'''
#Fibonacci Series: Print first N Fibonacci numbers.
'''N = int(input("Enter how many Fibonacci numbers: "))

a, b = 0, 1
count = 0

while count < N:
    print(a, end=" ")
    a, b = b, a + b
    count += 1'''
#Prime Count: Count how many prime numbers exist from 1 to N.
'''N = int(input("Enter an integer: "))
prime_count = 0

for num in range(2, N + 1):   
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1

print("Number of primes from 1 to", N, ":", prime_count)'''
#SECTION B: FUNCTIONS
#Q6. Even or Odd Function: Create a function to check whether a number is even or odd.

'''N = int(input("Enter an integer: "))
even_or_odd(N)
def even_or_odd(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")'''

#Factorial Function: Write a function to return factorial of a number.
'''N = int(input("Enter an integer: "))
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("Factorial of", N, "is", factorial(N))'''
#Largest of Three: Create a function to find the largest of three numbers
'''x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("Largest number is:", largest_of_three(x, y, z))'''

#Count Vowels: Create a function to count vowels in a string
'''text = input("Enter a string: ")
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print("Number of vowels:", count_vowels(text))'''
#. Simple Calculator: Create menu-driven calculator using functions.
'''def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

while True:
    print("\n--- Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting calculator. Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice! Please try again.")'''

#SECTION C: MODULES
#Q11. Create Custom Module: Create operations.py with square() and cube() functions and import it.
'''num=int(input("enter a number"))
def square(num):
    return num * num

def cube(num):
    return num * num * num

print("Square of 5:", square(num))
print("Cube of 2:", cube(num))'''
#Q12. Random Guess Game: Generate random number (1-100) and build guessing game using loop.

'''import random
secret_number = random.randint(1, 100)

print("Welcome to the Guessing Game!")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(" Congratulations! You guessed it right.")
        break'''
#. Math Module Usage: Use math module to calculate square root, power, and factorial
'''import math
num1 = int(input("enter a number"))
print("Square root of", num1, "is:", math.sqrt(num1))

base = int(input("enter a number"))
exponent = 5
print(base, "to the power of", exponent, "is:", math.pow(base, exponent))

num2 = int(input("enter a number "))
print("Factorial of", num2, "is:", math.factorial(num2))'''
#BONUS MINI PROJECT
# Student Management System: Create a menu-driven program that allows users to add student details, view all students, search by roll number, and calculate average marks. Use loops, functions, and modular programming concepts.
# Student Management System

'''students = []  

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students.append({"roll": roll, "name": name, "marks": marks})
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
    else:
        print("\n--- Student List ---")
        for s in students:
            print("Roll:", s["roll"], "| Name:", s["name"], "| Marks:", s["marks"])
        print()

def search_student():
    roll = int(input("Enter Roll Number to search: "))
    for s in students:
        if s["roll"] == roll:
            print("Student Found -> Roll:", s["roll"], "| Name:", s["name"], "| Marks:", s["marks"], "\n")
            return
    print("Student not found!\n")

def calculate_average():
    if not students:
        print("No student records to calculate average.\n")
    else:
        total = sum(s["marks"] for s in students)
        avg = total / len(students)
        print("Average Marks of all students:", avg, "\n")

while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search by Roll Number")
    print("4. Calculate Average Marks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        calculate_average()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")'''

