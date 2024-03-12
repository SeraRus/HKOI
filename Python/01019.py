import heapq

def calculate_minimum_time(numbers):
    heap = []
    for num in numbers:
        heapq.heappush(heap, num)
    
    total_time = 0
    while len(heap) > 1:
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)
        
        new_num = num1 + num2
        total_time += new_num
        
        heapq.heappush(heap, new_num)
    
    return total_time

N = int(input())

numbers = []
for _ in range(N):
    num = int(input())
    numbers.append(num)

minimum_time = calculate_minimum_time(numbers)

print(minimum_time)
