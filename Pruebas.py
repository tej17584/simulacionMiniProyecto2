####################################################################
# Alejandro Tejada 17584
# Diego Sevilla 17238
####################################################################
# Curso: Modelación y Simulación
# Programa: pruebas.py
# Propósito: Programa para mini proyecto
# Fecha: 09/2020
####################################################################
# %%
import numpy as np
import math
import random
import matplotlib.pyplot as plt


def pseudo(a, m):
    def inner_pseudo(xo, n):
        items = list(range(n))
        items[0] = xo

        for i in range(1, n):
            items[i] = (a*items[i-1]) % m

        return [i/float(m) for i in items]
    return inner_pseudo


F = {
    0.2: lambda x: x**2,
    0.5: lambda x: x**3,
    0.8: lambda x: x**4,
    1: lambda x: x**5,
}

F2 = {
    0.2: 'EVENTOA',
    0.5: 'EVENTOB',
    0.8: 'EVENTOC',
    1: 'EVENTOD',
}
# se crean los pseudos
mi_pseudo = pseudo(m=2**31-1, a=7**5)
# se crean mis randoms
mis_randoms = mi_pseudo(xo=5, n=1)
print(mis_randoms)
plt.style.use('seaborn-white')

data = np.random.randn(1000)
plt.hist(data);
# Keys
Fprob = [0]
Fprob += list(F.keys())
for x in range(0, 1):
    num = random.random()
    for i in range(0, len(Fprob)-1):
        if(Fprob[i] <= num < Fprob[i+1]):
            print(Fprob[i+1])
            print(F[Fprob[i+1]])


