# Read input
N, M = map(int, input().split())

# Upper part of the pattern
for i in range(1, N, 2):
    pattern = (".|." * i).center(M, "-")
    print(pattern)

# Center line with "WELCOME"
print("WELCOME".center(M, "-"))

# Lower part of the pattern
for i in range(N-2, 0, -2):
    pattern = (".|." * i).center(M, "-")
    print(pattern)
