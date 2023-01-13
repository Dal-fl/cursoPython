# Tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (30, 1.60, 'Dalia', 'Flores', 'Dalia')
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('Dalia'))
print(my_tuple.index('Flores'))

# my_tuple[1] = 1.65
# print(my_tuple) # TypeError: 'tuple' object does not support item assignment

print(my_tuple + my_other_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

# Convertir una tupla en una lista
my_tuple = list(my_tuple)
print(type(my_tuple))


#Asi se puede modificar
my_tuple[4] = 'MoureDev'
my_tuple.insert(1, 'Blue')
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Borrar una tupla
#del my_tuple  #NameError: name 'my_tuple' is not defined
print(my_tuple)