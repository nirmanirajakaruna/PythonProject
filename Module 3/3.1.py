length = int(input("Enter the length of the zander in centimeters: "))
limit = 42
if length < limit:
    shortage = limit - length
    print(f"Release the fish back in to the lake.The fish is {shortage} cm below the size limit.")
else:
    print("The zander meets the size limit.You can keep the fish")