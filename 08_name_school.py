# Name & School - Exercise
# Formatting and Variable OUTPUT using F-strings

sName = input("What is your first name: ")
sSchool = input("What school do you attend: ")
sCourse = input("What course are you taking at STCC: ")
print(f"Name: {sName}, " f"School: {sSchool}, " f"Course: {sCourse}")

sName = "Renee"
print(f"{sName:^20}")
print(f"{sName:<20}")
print(f"{sName:>20}")
