#Variables

my_string_variable = 'My String Variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

#Concatenacion de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print('Este es un valor de:', my_bool_variable)

#Algunas funciones del sistema
print(len(my_string_variable))

#Variables en una sola linea
name, surname, alias, age = "Dalia", "Flores", "Yaya", 28
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# Inputs
"""
first_name = input('What is your name?: ')
age = input('How old are you?: ')

print(first_name)
print(age)
"""

# Cambiamos su tipo
first_name = 35
age = 'Brais'
print(first_name)
print(age)

# Forzamos el tipo
addres: str = "Mi direccion"
addres = 28
print(type(addres))