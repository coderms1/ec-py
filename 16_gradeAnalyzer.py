# Grade Analyzer - FULL
# ECA - Python 11/23/2025

# Prompt user for INPUT
sName = input("Name of person whose grades we are calculating: ")

iTest1 = int(input("Enter Test Score #1: "))
iTest2 = int(input("Enter Test Score #2: "))
iTest3 = int(input("Enter Test Score #3: "))
iTest4 = int(input("Enter Test Score #4: "))

sDrop = input("Drop the lowest grade? (Y/N): ").upper()

# Calculate Average Score
if sDrop == "Y":
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        fAverage = (iTest2 + iTest3 + iTest4) / 3
    elif iTest2 <= iTest1 and iTest2 <= iTest3 and iTest2 <= iTest4:
        fAverage = (iTest1 + iTest3 + iTest4) / 3
    elif iTest3 <= iTest1 and iTest3 <= iTest2 and iTest3 <= iTest4:
        fAverage = (iTest1 + iTest2 + iTest4) / 3
    else:
        fAverage = (iTest1 + iTest2 + iTest3) / 3
else:
    fAverage = (iTest1 + iTest2 + iTest3 + iTest4) / 4

# Perform LOGIC to determine Letter Grade
def calc_grade(fAverage):
    if fAverage >= 97:
        sLetterGrade = "A+"
    elif fAverage >= 93:
        sLetterGrade = "A"
    elif fAverage >= 90:
        sLetterGrade = "A-"
    elif fAverage >= 87:
        sLetterGrade = "B+"
    elif fAverage >= 83:
        sLetterGrade = "B"
    elif fAverage >= 80:
        sLetterGrade = "B-"
    elif fAverage >= 77:
        sLetterGrade = "C+"
    elif fAverage >= 73:
        sLetterGrade = "C"
    elif fAverage >= 70:
        sLetterGrade = "C-"
    elif fAverage >= 67:
        sLetterGrade = "D+"
    elif fAverage >= 63:
        sLetterGrade = "D"
    elif fAverage >= 60:
        sLetterGrade = "D-"
    else:
        sLetterGrade = "F"

    return sLetterGrade

# Calc Letter Grade
sLetterGrade = calc_grade(fAverage)

# Display OUTPUT to user
print("\n=== Grade Report ===\n")
print('-' * 20)
print(f"Student Name: {sName}")
print(f"Average Score: {fAverage:.1f}")
print(f"Letter Grade: {sLetterGrade}")
