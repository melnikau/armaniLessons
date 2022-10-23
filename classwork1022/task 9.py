stack = input().split()

dict1 = {}

for i in stack:
    if i not in dict1.keys():
        dict1[i] = 1
    else:
        dict1[i] += 1

max_value = max(dict1.values())

print(stack)

for key, value in sorted(dict1.items()):
    if key == max_value:
        print(value)

