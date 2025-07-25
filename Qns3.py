# Exercise 3: Biography

# Asking the user to enter their details
# input() is used to get values from the user

name = input("Enter your full name: ")  # full name will work fine
hometown = input("Enter your hometown: ")
age_input = input("Enter your age: ")

# Trying to convert age to an integer to avoid text input like "twenty"
try:
    age = int(age_input)
except ValueError:
    # If the conversion fails, set a default age and give a warning
    age = 0
    print("Invalid age entered, setting age to 0.")

# Storing all values in a dictionary
bio = {
    "Name": name,
    "Hometown": hometown,
    "Age": age
}

# Printing all the values in one print statement, on separate lines
print(f"Name: {bio['Name']}\nHometown: {bio['Hometown']}\nAge: {bio['Age']}")
