p = {'pan':1.40}
h = {'huevos':2.30}
c = {'cebolla':0.85}
a = {'aceite':4.35}
q = input('Indique un articulo: ')
u = int(input('Escriba el número de unidades que desea: '))
if q in p:
    print(p[q] * u)
elif q in h:
    print(h[q])
elif q in c:
    print(c[q])
elif q in a:
    print(a[q])
else:
    print('El articulo indicado no está en la lista')