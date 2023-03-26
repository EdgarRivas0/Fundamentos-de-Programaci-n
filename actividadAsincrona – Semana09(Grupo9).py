print('******************************************************************\n')
print('                  Programa de Datos almacenados\n                  ')
print('******************************************************************\n')

#nombre apellidos edad y sexo y mostrarlos al final
print('****************** Favor de ingresar sus datos ******************')
Nombre=  input(" Ingrese sus dos nombres \n ")        #Esta variable recoge el/los nombre/s del usuario
Apellido= input(' Ingrse su apellido \n')             # Esta variable recoge el/los apellido/s 
Sexo=input(' Ingrese su sexo\n  m o f ')  #Esta variable guarda el sexo de la persona
Edad=  int(input(' Ingrese su edad\n '))               #Esta variable guarda la edad del usuario

if Sexo =="m" :   
    Sexo="masculino "              #if para el sexo masculino
    if Edad <= 2:         #esta parte del if es para determinar en que etapa de su vida se encuentra segun su edad
        print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
        print('Etapa de Bebé')
    elif Edad>= 3 and Edad <= 5:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de infancia')
    
    elif Edad>= 6 and Edad <= 11:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de niñes')
    elif Edad>= 12 and Edad <= 18:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de adolescencia ')  
    elif Edad>= 19 and Edad <= 26:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de juventud ')  
    elif Edad>= 27 and Edad <= 40:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de adultez joven ')  
    elif Edad>= 41 and Edad <= 55:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de adultez ')  
    elif Edad>= 56 and Edad <= 65:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de persona mayor')  
    elif Edad >= 66:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de vejez ')  

elif Sexo =="f":
    sexo= 'femenino'

    if Edad <= 2:         #esta parte del if es para determinar en que etapa de su vida se encuentra segun su edad
        print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
        print('Etapa de Bebé')
    elif Edad>= 3 and Edad <= 5:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de infancia')
    
    elif Edad>= 6 and Edad <= 11:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de niñes')
    elif Edad>= 12 and Edad <= 18:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de adolescencia ')  
    elif Edad>= 19 and Edad <= 26:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de juventud ')  
    elif Edad>= 27 and Edad <= 40:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de adultez joven ')  
    elif Edad>= 41 and Edad <= 55:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de adultez ')  
    elif Edad>= 56 and Edad <= 65:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de persona mayor')  
    elif Edad >= 66:
         print ('resultados, {} {} {} {}'.format(Nombre, Apellido, Sexo, Edad) )
         print('Etapa de vejez ')  
    
else: print('Sexo no ingresado')

if Edad % 2 ==0:
    print('La edad es numero par')
else: print('La edad es numero impar ')