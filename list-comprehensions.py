# Taking input values
x = int(input().strip())
y = int(input().strip())
z = int(input().strip())
n = int(input().strip())

# List comprehension to generate coordinates
result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

# Printing the result
print(result)
