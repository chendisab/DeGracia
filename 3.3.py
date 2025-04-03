last_name = input("Please enter your last name: ")
first_name = input("Please enter your first name: ")
age = input("Please enter your age: ")
contact_number = input("Please enter your contact number: ")
course = input("Please enter your course: ")

student_info = "Last Name: " + last_name + "\nFirst Name: " + first_name + "\nAge: " + age + "\nContact Number: " + contact_number + "\nCourse: " + course + "\n\n"

with open("students.txt", "a") as file:
    file.write(student_info)

print("The student's information has been successfully saved to 'students.txt'.")
