# Read number of English newspaper subscribers
n = int(input())
english = set(map(int, input().split()))

# Read number of French newspaper subscribers
m = int(input())
french = set(map(int, input().split()))

# Find students who subscribed to both
both = english.intersection(french)

# Output the count
print(len(both))
