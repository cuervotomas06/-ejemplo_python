lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
num = int(input("Ingrese un numero: "))

listaMultiplos = []
listaNoMultiplos = []
for i in lista:
    if i % num == 0:
       listaMultiplos.append(i)
    else:
        listaNoMultiplos.append(i)
print("Numeros multiplos de", num, ":", listaMultiplos)
print("Numeros no multiplos de", num, ":", listaNoMultiplos)
        