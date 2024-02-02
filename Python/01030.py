class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def josephus_survivor(n):

    head = Node(1)
    prev = head
    for i in range(2, n+1):
        new_node = Node(i)
        prev.next = new_node
        prev = new_node
    prev.next = head


    result = []
    current = head
    while current.next != current:
        next_soldier = current.next
        result.append(next_soldier.value)
        current.next = next_soldier.next
        current = next_soldier.next


    return result, current.value


N = int(input())


execution_list, survivor = josephus_survivor(N)
print(" ".join(map(str, execution_list)))
print(survivor)
