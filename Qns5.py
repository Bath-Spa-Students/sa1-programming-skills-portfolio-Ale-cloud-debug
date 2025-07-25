# Exercise 5: Days of the Month

# Making a dictionary to store number of days in each month
month_days = {
    1: 31,
    2: 28,  # Will change this to 29 later if it's a leap year
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Asking user for month number
month_input = input("Enter the month number (1 to 12): ")

# Checking if input is a digit and a valid month
if month_input.isdigit():
    month = int(month_input)

    if 1 <= month <= 12:
        # Check if the month is February (2)
        if month == 2:
            leap_input = input("Is it a leap year? (yes/no): ")
            if leap_input.strip().lower() == "yes":
                print("February has 29 days.")
            else:
                print("February has 28 days.")
        else:
            print(f"The month has {month_days[month]} days.")
    else:
        print("That’s not a valid month number 🤔 (1 to 12 only please)")
else:
    print("Please enter a number, not text 😅")
