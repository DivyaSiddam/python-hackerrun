if __name__ == '__main__':
    n = int(input().strip())  # Read the number of elements
    integer_list = tuple(map(int, input().split()))  # Convert input to a tuple of integers
    print(hash(integer_list))  # Print the hash of the tuple
