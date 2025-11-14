#Dog Age Calculator
#Constants
DOGAGE = 7.3

#Input
sName = input("What is your dog's name: ")
fAge = float(input(f"What is {sName}'s age: "))

#Calculate
fHumanAge = fAge * DOGAGE

#Output

print(f"{sName}'s human age is ", fHumanAge)
############
name1 = "Gordon"
name2 = "Matthew"
name3 = "Renee"
name4 = "Your_Name"

print(f"***{name1:^20}***")
print(f"***{name2:^20}***")
print(f"***{name3:^20}***")
print(f"***{name4:^20}***")

###########
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

# Each number is displayed in a field of 20 spaces
# and rounded to 2 decimal places.

print(f"{num1:10,.2f}{num2:20,.2f}")
print(f"{num3:10,.2f}{num4:20,.2f}")
print(f"{num5:10,.2f}{num6:20,.2f}")


############
#Constants: average weights in kg
LAPTOP_WEIGHT = 2.5          # average laptop
DOG_WEIGHT = 10.0            # small dog
HUMAN_WEIGHT = 70.0          # average human
MOTORBIKE_WEIGHT = 180.0     # average motorbike
CAR_WEIGHT = 1500.0          # small car
ELEPHANT_WEIGHT = 5000.0     # adult elephant

#Ask use for their weights
user_weight = float(input("Enter your weight in kilogrmas (kg): "))

#Calculate comparisons
laptops = user_weight / LAPTOP_WEIGHT
dogs = user_weight / DOG_WEIGHT
humans = user_weight / HUMAN_WEIGHT
motorbikes = user_weight / MOTORBIKE_WEIGHT
cars = user_weight / CAR_WEIGHT
elephants = user_weight / ELEPHANT_WEIGHT

#Print results
print("\nYour weight is approximately equal to: ")
print(f"{laptops:.2f} laptops")
print(f"{dogs:.2f}, small dogs")
print(f"{humans:.2f}, average humans")
print(f"{motorbikes:.2f}, motorbikes")
print(f"{cars:.2f}, cars")
print(f"{elephants:.2f}, elephants")
