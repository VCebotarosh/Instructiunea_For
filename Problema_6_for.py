numar=eval(input("Dati un numar:"))
suma1=0
suma2=0
suma3=0
suma4=0
suma5=0
suma6=0
produs=1
for i in range(1,numar+1):
    suma1+=i
    suma2+=(i-1)*i
    produs*=i
    suma3+=produs
    suma4+=int(str(i)+'2')
    suma5+=(i/(i+1))
    suma6+=int('2'+str(i+1))

print("Prima suma este egala cu",suma1)
print("A doua suma este egala cu",suma2)
print("A treia suma este egala cu",suma3)
print("A patra suma este egala cu",suma4)
print("A cincea suma este egala cu",round(suma5, 3))
print("A sasea suma este egala cu",1+2+suma6-int('2'+str(numar+1)))