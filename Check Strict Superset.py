# Read the main set A
A = set(map(int, input().split()))

# Read number of other sets
n = int(input())

# Check each set
is_strict_superset = True
for _ in range(n):
    other_set = set(map(int, input().split()))
    if not (A > other_set):  # strict superset check
        is_strict_superset = False
        break

# Print the result
print(is_strict_superset)
