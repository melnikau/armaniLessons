"""Дан список числел.  Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
Если наибольших элементов несколько, выведите индекс первого из них """

stack = [2, 4, 11, -67, 5, 45, -9, 45, 5, -7, -1]
i = 0
max_el = 0
index_el = 0

while i < (len(stack)-1):
    if stack[i] > max_el:
        max_el = stack[i]
        index_el = i
    i += 1

print(max_el, index_el)
