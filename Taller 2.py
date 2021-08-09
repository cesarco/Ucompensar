

print ("=============================================")
print ("=                                           =")
print ("=              MENU PRINCIPAL               =")
print ("=                                           =")
print ("=                                           =")
print ("=   1. Area del triangulo                   =")
print ("=   2. Coverción °F a °C                    =")
print ("=   3. Nota definitiva de un estudiante     =")
print ("=   4. Neto a cancelar de un producto       =")
print ("=                                           =")
print ("=============================================")


option=int(input('Digite una opción\n'))

if option==1:
    print('Programa que calcula el Area del triangulo')
    b = float(input('Digite la base del triangulo\n'))
    h = float(input('Digite la altura\n'))
    area=(b*h)/2
    print('El area del triangulo es:',area,'cm^2\n')

elif option==2:
    print('Programa que convierte °F a °C')
    f=float(input('Digite los °F a convertir\n'))
    c=(f-32)*5/9
    print('los ' ,f, '°F equivale a ',round(c,2),' °C')
    
elif option==3:
    print('Programa que calcula la nota defintiva de un estudiante')
    N1=float(input('Digite la primer nota\n'))
    N2=float(input('Digite la segunda nota\n'))
    N3=float(input('Digite la tercera nota\n'))
    DEF=(N1*0.2)+(N2*0.35)+(N3*0.45)
    print('La nota definitiva es',DEF)

elif option==4:
    print('Programa que calcula el Neto a  cancelar de un producto')
    v=float(input('Digite el valor del producto\n'))
    c=float(input('Digite la cantidad\n'))
    vt=(v*c)
    print('El valor total es: $',vt,'COP')
else:
    print('Opción no registrada')
    print('Fin del programa')
    
    
    

    
