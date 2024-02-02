N = int(input().strip())
fare_matrix = [list(map(float, input().strip().split())) for _ in range(N)]
M = int(input().strip())

for _ in range(M):
    start, end, ticket_type = input().strip().split()
    start, end = int(start) - 1, int(end) - 1

    if ticket_type == "A":
        if start < end:
            fare = fare_matrix[start][end]
        else:
            fare = fare_matrix[end][start]
    elif ticket_type == "C":
        if start > end:
            fare = fare_matrix[start][end]
        else:
            fare = fare_matrix[end][start]

    print(f"{fare:.1f}")
