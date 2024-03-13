def maximum_subarray_sum(diamonds):
    maxSoFar = 0
    maxEndingHere = 0

    for diamond in diamonds:
        maxEndingHere = maxEndingHere + diamond
        if maxEndingHere < 0:
            maxEndingHere = 0
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere

    return maxSoFar


N = int(input())
diamonds = list(map(int, input().split()))

result = maximum_subarray_sum(diamonds)
print(result)
