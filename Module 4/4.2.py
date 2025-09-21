def inches_to_cm():
    while True:
        inches = float(input("Enter the length in inches (negative number to quit): "))
        if inches < 0:
            print("program ended.")
            break
        cm = inches * 2.54
        print(f"{inches} inches = {cm:2f} cm")