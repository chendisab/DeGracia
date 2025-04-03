first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

full_name = first_name + " " + last_name

upper_case_name = full_name.upper()
lower_case_name = full_name.lower()

name_length = len(full_name)

print("\nComplete Name:", full_name)
print("Complete Name (Uppercase):", upper_case_name)
print("Complete Name (Lowercase):", lower_case_name)
print("Number of characters in the full name:", name_length)
