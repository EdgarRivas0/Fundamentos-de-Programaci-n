print("*******************************************    Inicio del programa    *******************************************\n")
vali= True
while vali==True:
    num= int(input("ingrese la cantidad de datos a procesar "))
    if num > 0:
        vali=False
        posi=0
        nega=0
        nul=0
# Obtener la cantidad de números que se van a ingresar
while True:
    try:
        n = int(input("""===========================================
Ingrese la cantidad de números a clasificar
============================================\n"""))
        if n <= 0:
            print("""===========================================
Ingrese un número mayor a cero
===========================================""")
            continue
        break
    except ValueError:
        print("""===========================================
Ingrese un número válido
===========================================\n""")

        for i in range(num):
            valor = input("Ingrese un valor: ")
            if valor.isdigit():
                data=int(valor)
                if data > 0:
                    posi+=1
                elif data < 0:
                    nega+=1
                else:
                    nul+=1
            elif valor.isalpha():
                print("a ingresado una palabra ")
                for i in valor:
                    print(i)
            else:
                print("Probablemente esto es un signo")
        print(f"\nLa cantidad de numeros positivos es {posi}")
        print(f"\nLa cantidad de numeros negativos es {nega}")
        print(f"\nLa cantidad de numeros nulos es {nul}")
# Inicializar variables para contar los números
positivos = 0
negativos = 0
nulos = 0

# Obtener los números y clasificarlos por su tipo
for i in range(n):
    while True:
        try:
            num = int(input(f"Ingrese el número {i+1}: "))
            break
        except ValueError:
            print("Ingrese un número válido")
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        print("\nEl numero ingresado no es correcto intentalo nuevamente")
        nulos += 1

# Mostrar los resultados obtenidos que ingreso el usuario
print(f"La cantidad de números positivos es: {positivos}")
print(f"La cantidad de números negativos es: {negativos}")
print(f"La cantidad de números nulos es: {nulos}")

print(print("*******************************************    Fin del programa    *******************************************\n"))
# Mensaje donde indica la finalizaciond el programa
print("Programa finalizado")