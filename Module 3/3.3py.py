gender = input("Enter biological gender (male/female):").lower()
value = int(input("Enter hemoglobin value (g/l:"))
if gender == "female":
    if value <117:
        print("Hemoglobin value is low.")
    elif value > 155:
        print("Hemoglobin value is high.")
    else:
        print("Hemoglobin value is normal.")
elif gender == "male":
    if value <134:
        print("Hemoglobin value is low.")
    elif value > 167:
        print("Hemoglobin value is high.")
    else:
        print("Hemoglobin value is normal.")
else:
    print("Invalid gender entered.")