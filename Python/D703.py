N, cur = map(int, input().split())
arr = list(map(int, input().split()))
ptr = list(map(int, input().split()))

while cur != 0:
    print(arr[cur-1])
    cur = ptr[cur-1]

print("End")
