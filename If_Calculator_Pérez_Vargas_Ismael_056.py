#Elabora un programa aue sea una calculadora simple con las 4 operaciones siguientes:
#Suma, resta multiplicación y división.
#El programa nos pedira 2 numeros por teclado y despues nos pedira un operador.
#Haz la calculadora con if else.

num = float(input("Introduce numero: "))
num2 = float(input("Introduce numero: "))
operad = input("Introduce operador: ")
suma = "+"
resta = "-"
multiplicación = "*"
división = "/"
if operad == suma:
    print("Resultado suma: ",num + num2)
elif operad == resta:
    print("Resultado resta: ",num - num2)   
elif operad == multiplicación:
    print("Resultado multiplicación: ",num * num2)
elif operad == división:
    print("Resultado división: ",num / num2)    
else:
    print("No existe tal operador")

input()