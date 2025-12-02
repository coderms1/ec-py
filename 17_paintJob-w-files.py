# Class: Python: CIT-115 (FALL 2025)
# Assignment: Paint Job w/ Files
# Instructor: Professor Tetault
from math import ceil 

# Prompt User for INPUT - Function
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value
        except:
            print("Invalid number. Try again.")

# Calculation Functions (PROCESS)
def getGallonsOfPaint(square_feet, feet_per_gallon):
    return ceil(square_feet / feet_per_gallon)

def getLaborHours(labor_hours_per_gallon, total_gallons):
    return labor_hours_per_gallon * total_gallons

def getLaborCost(labor_hours, labor_rate):
    return labor_hours * labor_rate

def getPaintCost(total_gallons, paint_price):
    return total_gallons * paint_price

def getSalesTax(state):
    state = state.upper()
    if state == "CT" or state == "VT":
        return 0.06
    elif state == "MA":
        return 0.0625
    elif state == "ME":
        return 0.085
    elif state == "RI":
        return 0.07
    elif state == "NH":
        return 0.0
    else:
        return 0.0

# Display OUTPUT & Write File - Function
def showCostEstimate(gallons, labor_hours, labor_cost, paint_cost, tax_rate, last_name):
    subtotal = labor_cost + paint_cost
    tax = subtotal * tax_rate
    total_cost = subtotal + tax

    print("-------------------------------------")
    print(f"Gallons of paint: {gallons}")
    print(f"Hours of labor: {labor_hours}")
    print(f"Paint charges: ${paint_cost:.2f}")
    print(f"Labor charges: ${labor_cost:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total cost: ${total_cost:.2f}")
    print("-------------------------------------")

    filename = last_name + "_PaintJobOutput.txt"

    with open(filename, "w") as file:
        file.write(f"Gallons of paint: {gallons}\n")
        file.write(f"Hours of labor: {labor_hours}\n")
        file.write(f"Paint charges: ${paint_cost:.2f}\n")
        file.write(f"Labor charges: ${labor_cost:.2f}\n")
        file.write(f"Tax: ${tax:.2f}\n")
        file.write(f"Total cost: ${total_cost:.2f}\n")

    print(f"File '{filename}' was created.")

# MAIN FUNCTION 
def main():
    sqft = getFloatInput("Enter wall space in square feet: ")
    paint_price = getFloatInput("Enter paint price per gallon: ")
    feet_per_gallon = getFloatInput("Enter feet per gallon: ")
    labor_hours_pg = getFloatInput("How many labor hours per gallon: ")
    labor_rate = getFloatInput("Labor charge per hour: ")

    state = input("State job is in: ").upper()
    last_name = input("Customer Last Name: ").title()

    gallons = getGallonsOfPaint(sqft, feet_per_gallon)
    labor_hours = getLaborHours(labor_hours_pg, gallons)
    paint_cost = getPaintCost(gallons, paint_price)
    labor_cost = getLaborCost(labor_hours, labor_rate)
    tax_rate = getSalesTax(state)

    showCostEstimate(gallons, labor_hours, labor_cost, paint_cost, tax_rate, last_name)


main()
