stack = [1, 3, 5, 55, 2, 5]
dictionary = {}

for el in stack:
    if el not in dictionary.keys():
        dictionary[el] = 1
    else:
        dictionary[el] += 1

print(dictionary)
