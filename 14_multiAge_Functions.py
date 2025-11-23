#Times Table
def multiplication_table(number, upto=10):
    print(f"\nMultiplication Table for {number}")
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")
iNumber = int(input("Type a number: "))
multiplication_table(iNumber)

#new
def multiplication_table(number, upto=11):
    print(f"\nMultiplication Table for {number}")
    for i in range(1, upto, + 1):
        print(f"{number} x {i} = {number * i}")
iNumber = int(input("Type a number: "))
multiplication_table(iNumber)

def multiplication_table(number, start=1, end=11):
    print(f"\n📘 Multiplication Table for {number}")
    print("-" * 30)
    for i in range(1, 11, 1):
        result = number * i
        print(f"{number:>3} × {i:<3} = {result:<4}")
    print("-" * 30)

# Get user input safely (v1)
# try:
#     num = int(input("Enter a number: "))
#     limit = input("Up to what number?: ")
#     limit = int(limit) 
#         if limit.strip() 
#         else 10

#     multiplication_table(num, 1, limit)
    
# except ValueError:
#     print("⚠️ Please enter a valid integer.")
# Get user input (v2)
try:
    num = int(input("Enter a number: "))
    limit = input("Up to what number: ")
    if limit.strip() == "":
        limit = 10
    else:
        limit = int(limit)

    
    multiplication_table(num, limit + 1)

except ValueError:
    print("⛔Please enter a valid whole number!")

# Get user input safely (v3)
# num = input("Enter a number: ")

# if not num.isdigit():
#     print("⚠️ Please enter a valid whole number.")
# else:
#     num = int(num)
#     limit = input("Up to what number? (default 10): ").strip()
#     if limit == "":
#         limit = 10
#     else:
#         limit = int(limit)

#     multiplication_table(num, limit)

#Age Category Checker
age = int(input("Enter your age: "))

if age < 13:
    print("You're a child. 🧸")
elif age < 20:
    print("You're a teenager. 🎒")
elif age < 60:
    print("You're an adult. 💼")
else:
    print("You're a senior citizen. 👴👵")

#Temperature Advisor Checker
temp = float(input("Enter the current temperature (°C): "))

if temp < 0:
    print(f"❄️ DANG! {temp}?? It's freezing! Wear a heavy coat, gloves, and a hat.")
elif temp < 10:
    print(f"🧤 Oooft.. {temp} degrees Celsius? It's quite cold — wear a jacket or sweater.")
elif temp < 20:
    print(f"🌤️ Ahhh... {temp} is my favorite weather. Mild weather. A light jacket should do.")
elif temp < 30:
    print(f"😎 Phew, {temp}? It's warm! T-shirt weather.")
else:
    print(f"🔥 Damn BOI, {temp}?? It's hot outside! Stay cool and hydrated.")




# # multiplication_table() function
# def multiplication_table(number, start=1, end=10):
#     print(f"\nMultiplication Table for {number}")
#     print("-" * 25)
#     for i in range(start, end + 1):
#         print(f"{number} x {i} = {number * i}")
#     print("-" * 25)

# Get user input safely (v1)
try:
    num = int(input("Enter a number: "))
    limit = input("Up to what number?: ").strip()
    limit = int(limit) if limit else 10

    multiplication_table(num, 1, limit)

except ValueError:
    print("⚠️ Please enter a valid integer.")


# Get user input safely (v2)
try:
    num = int(input("Enter a number: "))
    limit = input("Up to what number?: ").strip()
    if limit == "":
        limit = 10
    else:
        limit = int(limit)

    multiplication_table(num, 1, limit)

except ValueError:
    print("⛔ Please enter a valid whole number!")


# Get user input safely (v3)
num = input("Enter a number: ").strip()

if not num.isdigit():
    print("⚠️ Please enter a valid whole number.")
else:
    num = int(num)
    limit = input("Up to what number? (default 10): ").strip()
    if limit == "":
        limit = 10
    else:
        limit = int(limit)

    multiplication_table(num, 1, limit)

# Renee's combo: 
number = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

print(f"\nMultiplication table for {number} up to {limit}:\n")

for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")




