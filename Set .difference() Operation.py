# Read the number of English subscribers
n = int(input())
english = set(map(int, input().split()))

# Read the number of French subscribers
m = int(input())
french = set(map(int, input().split()))

# Students who are only subscribed to English newspaper
only_english = english.difference(french)

# Output the count
print(len(only_english))
