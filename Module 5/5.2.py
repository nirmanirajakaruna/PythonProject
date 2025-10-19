numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    numbers.append(int(user_input))

numbers.sort(reverse=True)

print("Top 5 greatest numbers:")
for number in numbers[:5]:
    print(number)