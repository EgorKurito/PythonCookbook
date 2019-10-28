'''
Mapping Keys to Multiple Values in a Dictionary
Problem:
You want to make a dictionary that maps keys to more than one
value (a so-called “multidict”).
'''

# Use list if you want to preserve the insertion order of the items
from collections import defaultdict
d = {
    'a': [1, 2, 4],
    'b': [4, 5],
}

# Use a set if you want to eliminate duplicates
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}


d = defaultdict(list)
d['a'].append(1)

e = defaultdict(set)
e['a'].append(1)


# Dirty code
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

# Clean code
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
