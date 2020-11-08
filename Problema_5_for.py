numar=int(input("Dati un numar: "))
suma=0
for i in range(1,numar):
    if((i%3==0)and(i%5==0)):
        suma+=i
    
print("Suma numerelor divizibile la 3 si 5 este:",suma)