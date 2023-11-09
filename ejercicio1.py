d = {'Euro':'€', 'Dollar':'$','Yen':'¥'}
j = input('Escriba una divisa ')
if j in d:
    print(d[j])
else:
    print('La divisa no corresponde con las nuestras.')
