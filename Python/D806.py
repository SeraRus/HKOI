import math


def merge_sort_(l):
    if len(l) > 1:
        mid = math.ceil(len(l)/2)
        left_half = l[:mid]
        right_half = l[mid:]

        merge_sort_(left_half)
        merge_sort_(right_half)

        i = j = k = 0
        print(left_half[0], left_half[-1], right_half[0], right_half[-1])
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                l[k] = left_half[i]
                i += 1
            else:
                l[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            l[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            l[k] = right_half[j]
            j += 1
            k += 1
    return l


merge_sort_(list(range(1, int(input())+1)))
