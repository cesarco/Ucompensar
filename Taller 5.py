print('-------------------------------------------')
print('|                                         |')
print('|            MENU PRINCIPAL               |')
print('|  1. Numero a la palabra                 |')
print('|  2. Palabra a número                    |')
print('-------------------------------------------')

opc=int(input('Digite una opción\n'))
if opc==1:
    print('Programa que convierte un número (1..3) en palabra')
    Num=int(input('Digite un numero a convertir\n'))
    if Num==1:
        print('El número digitado es Uno\n')
    elif Num==2:
        print('El número digitado es Dos\n')
    elif Num==3:
        print('El número digitado es Tres\n')
    else:
        print('Este número no se encuentra registrado\n')
elif opc==2:
    print('Programa que convierte una palabra en número(1..3)')
    Num1=input('Cual es la palabra que desea convertir\n')
    if Num1=='Uno':
        print('El número es: 1\n')
    elif Num1=='Dos':
        print('El número es: 2\n')
    elif Num1=='Tres':
        print('El número es: 3 \n')
    else:
        print('La palabra no se encuentra registrada')
else:
    print('opcion no registrada')
    print('fin del programa')
