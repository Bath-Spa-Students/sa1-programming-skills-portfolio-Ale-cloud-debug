# Exercise 8: Simple Search

# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask the user what name to search for
search_name = input("Enter the name you want to search for: ")

# Check if the name is in the list
if search_name in names:
    print(f"Yes! {search_name} is in the list. ✅")
else:
    print(f"Oops! {search_name} is not in the list. ❌")
