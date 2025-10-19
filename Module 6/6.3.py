def gallons_to_liters(gallons):
    return gallons * 3.785

while True:
    g = float(input("Enter gallons(negative to stop): "))
    if g < 0:
        break
    print(g, "gallons =",gallons_to_liters(g), "liters")