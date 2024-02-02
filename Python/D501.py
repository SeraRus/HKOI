with open('account.txt', 'r') as f:
    n = int(f.readline())
    balance = 0
    for i in range(n):
        transaction = int(f.readline())
        balance += transaction
    print(balance)
