data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# def calculate_structure_sum(data_structure):
#     numbers = 0
#     for data in data_structure:
#         if isinstance(data, list):
#             for i in data:
#                 if i == str(i):
#                     numbers += len(i)
#                 else:
#                     numbers += i
#         elif isinstance(data, dict):
#             for value in data.values():
#                 numbers += value
#             for key in data.keys():
#                 numbers += len(key)
#         elif isinstance(data, tuple):
#             ?
#             for item in data:
#                 if item == str(item):
#                     numbers += len(item)
#                 else:
#                     numbers += item
#         elif isinstance(data, str):
#             for i in data:
#                 numbers += len(i)
#         else:
#             return numbers

def calculate_structure_sum(data_structure):
    numbers = 0
    if isinstance(data_structure, int):
        numbers += data_structure
    elif isinstance(data_structure, list):
        for data in data_structure:
            numbers += calculate_structure_sum(data)
    elif isinstance(data_structure, dict):
        for value in data_structure.values():
            numbers += value
        for key in data_structure.keys():
            numbers += len(key)
    elif isinstance(data_structure, tuple):
        for data in data_structure:
            numbers += calculate_structure_sum(data)
    elif isinstance(data_structure, set):
        for data in data_structure:
            numbers += calculate_structure_sum(data)
    elif isinstance(data_structure, str):
        numbers += len(data_structure)
    return numbers

result = calculate_structure_sum(data_structure)
print(result)
