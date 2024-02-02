S = input().strip()
T = input().strip()

count = 0
for i in range(len(S)-len(T)+1):
    if S[i:i+len(T)] == T:
        count += 1
print(count)


max_count = 0
i = 0
while i < len(S):
    if S[i:i+len(T)] == T:
        max_count += 1
        i += len(T)
    else:
        i += 1
print(max_count)
