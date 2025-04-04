# Read number of English newspaper subscribers
n = int(input())
english = set(map(int, input().split()))

# Read number of French newspaper subscribers
m = int(input())
french = set(map(int, input().split()))

# Union of both sets
total = english.union(french)

# Print the total number of unique subscribers
print(len(total))
