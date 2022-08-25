# # Consideremos las sucesiones:
# a=[]#Se crea una lista para guardar los elementos de una sumatoria
# suma=0#Dejamos esta variable para guardar la posterior sumatoria
# for i in range(5): #Se tiene que considerar el termino de inicio en la sumatoria
#     m=i+23 #en el subindice se tiene que indicar en que termino inicia
#     a.append(3*m-5) #aqui se coloca la formula de la sucesion
#     suma=a[i]+suma #aqui se guarda la sumatoria de la sucesion
#     print(f'a({m})={a[i]}')
# print(f'Sumatoria ={suma}')

# b=[]
# suma2=0
# for i in range(5):
#     k=i+5
#     b.append(7*k**2)
#     suma2=b[i]+suma2
#     print(f'a({k})={b[i]}')
# print(f'Sumatoria ={suma2}')

# c=[]
# suma3=0
# for i in range(4):
#     h=i+8
#     c.append(900*0.6**h)
#     suma3=c[i]+suma3
#     print(f'c({k})={c[i]}')
# print(f'Sumatoria ={suma3}')

# d=[]
# suma4=0
# for i in range(8):
#     j=i+5
#     d.append(3*j-5)
#     suma4=d[i]+suma4
#     print(f'd({d})={d[i]}')
# print(f'Sumatoria ={suma4}')

# s1=[]
# suma=0
# for i in range(12):
#     n=i+11
#     s1.append(30*(2*i+(n-1))*6)
#     suma=s1[i]+suma
#     print(f's1({s1})={s1[i]}')
# print(f'Sumatoria ={suma}')

# Para cada una de las sig. sumatorias

# 1) i=1 n=560 (61+7i)
# 2) i=22 n=650 (45+4i)
# 3) i=1 n=54 9300*0.82ⁱ
# 4) i=21 n=80 7500*0.97ⁱ

    # a) Calcule su valor determinado en cada bucle el valor del termino con la expresion de la sucesion
    # b) Calcule su valor determinado en cada bucle el valor del termino con alguna expresion recursiva.
    # c) Calcule su valor, esta vez aplicando formula de suma aritmetica o geometrica.
 
# 1) i=1 n=560 (61+7i)
    # a)
from os import truncate


a1=[]
a_suma1=0
for i in range(560):
    n=i+1
    a1.append(61+7*n)
    a_suma1=a1[i]+a_suma1
print(f'Sumatoria 1 = {a_suma1}') #1.133.720

a2=[]
a_suma2=0
for i in range(629):
    n=i+22
    a2.append(45+4*n)
    a_suma2=a2[i]+a_suma2
print(f'Sumatoria 2 = {a_suma2}') #873.681

a3=[]
a_suma3=0
for i in range(54):
    n=i+1
    a3.append(9300*0.82**n)
    a_suma3=a3[i]+a_suma3
print(f'Sumatoria 3 = {a_suma3}') #42365.7

a4=[]
a_suma4=0
for i in range(60):
    n=i+21
    a4.append(7500*0.97**n)
    a_suma4=a4[i]+a_suma4
print(f'Sumatoria 4 = {a_suma4}') #110664.53