# Pet/Time Decider: Which pet for you?
# Date: 10/28/25

hours = float(input("How much time do you spend with the pets: "))

if hours < 0:
    print("Invalid input! Time cannot be negative.")
elif hours <= 1:
    print("You should prolly get a fishy, bruh.")
elif hours <= 3:
    print("A gato (cat) would be purrrfect for you!")
elif hours <= 5:
    print("You just might be a doggo person.")
else:
    print("YOU SHOULD GET A HORSE!")
