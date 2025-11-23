## Early College Python - Class Code
## Instructor: Renee Tetrault
## Date: 10/30/2025
## Coder: ms1

# Traffic Lights
color = input("Enter the traffic light color (red, yellow, green): ").lower()
w
if color == 'red':
    print("Stop!🔴")
elif color == 'yellow':
    print("Slow down, slick.🟡")
elif color == 'green':
    print("Go (with caution).🟢")
else:
    print("Invalid color 🚫")

# Function - Palindrome
def is_palindrome(word):
    cleaned = word.lower().replace(" ", "") # This takes the entry, turns it lowercase & era
    return cleaned == cleaned[::-1]

word = input("Enter word, homie: ")

# if is_palindrome(word):
#     print("This IS A PALINDROME!🎉")
# else:
#     print("Nah bro, not a Palindrome - nice try though.🙄")

print(f"Is '{word.upper()}' a palindrome, True or False?\n -> {(is_palindrome(word))}!")

# Multiplication table

def m_table(num):
    # Prints the multiplication table for a given number
    print(f"\Mutlplication Table for {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

iNum = int(input("Enter a whole number: "))

# Call function 
m_table(iNum)
