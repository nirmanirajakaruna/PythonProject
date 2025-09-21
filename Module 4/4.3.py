def main():
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to quit): ")

        if user_input == "":  # empty string to quit
            break

        try:
            num = float(user_input)  # convert to number
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if len(numbers) > 0:
        print("Smallest number:", min(numbers))
        print("Largest number:", max(numbers))
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()
