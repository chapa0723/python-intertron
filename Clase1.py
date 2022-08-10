#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("¡Hola Mundo!")

#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
cadena = "¡Hola Mundo!"
print("\n" + cadena)

#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
nombre = input("¿Cual es tu nombre?: ")
print("\n¡Hola " + nombre + "!")


#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética  (2*2) * 4 / (5-1)
print("\n" + str((2*2)*4/(5-1)))


#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas = int(input("¿Cuantas horas trabajaste?: "))
coste = int(input("¿Cuanto costa la hora?: "))
print("\n La paga correspondiente: " + str(horas * coste))


#Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta . La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
m = int (input ('\n Ingresa el valor: '))
suma = 0
for i in range (m+1):
    suma+=i
print ('\n Valor de la suma: ', (suma))

"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de 
masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa 
corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos 
decimales."""
peso = float(input("¿Cuál es tu peso (en kg)?: "))
estatura = float(input("¿Cuál es tu estatura (en metros)?: "))
imc = peso / (estatura * estatura)
print("\n Tu índice de masa corporal es: " + str(round(imc,2)))


"""Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre 
<m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el 
usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente."""
n = int(input("¿Cuál es el primer número?: "))
m = int(input("¿Cuál es el segundo número?: "))
c = n // m
r = n % m
print("\n El cociente es: " + str(c) + " y el resto es: " + str(r))


"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número 
de años, y muestre por pantalla el capital obtenido en la inversión."""
capital = float(input("¿Cuánto quieres invertir?: "))
interes = float(input("¿Cuál es el interés anual?: "))
años = int(input("¿Cuántos años quieres?: "))
capital_final = capital * (1 + interes / 100) ** años
print("\n El capital final es: " + str(capital_final))


"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta 
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el 
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y 
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el 
último pedido y calcule el peso total del paquete que será enviado."""
payasos = int(input("¿Cuántos payasos?: "))
muñecas = int(input("¿Cuántas muñecas?: "))
peso_payasos = payasos * 112
peso_muñecas = muñecas * 75
peso_total = peso_payasos + peso_muñecas
print("\n El peso total del paquete es: " + str(peso_total))

"""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular 
y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear 
cada cantidad a dos decimales. """
capital = float(input("¿Cuánto quieres invertir?: "))
interes = 4.0
capital_1 = capital * (1 + interes / 100)
print("\n El capital final del primer año es: " + str(round(capital_1,2)))
capital_2 = capital_1 * (1 + interes / 100)
print("\n El capital final del segundo año es: " + str(round(capital_2,2)))
capital_3 = capital_2 * (1 + interes / 100)
print("\n El capital final del tercer año es: " + str(round(capital_3,2)))


"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento 
del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del 
día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que 
se le hace por no ser fresca y el coste final total."""
barras = int(input("¿Cuántas barras?: "))
precio = 3.49
descuento = 0.6
precio_final = precio * (1 - descuento)
print("\n El precio habitual de una barra de pan es: $" + str(precio))")
print ("\n El descuento es de un 60%")
coste_final = precio_final * barras
print("\n El coste totalde pan es: $" + str(round(coste_final,2)))


