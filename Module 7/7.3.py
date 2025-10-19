airports = {}

while True:
    choice = input("\nEnter '1' to add, '2' to find, '3' to quit: ")
    if choice == "1":
        code = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[code] = name
        print("airport added!")

    elif choice == "2":
        code = input("Enter ICAO code: ")
        if code in airports:
            print("Airport name:",airports[code])
        else:
            print("Not found!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")