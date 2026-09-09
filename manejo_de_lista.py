lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
num = int(input("Ingrese un numero: "))
print("Numeros multiplos de:", num)
for i in lista:
    if i % num == 0:
        print(i)
        
       