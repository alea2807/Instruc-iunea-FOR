#problema 5
num=eval(input("Introduceti num: "))
suma=0
for i in range(1,num+1):
    if ((i%3==0 and i%5==0)):
        suma+=i
print(suma)