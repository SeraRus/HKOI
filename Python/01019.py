import heapq
n = int(input())
d = []
for _ in range(n):
    d.append(int(input()))
heapq.heapify(d)
cnt = 0
for _ in range(n - 1):
    n1 = heapq.heappop(d)
    n2 = heapq.heappop(d)
    acc = n1 + n2
    cnt += acc
    heapq.heappush(d, acc)
print(cnt)
