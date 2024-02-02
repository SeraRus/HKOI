def bubble_sort(arr, direction):
    swap_count = 0
    n = len(arr)

    if direction == 0:
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap_count += 1
    elif direction == 1:
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap_count += 1

    return swap_count, arr

N, A = map(int, input().split())
arr = list(map(int, input().split()))

swap_count, sorted_arr = bubble_sort(arr, A)

print(swap_count)
print(' '.join(map(str, sorted_arr)))
