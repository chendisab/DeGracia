f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
years = input("Enter your age: ")

complete_name = f_name + " " + l_name
first_three = f_name[:3]

greeting = f"Hello, {first_three}! Welcome. You are {years} years old."

print("\nFull Name:", complete_name)
print("First Three Letters:", first_three)
print("Greeting:", greeting)
