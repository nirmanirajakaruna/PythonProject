smallest = None
largest = None

while True:
        user_input = input("Enter a number (or press Enter to quit): ")

        if user_input == "":  # empty string to quit
            break

        try:
            num = float(user_input)  # convert to number
        except ValueError:
            print("Please enter a valid number.")
            continue

        if smallest is None or num < smallest:
            smallest = num
        if largest is None or num > largest:
            largest = num
        if smallest is None or largest is None:
          print("No numbers were entered.")

        else:
                print("Smallest number:", smallest)
                print("Largest number:", largest)

