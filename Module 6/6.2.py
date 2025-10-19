import random

def roll_disc(sides):
    return random.randint(1, sides)
def main():
    sides = int(input("Enter the number of the sides on the dice: "))
    max_side = sides
    result = 0
    while result != max_side:
        result = roll_disc(sides)
        print(f"Rolled: {result}")

main()