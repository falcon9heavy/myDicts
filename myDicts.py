"""
Dictionaries.....:

This is an accumulation of examples using dictionaries
with the intent of educating python users

Key things to keep in mind first...

--> lists are ordered, dictionaries are not, they are arbitrary, tracked by keys, not indexes.
    no longer the case...
--> Assessed by KEYS, not offset postion or index
--> Heterogenous, variable length

Python Collections (Arrays)

There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered (3.7) and changeable. No duplicate members.

Also

    Anything which can be stored in a Python variable can be stored in a dictionary value.
    That includes mutable types including list and even dict — meaning you can nest dictionaries
    inside on another. In contrast keys must be hashable and immutable — the object hash must
    not change once calculated. This means list or dict objects cannot be used
    for dictionary keys, however a tuple is fine.

*Set items are unchangeable, but you can remove and/or add items whenever you like.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

"""

# in a literal definition, you have a bit more ability to define keys... see where num 4 works
# is accepted as a key in the literal

D = {
    'sue': ['qwerty','yuiop'],
    4 : 'sally',
     'bill': 12,
    'snuka': [1,2,3],
    tuple(['list','of','strings']):{ 1: 'jane', 2: 'terry'} # lists not hashable, tuples are, so...
    }
print(D)

# yet when working with constructor dict(), it don't
#D.update(5='mary')

#but you can single out a key in literal form to update or add
D[4]='barry'

E = dict(sue = ['qwerty','yuiop'])
E.update(sue='sally')
print(E)

print(f' I will always try to be {"snuka" in D} ') # in can find keys
print(f' Then again sometimes I\'ll be {12 in D})' ) # but not values

T = ('a','b','c')
print(T, type(T))
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7)
F = dict.fromkeys(tuple1,tuple2)
print(F)

#oh, I actually wanted to 'zip' those two tuples into a dictionary, item per item
F = dict(zip(tuple1,tuple2))
print(F)


tuple3 = (True, False, False)

tuplex = ("abc", 34, True, 40, "male", {'key1':'valueX'})
print(f' this is proof that {tuplex} is a tuple type({type(tuplex)}')


D = {'spam' : 2, 'ham' : 1, 'eggs' : 3}

print(D['eggs'], 
    len(D),          # how many pair?
    'ham' in D,      # is ham one of the keys
    1 in D,          # is 1 a key? and no it won't tell you if it's a value
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


population = {'Shanghai':17.8, 'Istanbul':13.3, 'Karachi':13.0, 'Mumbai':12.5}
for key in population:
	print("the population of {} is {}".format(key,population[key]))

print(
    list(population.items()),
    list(population.values()),
    list(population.keys()),
    population.get('Izzztanbul', 88) # this works like an true, else return other value=
    )

D = elements
D2 = {'toast':4, 'muffin':5}
D.update(D2)
print(D)
D3 = {'toast':99}
D.update(D3)
print(D)

print(D.pop('toast')) # pop out the toast for the value bitch!

L = list(population.values())
print(L, L.pop()) # or whatever you want...what's left
print(L.pop(0))

print(D)

# Question: go ahead and switch the keys and values in D
# first, can you force the change? dicts are supposed to be immutable
# so does that mean you can't swap out a key, lets see...
# {'hydro': 3, 'water': 6, 'chucky': 8, 'muffin': 5}
# change 'hydro' hydrant

D['hydrant'] = D['hydro']
del D['hydro']
print(D)

# or we can reverse that using pop()

D['hydro'] = D.pop('hydrant')
print("here is my dict", D) # were gonna reverse this list with zip

D_list_keys = list(D.keys())
D_list_values = list(D.values())

DD = dict(zip(D_list_values, D_list_keys))
print(DD)

