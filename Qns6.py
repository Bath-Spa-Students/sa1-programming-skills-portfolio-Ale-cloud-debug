# Exercise 6: Brute Force Attack

# Setting the correct password
correct_password = "12345"

# Variable to keep track of user input
entered_password = ""

# Keep asking until the correct password is typed
while entered_password != correct_password:
    entered_password = input("Please enter the password: ")

# If loop ends, that means password was correct
print("Access granted! ✅ Welcome!")
