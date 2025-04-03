import json
import os

class StudentRecordManager:
    def __init__(self):

        self.records = []
        self.filename = None

    def load_file(self, filename):

        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.records = json.load(file)
            self.filename = filename
            print("File loaded successfully.")
        else:
            print("File not found.")

    def save_file(self):

        if self.filename:
            with open(self.filename, "w") as file:
                json.dump(self.records, file)
            print("File saved successfully.")
        else:
            print("No file is currently open. Use 'Save As' to specify a filename.")

    def save_as(self, filename):

        with open(filename, "w") as file:
            json.dump(self.records, file)
        self.filename = filename
        print("File saved successfully as", filename)

    def show_all_records(self):

        for record in self.records:
            print(record)

    def order_by_last_name(self):

        self.records.sort(key=lambda x: x[1][1])
        print("Records sorted by last name.")

    def order_by_grade(self):

        self.records.sort(key=lambda x: (x[2] * 0.6 + x[3] * 0.4), reverse=True)
        print("Records sorted by grade.")

    def show_student_record(self, student_id):

        record = next((r for r in self.records if r[0] == student_id), None)
        if record:
            print(record)
        else:
            print("Student record not found.")

    def add_record(self, student_id, first_name, last_name, class_standing, major_exam):

        if any(r[0] == student_id for r in self.records):
            print("Student ID already exists.")
            return
        self.records.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully.")

    def edit_record(self, student_id, first_name=None, last_name=None, class_standing=None, major_exam=None):

        for i, record in enumerate(self.records):
            if record[0] == student_id:

                new_record = (
                    student_id,
                    (first_name or record[1][0], last_name or record[1][1]),
                    class_standing if class_standing is not None else record[2],
                    major_exam if major_exam is not None else record[3]
                )
                self.records[i] = new_record
                print("Record updated successfully.")
                return
        print("Student ID not found.")

    def delete_record(self, student_id):

        self.records = [r for r in self.records if r[0] != student_id]
        print("Record deleted successfully.")

def main():
    manager = StudentRecordManager()

    while True:

        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            filename = input("Enter filename: ")
            manager.load_file(filename)
        elif choice == "2":
            manager.save_file()
        elif choice == "3":
            filename = input("Enter new filename: ")
            manager.save_as(filename)
        elif choice == "4":
            manager.show_all_records()
        elif choice == "5":
            manager.order_by_last_name()
        elif choice == "6":
            manager.order_by_grade()
        elif choice == "7":
            student_id = input("Enter Student ID: ")
            manager.show_student_record(student_id)
        elif choice == "8":

            student_id = input("Enter Student ID: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = float(input("Enter Class Standing Grade: "))
            major_exam = float(input("Enter Major Exam Grade: "))
            manager.add_record(student_id, first_name, last_name, class_standing, major_exam)
        elif choice == "9":

            student_id = input("Enter Student ID to Edit: ")
            first_name = input("Enter New First Name (leave blank to keep current): ") or None
            last_name = input("Enter New Last Name (leave blank to keep current): ") or None
            class_standing = input("Enter New Class Standing Grade (leave blank to keep current): ")
            major_exam = input("Enter New Major Exam Grade (leave blank to keep current): ")
            class_standing = float(class_standing) if class_standing else None
            major_exam = float(major_exam) if major_exam else None
            manager.edit_record(student_id, first_name, last_name, class_standing, major_exam)
        elif choice == "10":
            student_id = input("Enter Student ID to Delete: ")
            manager.delete_record(student_id)
        elif choice == "11":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()



python
Copy
Edit
import json
import os

class RecordManager:
    def __init__(self):
        self.records = []
        self.filename = None

    def open_file(self, file_name):
        if os.path.isfile(file_name):
            with open(file_name, "r") as file:
                self.records = json.load(file)
            self.filename = file_name
            print("File loaded successfully.")
        else:
            print("File not found.")

    def save_current_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                json.dump(self.records, file)
            print("File saved successfully.")
        else:
            print("No file opened. Use 'Save As' to choose a file.")

    def save_to_new_file(self, new_filename):
        with open(new_filename, "w") as file:
            json.dump(self.records, file)
        self.filename = new_filename
        print(f"File saved successfully as {new_filename}.")

    def display_all_records(self):
        for record in self.records:
            print(record)

    def sort_by_last_name(self):
        self.records.sort(key=lambda x: x[1][1])
        print("Records sorted by last name.")

    def sort_by_grade(self):
        self.records.sort(key=lambda x: (x[2] * 0.6 + x[3] * 0.4), reverse=True) 
        print("Records sorted by grade.")

    def find_record_by_id(self, student_id):
        record = next((r for r in self.records if r[0] == student_id), None)
        if record:
            print(record)
        else:
            print("Record not found.")

    def add_new_record(self, student_id, first_name, last_name, class_standing, major_exam):
        if any(r[0] == student_id for r in self.records):
            print("This student ID already exists.")
            return
        self.records.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully.")

    def update_record(self, student_id, first_name=None, last_name=None, class_standing=None, major_exam=None):
        for idx, record in enumerate(self.records):
            if record[0] == student_id:
                updated_record = (
                    student_id,
                    (first_name or record[1][0], last_name or record[1][1]),
                    class_standing if class_standing is not None else record[2],
                    major_exam if major_exam is not None else record[3]
                )
                self.records[idx] = updated_record
                print("Record updated successfully.")
                return
        print("Student record not found.")

    def remove_record(self, student_id):
        self.records = [r for r in self.records if r[0] != student_id]
        print("Record deleted successfully.")

def main():
    manager = RecordManager()

    while True:
        print("\nOptions Menu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. View All Student Records")
        print("5. Sort by Last Name")
        print("6. Sort by Grade")
        print("7. View Specific Student Record")
        print("8. Add a New Record")
        print("9. Edit an Existing Record")
        print("10. Delete a Record")
        print("11. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            file_name = input("Enter file name to load: ")
            manager.open_file(file_name)
        elif choice == "2":
            manager.save_current_file()
        elif choice == "3":
            new_filename = input("Enter new file name: ")
            manager.save_to_new_file(new_filename)
        elif choice == "4":
            manager.display_all_records()
        elif choice == "5":
            manager.sort_by_last_name()
        elif choice == "6":
            manager.sort_by_grade()
        elif choice == "7":
            student_id = input("Enter Student ID to view: ")
            manager.find_record_by_id(student_id)
        elif choice == "8":
            student_id = input("Enter Student ID: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = float(input("Enter Class Standing Grade: "))
            major_exam = float(input("Enter Major Exam Grade: "))
            manager.add_new_record(student_id, first_name, last_name, class_standing, major_exam)
        elif choice == "9":
            student_id = input("Enter Student ID to edit: ")
            first_name = input("Enter New First Name (leave blank to keep current): ") or None
            last_name = input("Enter New Last Name (leave blank to keep current): ") or None
            class_standing = input("Enter New Class Standing Grade (leave blank to keep current): ")
            major_exam = input("Enter New Major Exam Grade (leave blank to keep current): ")
            class_standing = float(class_standing) if class_standing else None
            major_exam = float(major_exam) if major_exam else None
            manager.update_record(student_id, first_name, last_name, class_standing, major_exam)
        elif choice == "10":
            student_id = input("Enter Student ID to delete: ")
            manager.remove_record(student_id)
        elif choice == "11":
            break  # Exit the program
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()