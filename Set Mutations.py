# Read initial set size and elements
n = int(input())
A = set(map(int, input().split()))

# Read number of operations
N = int(input())

# Perform each operation
for _ in range(N):
    op_name, _ = input().split()
    other_set = set(map(int, input().split()))
    
    # Apply mutation operation using getattr
    getattr(A, op_name)(other_set)

# Print the sum of the final mutated set
print(sum(A))
