# Dictionaries

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Dalia", "Apellido":"Flores", "Edad":"28", 1:"Python"}

my_dict = {
    "Nombre":"Dalia", 
    "Apellido":"Flores", 
    "Edad":"28", 
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.60
    }

print(my_dict)
print(my_other_dict)

print(my_dict["Nombre"])
print(my_dict["Lenguajes"])

#Cambiar el valor de un elemento
my_dict["Nombre"] = "Claritza"
print(my_dict["Nombre"])

#Acceder a un valor numerico
print(my_dict[1])

#Agregar un nuevo campo al diccionario
my_dict["calle"] = "Pradera Bonita"
print(my_dict)

#Eliminar un elemento del diccionario
del my_dict["calle"]
print(my_dict)

#Comprobar la existencia de un elemento 
print("Flores" in my_dict)
print("Apellido" in my_dict)

#Acceder al valor de un elemento
print(my_dict["Apellido"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]


my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
print(type(my_new_dict))
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict.values()))
print(tuple(my_new_dict.values()))
print(set(my_new_dict))


