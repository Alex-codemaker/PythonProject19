data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def data_structure_sum(data_structure):
    s = 0
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            s += data_structure_sum(key)
            s += data_structure_sum(value)
    elif isinstance(data_structure,(list,tuple, set)):
        for items in data_structure:
            s += data_structure_sum(items)
    elif isinstance(data_structure, ( int, float)):
        s += data_structure
    elif isinstance(data_structure, str):
        s += len(data_structure)
    return s
print(data_structure_sum(data_structure))













#calculate_structure_sum = 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + len('drum') + 8 + len('Hello') + 2 + len('Urban') + len ('Urban2') + 35
#result = calculate_structure_sum(data_structure)
#print(result)


