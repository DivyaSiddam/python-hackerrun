if __name__ == '__main__':
    N = int(input().strip())  # Read number of commands
    my_list = []  # Initialize empty list

    # Process each command
    for _ in range(N):
        command = input().strip().split()  # Read and split command

        if command[0] == "insert":
            my_list.insert(int(command[1]), int(command[2]))  # Insert at index
        elif command[0] == "print":
            print(my_list)  # Print the list
        elif command[0] == "remove":
            my_list.remove(int(command[1]))  # Remove first occurrence
        elif command[0] == "append":
            my_list.append(int(command[1]))  # Append to list
        elif command[0] == "sort":
            my_list.sort()  # Sort list
        elif command[0] == "pop":
            my_list.pop()  # Remove last element
        elif command[0] == "reverse":
            my_list.reverse()  # Reverse list
