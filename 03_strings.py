# Strings #

my_string = 'Mi String'
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string +  " " + my_other_string)

my_new_line_string = 'Este es un String\ncon salto de linea'
print(my_new_line_string)

my_tab_string = '\tEsto es un string con tabulacion'
print(my_tab_string)

my_scape_string = 'Esto es un string con scape'
print(my_scape_string)

# Formateo 

name, surname, age = 'Dalia', 'Flores', 28
print('Mi nombre es {} {} Y mi edad es {}'.format(name, surname, age))
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age))
print(f'Mi nombre es {name} {surname} y mi edad es {age}') #la f sirve para formatear

# Desempaquetado de caracteres
language = 'Python'
a, b, c, d, e, f = language
print(a)
print(b)

# Division
language_slice = language [1:3]
print(language_slice)

language_slice = language [1:]
print(language_slice)

language_slice = language [-2]
print(language_slice)

language_slice = language [1:2:4]
print(language_slice)
# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count('t'))
print(language.isnumeric())
print('1'.isnumeric())
print(language.lower())
print(language.upper().isupper())
