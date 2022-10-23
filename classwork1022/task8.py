dicty = {}
for i in range(int(input())):
    name, ball = input().split()
    for j in name:
        dicty[name] = ball
for key, value in sorted(dicty.items()):
        print(key, value)