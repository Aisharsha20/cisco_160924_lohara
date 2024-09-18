names_list = input('Enter at least 5 integers separated by spaces: ').split()
names_list = [int(num) for num in names_list]
names_tuple = tuple(names_list)
names_set = set(names_tuple)
names_fset = frozenset(names_set)

# Dictionary comprehension: mapping the number to its string length
names_dict = {name: len(str(name)) for name in names_fset}

# Printing the results
print(f'Original list: {names_list}')
print(f'Set (no duplicates): {names_set}')
print(f'Frozen Set: {names_fset}')
print(f'Dictionary of number lengths: {names_dict}')
