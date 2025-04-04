# Read input
K = int(input())
room_list = list(map(int, input().split()))

# Apply the formula
unique_rooms = set(room_list)
captain_room = (K * sum(unique_rooms) - sum(room_list)) // (K - 1)

# Output the result
print(captain_room)
