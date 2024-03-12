#單行輸入轉換列表
list = list(map(int, input().split()))

#多行輸入轉換二維列表
matrix = [list(map(int, input().split())) for _ in range(int(input()))]

#歸併排序
def merge_sort(blist):

    def merge_sort_(alist):
        if len(alist) > 1:
            mid = len(alist) // 2
            left_half = alist[:mid]
            right_half = alist[mid:]

            merge_sort_(left_half)
            merge_sort_(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    alist[k] = left_half[i]
                    i += 1
                else:
                    alist[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                alist[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                alist[k] = right_half[j]
                j += 1
                k += 1
        return alist

    blist = merge_sort_(blist)
    return blist

#選擇排序
def selection_sort(alist):
    listed = []
    for _ in range(len(alist)):
        min_num = 0
        for u in range(len(alist)):
            if alist[u] < alist[min_num]:
                min_num = u
        listed.append(alist.pop(min_num))
    return listed
