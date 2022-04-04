n = int(input())
vote = input()

if 1 <= n <= 15:
    if n == len(vote):
        a = vote.count('A')
        b = vote.count('B')
        if a == b:
            print("Tie")
        elif a > b:
            print("A")
        elif a < b:
            print("B")