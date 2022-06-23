"""
Dictionaries.....:

Key things to keep in mind first...

--> lists are ordered, dictionaries are not, they are arbitrary, tracked by keys, not indexes.
--> Assessed by KEYS, not offset postion or index
--> Heterogenous, variable length
--> Mutable mappings - as in no underlying order system, only mapped to data you create in keys

lists support access by index, like arrays
Dictionary support access by keys - or hash tables

Something to rememember: All built-in immutable objects, like tuples, are hashable while
mutable containers like lists and dictionaries are not hashable.
So if you want to use a list of values as a key, you need to make it hashable by
making it a tuple().

"""


# I almost feel bad for jamming all of this stuff in a dictionary
# A convoluted dictionary!

D = {
    'i can\'t type': ['querty','uyiop'],
     6: 12,
     'snuka': [1,2,3],
     4: { 1: 'jane', 2: 'terry'},
     tuple(['stop','go']):4, # have to hash the list with tuple function
     }

print(D.items()) # get KV pairs as tuples
print(D.keys(), D.values())

# the 'in' statement really only evaluates keys
print(f'Is the word "snuka" found in this dictionary? {"snuka" in D} ')

D = {'spam' : 2, 'ham' : 1, 'eggs' : 3}

print(
    D['eggs'],
    len(D),          # how many pair?
    'ham' in D,      # is ham one of the keys
    1 in D,          # is 1 a key? and no it won't tell you if its a value
    list(D.keys()),  # stick the keys in a list
    list(D.values()) # stick the values in a list
    )
D['ham'] = ['eddie', 'mike', 'stone', 'matt']
print(D)

del D['eggs']
D['brunch'] = 'Bacon'
print(D)

"""
DICTIONARIES : MUTABLE, UNORDERED, KVSTORE, IMMUTABLE KEY
"""

elements = {'hydro': 3, 'water': 6, 'chucky': 8}
print('chucky' in elements)
print(elements['chucky'])
print(elements.get('billy'))

"""
population = {'Shanghai':17.8, 'Istanbul':13.3, 'Karachi':13.0, 'Mumbai':12.5}
for key in population:
	print("the population of {} is {}".format(key,population[key]))

#print(
#    list(population.items()),
#    list(population.values()),
#    list(population.keys()),
#    population.get('Izzztanbul', 88) # this works like an true, else return other value=
#    )

D = elements
D2 = {'toast':4, 'muffin':5}
D.update(D2)
D3 = {'toast':99}
D.update(D3)
#print(D)

L = list(population.values())
#print(L, L.pop()) # or whatever you want...what's left
#print(L.pop(0))



# Question: go ahead and switch the keys and values in D
# first, can you force the change? dicts are supposed to be immutable
# so does that mean you can't swap out a key, lets see...
# {'hydro': 3, 'water': 6, 'chucky': 8, 'muffin': 5}
# change 'hydro' hydrant

D['hydrant'] = D['hydro']
del D['hydro']

# or we can reverse that using pop()

D['hydro'] = D.pop('hydrant')

D_list_keys = list(D.keys())
D_list_values = list(D.values())

DD = dict(zip(D_list_values, D_list_keys))
"""