#Enteros
#Multiplicaccion
Termino1=int(input("Ingrese un digito, para multiplicar "))
Termino2=int(input("Ingrese otro termino "))
Termino3=int(input("Ingrese un tercer termino "))          #Se le da la oportunidad de digitar los datos que gusta
Multiplicacion=str(Termino1*Termino2*Termino3)
print("El resultado de la multiplicacion es " + Multiplicacion)   

#Division
Termino=int(input("Ingrese un numero para una razon "))
TERmino=int(input("Ingrese un segundo digito para una division entera "))
Division= (int (Termino)//int (TERmino))       
print("El resultado de la division es " + str(Division))

SUMATOTAL= (int (Multiplicacion) + int (Division))    #Se suman solo las respuestas de cada desarollo
print("Sumando todos los datos ingresados la respuesta es " + str( SUMATOTAL))


#FLOAT 
#EXPONENCIAL
TERMINO = float(input("Ingrese el numero que desee elevar "))
Indice = float(input("Introduzca el indice para elevar su termino "))
Exponencia = (float(TERMINO) ** float(Indice))  #Aqui se eleva su numero por el otro que digito
print ("Su numero elevado es " + str(Exponencia))

TERMINO1 = float(input("Ingrese el numero que desee elevar "))
IndicE = float(input("Introduzca el indice para elevar su termino "))
ExponenciA = (float(TERMINO1) ** float (IndicE))
print ("Su numero elevado es " + str( ExponenciA))   #Aqui el otro ejemplo

#MODULO
Numerador = float(input("Ingresa un digito dividendo "))
Denominador= float(input("Ingrese el dato de un divisor "))  #Aqui con modulo lo unico que da total el residuo de la division
DIvion = (float (Numerador)%float(Denominador))
print("El valor del modulo " + str(DIvion))

Numerador2 = float(input("Ingresa un digito dividendo "))
Denominador2= float(input("Ingrese el dato de un divisor "))
DIvion2 = (float (Numerador2)%float (Denominador2))       #otro ejemplo del residuo de la division
print("El valor del modulo es " + str(DIvion2))

RESTA= str(Numerador-Numerador2-Denominador-Denominador2)
print("La resta de los valores float es " + RESTA)
Totaldivision = (float(RESTA) / float (SUMATOTAL))     #aqui se divide la resta de todos los datos de float entre la suma de todos los datos int
print("La division de la resta entre la suma es "+ str(Totaldivision))

#COMPLEJOS 
VARIABLESCOMPLEJAS = complex(4j)
VARIABLESCOMPLEJAS+=complex(5j)   #se plantearan todos los numeros complejos de un solo
VARIABLESCOMPLEJAS+= complex(7j)
VARIABLESCOMPLEJAS +=complex (9j)


#CARACTER
Lisandro= str("uva")
Marbelly= str("Fresa")
Fatima= str ("higo")   
Xavier= str("Zapote")
Edgar=str("Sandia")


#BOOLEANOS
x=str(input("Escriba el nombre de una fruta: "))
bool(x)
if x == (Lisandro):
    print("Lisandro, La fruta es")
    print(True)

if x == (Marbelly):
    print("Marbelly La fruta es")
    print(True)

if x == (Fatima):
    print(" Fatima , La fruta es")
    print(True) 

if x == (Xavier):
    print("Xavier , La fruta es")
    print(True)  

if x == (Edgar):
    print("Edgar, La fruta es")
    print(True)  


else: 
  (print(" La fruta no coincide con nadie " + str(False) ))
  

print("Fin del trabajo :) ")