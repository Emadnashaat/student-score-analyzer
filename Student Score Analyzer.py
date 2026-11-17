def get_students_number():
    """
    Ask the user to enter the number of students.
    Validates that the input is a positive integer.

    Parameters: None

    Returns: 
       int: The valid number of students.    
    """

    while True:
        try:
            number_of_students = int(input("Enter number of students: "))
            if number_of_students > 0:
                return number_of_students
            else:
                print("Enter a positive number")
        except ValueError:
            print("Invalid input")

def get_student_name(student_records):
    """
    Prompt the user to enter a student's name and validate the input.

    Ensures that the name is not empty, contains only letters and spaces,
    and does not already exist in the student records.

    Args:
        student_records (dict): A dictionary containing existing student names and their scores.

    Returns:
        str: The validated and normalized student name.
    """
    while True:
        student_name = input("Enter student name: ").strip().lower()
        if not student_name:
            print("Student name cannot be empty.")
            continue
        if not student_name.replace(" ","").isalpha():
            print("Name must contain letters and spaces only.")
            continue
        if student_name in student_records:
            print("This student already exists. Please enter a different name.")
            continue
        return student_name

def get_student_score(student_name):
    """
    Prompt the user to enter a student's score and validate the input.

    Ensures that the score is an integer between 0 and 100.

    Args:
        student_name (str): The name of the student.

    Returns:
        int: The validated student score.
    """

    while True:
        try:
            score = int(input(f"Enter {student_name}'s score: "))
            if 0<= score <=100:
                return score
            else:
                print("Score must be between 0 and 100")
        except ValueError:
            print("Please enter a valid number")

def calculate_average(student_records):
    """
    Calculate the average score of all students.

    Args:
        student_records (dict): A dictionary containing student names and their scores.

    Returns:
        float: The average score of all students.
    """

    if not student_records:
        return 0
    average = sum(student_records.values()) / len(student_records)
    return average
    
def get_highest_score(student_records):
    """
    Get the names of students who achieved the highest score.

    Args:
        student_records (dict): A dictionary containing student names
                                and their scores.

    Returns:
        tuple: A tuple containing:
            - list: Names of students with the highest score.
            - int or None: The highest score, or None if no records exist.
    """

    if not student_records:
        return [],None
    top_student = []
    highest_score = max(student_records.values())
    for name, score in student_records.items():
        if score == highest_score:
            top_student.append(name)
    return top_student, highest_score

def get_lowest_score(student_records):
    """
    Get the names of students who achieved the lowest score.

    Args:
        student_records (dict): A dictionary containing student names
                                and their scores.

    Returns:
        tuple: A tuple containing:
            - list: Names of students with the lowest score.
            - int or None: The lowest score, or None if no records exist.
    """

    if not student_records:
        return [],None
    lowest_student = []
    lowest_score = min(student_records.values())
    for name, score in student_records.items():
        if score == lowest_score:
            lowest_student.append(name)
    return lowest_student, lowest_score

def get_student_ranking(student_records):
    """
    Rank students based on their scores and assign a grade to each student.

    Args:
        student_records (dict): A dictionary containing student names
                                and their scores.

    Returns:
        list: A list containing the ranked students with their scores
              and grades. Returns an empty list if no student records
              are available.
    """
    if not student_records:
        return []
    ranked_students = sorted(
    student_records.items(),
    key=lambda item:item[1],
    reverse=True
    )
    ranked_results = []
    for rank, student in enumerate(ranked_students, start=1):
        name, score = student
        if score >=90:
            grade= "Excellent"
        elif score >=80:
            grade = "Very Good"
        elif score >=70:
            grade = "Good"
        elif score >= 50:
            grade = "Pass"
        else:
            grade= "Fail"
        ranked_results.append(f"{rank}. {name} - {score} - {grade}")
    return ranked_results

def display_report(student_records):
    """
    Display a complete report of student scores and performance.

    Args:
        student_records (dict): A dictionary containing student names
                                and their scores.

    Returns:
        None: Prints the average score, highest and lowest scores,
              top and lowest students, and the student ranking.
              Displays a message if no student records are available.
    """
    if not student_records:
        print("No student records available.")
        return
    average = calculate_average(student_records)
    top_student , highest_score =get_highest_score(student_records)
    lowest_student , lowest_score = get_lowest_score(student_records)
    
    ranked_results = get_student_ranking(student_records)

    print("\n========== Student Report ==========")
    print(f"Average Score: {average:.2f}")
    print(f"Highest Score: {highest_score}")
    print(f"Top Students: {', '.join(top_student)}")
    print(f"Lowest Score: {lowest_score}")
    print(f"Lowest Students: {', '.join(lowest_student)}")
    print("\nStudent Ranking:")
    for student in ranked_results:
        print(student)
    print("====================================")


def main():
    number_of_students = get_students_number()
    student_records ={}
    for i in range(number_of_students):
        print(f"\nStudent {i + 1}")
        student_name = get_student_name(student_records)
        student_score = get_student_score(student_name)
        student_records[student_name]=student_score
    display_report(student_records)


if __name__ == "__main__":
     main()





