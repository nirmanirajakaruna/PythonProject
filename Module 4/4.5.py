correct_username = "python"
correct_password = "rules"
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("welcome")
        break
    else:
        attempts += 1
        print("Incorrect username or password, try again.")
else:
    print("Access denied")