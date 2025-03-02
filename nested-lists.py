if __name__ == '__main__':
    students = []  # List to store student records

    # Read input
    for _ in range(int(input().strip())):
        name = input().strip()
        score = float(input().strip())
        students.append([name, score])  # Store name and score as a list

    # Extract unique scores and sort them
    scores = sorted(set(score for _, score in students))

    # Get the second lowest score
    second_lowest = scores[1]

    # Get names of students with the second lowest score
    result = sorted([name for name, score in students if score == second_lowest])

    # Print names alphabetically
    for name in result:
        print(name)
