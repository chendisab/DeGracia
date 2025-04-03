try:
    with open("students.txt", "r") as file:
        content = file.readlines()
    
    print("Displaying Student Information:")
    for line in content:
        print(line.strip())

except FileNotFoundError:
    print("Error: 'students.txt' could not be found. Please ensure the file is present.")
except Exception as error:
    print(f"An unexpected error occurred: {error}")

