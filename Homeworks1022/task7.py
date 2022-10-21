"""Дан список чисел.
Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет - не выводите ничего.
Если таких пар соседей несколько - выведите первую пару. """
import math

stack = [2, -4, 11, 0, -67, 0, 5, 45, -9, -45, 5, -7, 0, -1, -3]
i = 0

while i < len(stack) - 1:
    if (math.fabs(stack[i]) == stack[i] and math.fabs(stack[i + 1]) == stack[i + 1]) or (
            math.fabs(stack[i]) != stack[i] and math.fabs(stack[i + 1]) != stack[i + 1]):
        print(stack[i], stack[i + 1])
    i += 1
