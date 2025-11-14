# for loops, calculations, and print
print(1)
print(2)
print(3)
print(4)
print(5)

#for loops
for i in range(1, 6):
    print(i)
for j in range(1, 11):
    print(j)
for x in range(2, 9, 2):
    print(x)
for z in range(10):
    print(z, end='')

print() # Create space

## Dog Age Calculator ##

#Input
sDog = input("What is the dog's name: ")
fAge = float(input(f"Enter is {sDog}'s age: "))

#Calculation
fHuman = fAge * 7.3

#Output
print(f"{sDog}'s age in human years is: {fHuman:.1f}")

##Math Problems 

#Addition
a = 8
b = 5
result = a + b
print(f"Addition: {result}")

#Subtraction
a = 8
b = 5
result = a - b
print(f"Subtraction: {result}")

#Multiplication
a = 8
b = 5
result = a * b
print(f"Multiplication: {result}")

#Division (Floating point)
a = 8
b = 5
result = a / b
print(f"Floating Point Division: {result}")

#Division (Integer)
a = 8
b = 5
result = a // b
print(f"Integer Division: {result}")

#Modulus
a = 8
b = 5
result = a % b
print(f"Remainder: {result}")

#Exponents
a = 8
b = 5
result = a ** b
print(f"Exponents: {result}")
