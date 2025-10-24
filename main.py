# main.py
# A Python program to calculate student grades

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("Welcome to the Student Grade Calculator!")
    student_name = input("Enter student name: ")
    try:
        score = float(input("Enter student score (0-100): "))
        if score < 0 or score > 100:
            print("Invalid score. Must be between 0 and 100.")
            return
    except ValueError:
        print("Invalid input. Enter a number.")
        return

    grade = calculate_grade(score)
    print(f"{student_name} has achieved grade: {grade}")

if __name__ == "__main__":
    main()
# ToDo: implement input validation
# in progress
