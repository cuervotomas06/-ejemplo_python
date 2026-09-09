lista = [int(x) for x in input("Ingrese una lista de numeros separados por comas: ").split(",")]
for i in lista:
    if i < 0:
        break
    else:
        print(i)

