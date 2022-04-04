cook = []
score = 0
for i in range(5):
    a  = list(map(int, input().split()))
    score = sum(a)
    cook.append(score)
print(cook.index(max(cook)) + 1, max(cook))