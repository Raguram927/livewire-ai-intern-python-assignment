'''N = int(input("Enter an integer: "))
sum_digits = 0

while N > 0:
    sum_digits += N % 10   
    N //= 10        

print("Sum of digits:", sum_digits)'''
'''N = int(input("Enter an integer: "))
reverse_num = 0

while N > 0:
    digit = N % 10          
    reverse_num = reverse_num * 10 + digit
    N //= 10                
print("Reversed number:", reverse_num)'''
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
'''N = int(input("Enter how many Fibonacci numbers: "))

a, b = 0, 1
count = 0

while count < N:
    print(a, end=" ")
    a, b = b, a + b
    count += 1'''
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
'''N = int(input("Enter an integer: "))
even_or_odd(N)
def even_or_odd(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")'''

'''N = int(input("Enter an integer: "))
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("Factorial of", N, "is", factorial(N))'''
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

'''text = input("Enter a string: ")
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print("Number of vowels:", count_vowels(text))'''
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








