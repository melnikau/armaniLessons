dictionary = {}
for _ in range(int(input())):
    name, ball = input().split()

    if name not in dictionary.keys():
        dictionary[name] = int(ball)
    else:
        dictionary[name] += int(ball)

for key, value in sorted(dictionary.items()):
    print(key, value)