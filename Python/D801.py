def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


N, Q = map(int, input().split())

arr = list(map(int, input().split()))

target = list(map(int, input().split(" ")))
for i in target:

    exists = binary_search(arr, i)
    if exists:
        print("Yes")
    else:
        print("No")
