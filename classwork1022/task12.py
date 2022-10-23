stack = [1, 3, 5, 55, 2, 5]
i = 0
while i < len(stack) - 1:
    stack[i] = stack[i + 1]
    i += 1

print(stack)

