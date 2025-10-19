names = set()

while True:
    name = input("Enter a name (empty to stop): ")
    if name == "":
        break
    if name in names:
        print("Exisiting name")
    else:
        print("New name")
        names.add(name)

print("\nAll names entered:")
for n in names:
    print(n)