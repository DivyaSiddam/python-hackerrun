# Create an empty set
country_set = set()

# Read the number of stamps
n = int(input())

# Read each country and add to the set
for _ in range(n):
    country = input()
    country_set.add(country)

# Output the number of distinct country stamps
print(len(country_set))
