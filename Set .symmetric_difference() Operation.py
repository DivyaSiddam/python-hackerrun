# Read number of English subscribers
n = int(input())
english = set(map(int, input().split()))

# Read number of French subscribers
m = int(input())
french = set(map(int, input().split()))

# Students subscribed to only one newspaper (not both)
only_one = english.symmetric_difference(french)

# Output the count
print(len(only_one))
