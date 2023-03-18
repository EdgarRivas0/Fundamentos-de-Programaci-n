print("---------------------------")
print("------¡Identificador!------")
print("---------------------------")

print("Menú de opciones")             #Menu que se imprime al iniciar el progrma
print("Presione 1 para identificar gentilicios")     #Opcion 1
print("Presione 2 para identificar animales")         #Opcion 2

opción = int(input("¿Cuál es la opción que desea seleccionar? \n"))  #Esta linea del codigo da inicio al programa

if opción == 1:                               #Aqui empieza la opcion uno si la variable es igual a uno de los elif o if se ejecutara lo planteado en cada linea
    print("Identificador de gentilicios\n")
    
    opcionhumano = str(input("¿Cuál es el gentilicio que desea identificar? "))
    
    if opcionhumano == "El Salvador":
        print("Su gentilicio es 'salvadoreño' ")
    elif opcionhumano == "Mexico":
        print("Su gentilicio es 'mexicano/a' ")
    elif opcionhumano == "Estados Unidos":
        print("Su gentilicio es 'estadounidense' ")
    elif opcionhumano == "Canada":
        print("Su gentilicio es 'canadiense' ")
    elif opcionhumano == "Inglaterra":
        print("Su gentilico es 'británico/a' ")
    elif opcionhumano == "Argentina":
        print("Su gentilicio es 'argentino/a' ")
    elif opcionhumano == "España":
        print("Su gentilicio es 'español/a' ")
    elif opcionhumano == "Chile":
        print("SU gentilicio es 'chileno/a' ")
    elif opcionhumano == "Australia":
        print("Su gentilicio es 'australiano/a' ")
    elif opcionhumano == "Italia":
        print("Su gentilicio es 'italiano/a' ")          #Aqui terminan los elif
    else:                                                 #La opcion else por si ningun dato introducido es igual
        print('Ese no esta en la base de datos \n')           
        
        
elif opción == 2:                                         #Aqui empieza la opcion identificador de Animales, si la variable introducida es igual a alguno de los if se desarrollara correctamente
    print("Identificador de tipo de animal")
    
    opcionanimal = str(input("¿Cuál es el tipo de animal que desea idetificar?"))        #Aqui introduce el nombre de un animal
    
    if opcionanimal == "Lobo":
        print("El tipo de animal es 'canino'")
    elif opcionanimal == "Tigre":
        print("El tipo de animal es 'felino'")
    elif opcionanimal == "Vaca":
        print("El tipo de animal es 'bobino'")
    elif opcionanimal == "Caballo":
        print("El tipo de animal es 'equino'")
    elif opcionanimal == "Oso":
        print("El tipo de animal es 'pantígrado'")
    elif opcionanimal == "Colibrí":
        print("El tipo de animal es 'ave'")
    elif opcionanimal == "Iguana":
        print("El tipo de animal es 'reptil'")
    elif opcionanimal == "Perro":
        print("El tipo de animal es 'canino'")
    elif opcionanimal == "Pingüino":
        print("El tipo de animal es 'ave'")
    elif opcionanimal == "León":
        print("El tipo de animal es 'felino'")      #Aqui terminan todas las opciones de if que habias
    else:                                          #Y el else por si la variable no cuadra con ningun if
        print("El animal ingresado no se puede identificar")
        
else:
    print("Opción no disponible")         #Este else es de el menu de inicio, si no introduce 1 o 2 que son las opciones, saltara este print para hacerle saber que no se puede desarrollar el programa
    
print("FIN\n")     #FIN