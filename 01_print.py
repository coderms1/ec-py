# Early College Python
# Learning print() function

print("Today is Thursday, September 18, 2025.")

name = input("What is your name? ")
age = int(input("How old are you? "))
subject = input("What is your favorite subject in school? ")
year_when_75 = (2025 + (75 -  age))

print(f"Nice to meet you, {name}!")

print(f"WOW, {name}! You're {age} years old today and you're \nfavorite subject in school is {subject}!\nFYI- you will turn 75 in the year {year_when_75}!")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum1 = (num1 + num2)
print(f"The sum of {num1} and {num2} is {sum1}.")

birth_year = int(input("Enter your birth year: "))
current_year = 2025
age = (current_year - birth_year)
print(f"Year are {age} year old. ")

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print(f"Sum: {number1 + number2}")
print(f"Difference: {number1 - number2}")
print(f"Product: {number1 * number2}")
print(f"Quotient: {number1 / number2}")
