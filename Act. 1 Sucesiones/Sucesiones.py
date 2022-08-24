# In VsCode download the extension "Fast Unicode Math Characters".

# The hotkeys for ₂ is \_2.

# The hotkeys for ² is \^2.

# Sucesiones:
#     -Una sucesion es una secuencia de terminos (Aₙ), donde cada uno de ellos esta asociado
#       a un valor 'n', un numero natural que nos indica que lugar ocupa el termino.

    # donde Aₙ representa el termino en el lugar n de la sucesion, con n=1, 2, 3, ...

# Como n puede ser cualquier numero natural, eso quiere decir que una sucesion tiene infinitos terminos.

# El nombre de la sucesion es una letra que usamos para identificarla, mientras que el subindice (ₓ)
#     es una variable que etiqueta los elementos deu na sicesion, indicando el lugar que ocupan.

# ¿Arreglos o listias?
    # Lo Arreglos son estructuras ded atos estatiscas, ya que hay que declarar su tamaño antesde  utilizarlos.
    # A diferencia de los Arreglos, las Listas son estructuras de datos dinamicas que pueden ir creciendo conforme se vaya requiriendo.

# En este codigo, podemos ver como declarar una lista acotada y luego ir recorriendo sus elementos uno a uno

b=[6,9,12,15,18] #Recordando que las listas de Python comienzan en 0, al indice contador se le suma 1 (+1)
for i in range(len(b)): #Con len(), contamos la lista y vamos agregando +1 al indice.
    n=i+1
    print(f'b({n})={b[i]}')

# Podemos generar los cuatro primeros terminos de esta sucesion usando el sig. codigo:
a=[]
for i in range(10):
    n=i+1
    a.append(3*n)
    print(f'a({n})={a[i]}')
#Sabiendo cual es la formula podemos agregarla a la lista e iterarla para mostrar los terminos que necesitemos.

#  Se define la sucesion (Bₙ) como 
#     Bₙ = 5*0.92ₙ
# donde queremos calcular y mostrar en pantalla desde B₁₀ hasta B₁₅. El problema es que si bien es cierto se pueden
# agregar elemenos, pero necesariamente deben existir los 9 elementos anteriores a B₁₀, de lo contrario Python arrojara error. 

# Entonces para no calcular elementos innecesarios usaremos la expresion
#     N = i + 10 Siendo '10' el numero del termino donde queremos empezar.
# con la que haremos que la lista asociada a esta sucesion inicie con B[0] y al mismo tiempo comenzamos calculando 
# B₁₀.

b=[]
#al usar rangue(6) la variable "i" asume valores enteross desde 0 hasta 5
for i in range(6): #Se agrega un termino mas para que nos tome hasta el anterior a este.
    n=i+10 #Se le suma +10 ya que es el termino donde vamos a comenzar
    b.append(5*0.92**n) #Se agrega la secuencia en la lista para poder guardarla e iterarla.
    print(f'b({n})={b[i]}')

# Considere la sucesion (3n²+7).
#     a)Los primeros 5 terminos
#     b)Los 5 terminos que vienen inmediatamente despues del decimoquinto termino.

s=[]
for i in range(5):
    n=i+1
    s.append(3*n**2+7)
    print(f'b({n})={b[i]}')

s1=[]
for i in range(5):
    n=i+15
    s1.append(3*n**2+7)
    print(f'b({n})={b[i]}')

# Considere la sucesion (Gₙ) cuyo termino general es 5n³
#     a)Los primeros 4 terminos
#     b)los 4 terminos que vienen inmediatamente despues del octavo termino
#     c)¿el termino 40.000 pertenece a la sucesion?, Verificarlo usando una ecuacion en Python y usando bucles
#         ¿Cual es mas rapido?
