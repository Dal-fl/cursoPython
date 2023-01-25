# Loops #

# While


my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: 
    print('Mi condicion es mayor o igual a 10')
    
print('La ejecucion continua')
    

while my_condition < 20:
    my_condition += 1
    if my_condition ==15:
        print('Mi condicion es 15, se detiene la ejecucion')
        break

    print(my_condition)

print('La ejecucion continua')

# For #

my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)

my_tuple = (30, 1.60, 'Dalia', 'Flores', 'Dalia')
for element in my_tuple:
    print(element)
    
my_set = {'Dalia', 'Flores', 28}
for element in my_set:
    print(element)

my_dict = {"Nombre":"Dalia", "Apellido":"Flores", "Edad":"28", 1:"Python"}
for element in my_dict:
    print(element)
    if element == 'Edad':
        break
else:
    print('El bucle for para dicts ha finalizado')