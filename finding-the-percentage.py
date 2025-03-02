if __name__ == '__main__':
    n = int(input().strip())  # Read number of students
    student_marks = {}  # Dictionary to store student marks

    # Read student records
    for _ in range(n):
        name, *line = input().split()  # Read name and scores
        scores = list(map(float, line))  # Convert scores to float
        student_marks[name] = scores  # Store in dictionary

    query_name = input().strip()  # Read the name to be queried

    # Compute the average and print with 2 decimal places
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average:.2f}")
