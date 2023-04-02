'''num = 1

while num <= 6:
    print(num)
    num += 1
    
print("Gracias por utilizar el programa.")'''

'''suma = 0 
 
num = int(input("Ingrese un numero -> "))

while num != 0:
    suma += num
    
    num = int(input("Ingrese un numero -> "))
    
    if num == 0:
        break

print(f"Suma total: {suma}")'''


x = 1
n = int(input("Cuantas compras necesita realizar -> "))
suma = 0
while x <= n:
    valor = float(input("Ingrese el valor -> "))
    suma = suma+valor
    x = x+1

print(f"La suma de los valores es: {suma}")
