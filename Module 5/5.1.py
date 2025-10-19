import random

num_dice = int(input("How many dice do you want to roll? "))

total_sum = 0
for _ in range(num_dice):
    roll = random.randint(1, 6)
    total_sum += roll

print("The sum of the dice is:", total_sum)