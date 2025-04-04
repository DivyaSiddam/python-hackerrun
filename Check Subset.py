# Read number of test cases
T = int(input())

for _ in range(T):
    len_A = int(input())
    A = set(map(int, input().split()))
    
    len_B = int(input())
    B = set(map(int, input().split()))
    
    # Check if A is a subset of B
    print(A.issubset(B))
