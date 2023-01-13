# Listas #

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))
print(type(my_list)) #class 'list'

my_other_list = [28, 1.60, "Dalia", "Flores"]
print(my_other_list)
# En una lista se pueden guardar diferentes tipos de datos
print(type(my_other_list)) #class 'list'


print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
#print(my_other_list[-5]) #IndexError: list index out of range
print(my_other_list[-4])
print(my_list.count(30)) #Contar el numero de repeticiones

age, height, name, surname = my_other_list
print(name)

name, height, age, surname, = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)

# Formas de insertar datos a una lista
my_other_list.append('MoureDev')
print(my_other_list)

my_other_list.insert(0, 'Blue')
print(my_other_list)

my_other_list[0] = 'Verde' #Cambiar de valor un elemento en la lista
print(my_other_list)

#Forma de remover datos de la lista
my_list.remove(30)
print(my_list)

my_list.pop() #Elimina el ultimo elemento de la lista
print(my_list)

print(my_list.pop(2)) #Remover un elemento segun su indice, retornando el mismo 
print(my_list)

del my_list[2] #Eliminar un elemento de la lista segun su indice
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort() # Ordenar de menor a mayor en caso de numeros
print(my_new_list)

my_list = 'Hola Python'
print(my_list)
print(type(my_list)) # Tipado dinamico

#Remove elimina un elemento del cual conocemos el valor(si se repite elimina el primero que encuentre), pop elimina el ultimo elemento, del elimina segun su indice, clear borra toda la lista
