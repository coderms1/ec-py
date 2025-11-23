# Temperature Converter (Fahrenheit v. Celsius)
# Date: 10/28/2025

# GREETING (say whassup 😎)
print("Zim's Temp Converter: \n")

# INPUT (Prompt user)
fTemp = float(input("Enter a temperature: "))
sType = input("Is this Fahrenheit or Celsius [F/C]: ").upper()

# PROCESS (Calculations)
fFahrenheit = ((9.0 / 5.0) * fTemp) + 32
fCelsius = (5.0 / 9.0) * (fTemp - 32)

# OUTPUT (Logic -> display results)
if sType == 'F':
    if fTemp > 212:
        print("Temp cannot be > 212! 🥵🪭")
    elif fTemp <= 212:
        print(f"The Celsius equivalent is: {fCelsius:.1f} 🌡️")
elif sType == 'C':
    if fTemp > 100: 
        print("Temp cannot be > 100! 🔥🧑‍🚒")
    elif fTemp <= 100:
        print(f"The Celsius equivalent is: {fFahrenheit:.1f} 🌡️")
else:
    print("PLEASE, only enter F or C for Temperature Type! 😠")
