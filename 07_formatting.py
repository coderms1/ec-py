# Extra Print Formatting (strings & numbers)

# TAB Examples
print("Monday\t\tTuesday\t\tWednesday")
print("Thursday\tFriday\t\tSaturday")

amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f"The monthly pyament is {monthly_payment:.2f}.")

monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print(f"Your annual pay is ${annual_pay:,.2f}")

# Formatting Numbers
price = 3.5
print(f"Price: ${price:.2f}")
temperature = 73.4567
print(f"Today’s temperature: {temperature:.2f}°F")
average = 89.999
print(f"Class average: {average:.2f}%")

# Money with COMMAS
big_number = 2500000
print(f"Total Revenue: ${big_number:,.2f}")
salary = 48235.75
print(f"Your salary is ${salary:,.2f}")
donations = 123456789.0
print(f"Total donations collected: ${donations:,.2f}")

# String + Variable Formatting
name = "Zim"
age = 29
print(f"{name} is {age} years old.")
item = "Laptop"
price = 999.99
print(f"The {item} costs ${price:.2f}.")
student = "Maria"
gpa = 3.845
print(f"{student}'s GPA is {gpa:.2f}")
