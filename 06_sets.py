# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un dict

my_other_set = {'Dalia', 'Flores', 28}
print(type(my_other_set))

print(len(my_other_set))

# print(my_other_set[0])  TypeError: 'set' object is not subscriptable

my_other_set.add('Nyssa')
print(my_other_set) # Un set no es una estructura ordenada
my_other_set.add('Nyssa')
print(my_other_set) # Un set no admite repetidos

print('Dalia' in my_other_set)
print('Dali' in my_other_set) # Consultar la existencia de un elemento en un set

my_other_set.remove('Dalia')
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {'Dalia', 'Flores', 28}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'Python', 'Java', 'C++'}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({'C++', 'SQL'}))

print(my_new_set.union({'MySQL', 'MongoDB'}))

print(my_new_set.difference(my_set))
