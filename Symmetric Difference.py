# Read inputs
m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

# Compute symmetric difference
result = a.symmetric_difference(b)

# Print in ascending order
for num in sorted(result):
    print(num)
