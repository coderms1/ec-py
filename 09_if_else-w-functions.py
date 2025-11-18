#If and Else statements with FUN-ctions! =]
#Check if adult or minor.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#Check score with grade with multiple conditions.
score = int(input("Enter your grade: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C or below")

#Check if number is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#Students will complete.
#Check if number is positive or negative.
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

#Students will complete.
#Check if a person is eligible to vote.
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else: print("You are not eligible to vote yet.")

#Students will complete.
#Compare two numbers.
a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))
if a > b:
    print("a is greater than b")
elif a < b:
    print("b is greater than a")
else:
    print("a and b are equal")

#Check if a number is divisible by 2 and 3
num = int(input("Enter number: "))

if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
elif num % 2 == 0:
    print("Divisible by 2 only")
elif num % 3 == 0:
    print("Divisible by 3 only")
else: print("Not divisible by 2 or 3")

#Check Login Credentials
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print ("Login successful")
else: print("Invalid credentials")

#Students will complete.
#Simple Grade Checker
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")


#Students will complete.
#def means define a function
def say_hello(name):
    print(f"Hello, {name}!")
say_hello("Renee")

# Define the function
def check_even_or_odd(number):
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

# Ask user for input
num = int(input("Enter a number: "))

# Call the function
check_even_or_odd(num)


def currency_converter():
    print("Currency Converter (USD <-> EUR <-> CAD)")
    amount = float(input("Enter amount: "))
    currency = input("Enter currency (USD/EUR/CAD): ").upper()

    if currency == "USD":
        print(f"{amount} USD = {amount * 0.86} EUR")
        print(f"{amount} USD = {amount * 1.40} CAD")
    elif currency == "EUR":
        print(f"{amount} EUR = {amount * 1.16} USD")
        print(f"{amount} EUR = {amount * 1.64} CAD")
    elif currency == "CAD":
        print(f"{amount} CAD = {amount / 1.40:.2f} USD")
        print(f"{amount} CAD = {amount / 0.61:.2f} EUR")
    else:
        print("Unknown currency.")

currency_converter()

# Simple Distance Converter
def convert_distance():
    print("Distance Converter: km <-> miles <-> meters")
    distance = float(input("Enter distance: "))
    unit = input("Enter current unit (km/miles/meters): ").lower()

    if unit == "km":
        print(f"{distance} km = {distance * 0.621371} miles")
        print(f"{distance} km = {distance * 1000} meters")
    elif unit == "miles":
        print(f"{distance} miles = {distance * 1.60934} km")
        print(f"{distance} miles = {distance * 1609.34} meters")
    elif unit == "meters":
        print(f"{distance} meters = {distance / 1000} km")
        print(f"{distance} meters = {distance / 1609.34:.2f} miles")
    else:
        print("Unknown unit.")

convert_distance()

