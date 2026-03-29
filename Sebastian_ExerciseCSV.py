# Program: Grades CSV Creator and Reader

import csv


# -----------------------------------------
# Function: create_grades_file
# Description: Allows instructor to input student data
# and writes it to grades.csv
# -----------------------------------------
def create_grades_file():
    # Ask how many students
    num_students = int(input("Enter number of students: "))

    # Open file in write mode
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loop through each student
        for i in range(num_students):
            print(f"\nStudent {i + 1}")

            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write row to CSV
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\ngrades.csv file created successfully!")


# -----------------------------------------
# Function: display_grades
# Description: Reads grades.csv and displays
# data in a formatted table
# -----------------------------------------
def display_grades():
    try:
        with open("grades.csv", "r") as file:
            reader = csv.reader(file)

            print("\nStudent Grades:\n")

            # Print each row formatted
            for row in reader:
                print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(
                    row[0], row[1], row[2], row[3], row[4]
                ))

    except FileNotFoundError:
        print("grades.csv file not found. Please create it first.")


# -----------------------------------------
# Main Function
# -----------------------------------------
def main():
    create_grades_file()
    display_grades()


# Run program
main()