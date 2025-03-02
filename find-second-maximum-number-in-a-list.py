if __name__ == '__main__':
    n = int(input().strip())  # Read the number of scores
    arr = list(map(int, input().split()))  # Read and convert input to a list of integers

    # Remove duplicates by converting to a set and then sort in descending order
    unique_scores = sorted(set(arr), reverse=True)

    # The second highest score is at index 1 after sorting in descending order
    print(unique_scores[1])
