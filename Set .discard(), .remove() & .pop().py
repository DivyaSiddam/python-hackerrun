# Read initial set size
n = int(input())

# Read set elements and convert to integers
s = set(map(int, input().split()))

# Read number of commands
N = int(input())

# Execute commands
for _ in range(N):
    command = input().split()

    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

# Print the sum of the remaining elements
print(sum(s))
