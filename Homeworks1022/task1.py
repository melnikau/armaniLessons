"""Найдите количество положительных элементов в данном списке"""

stack = [2, 4, 11, -67, 5, -9, 45, 5, -7]

counter_positive = 0

for el in stack:
    if el > 0:
        counter_positive += 1

print(counter_positive)
