from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def graficar():
    plt.title("ln(1+x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    antecedentes = np.linspace(0.00005, 10, num=100)
    imagenes = []
    for i in range(len(antecedentes)):
        imagenes.append(ln(1+antecedentes[i]))
    plt.plot(antecedentes, imagenes) 
    plt.grid()
    plt.axvline()
    plt.axhline()
    plt.show()

def apTaylor(tol, a , f, val):
    taylor = 0
    i = 0

    error = abs(taylor - ln(1+val))
    while(error > 0 and i < 50):
        f_prima = f.diff(x, i)
        taylor += (f_prima.evalf(subs = {x: a})*((val-a)**i))/np.math.factorial(i)
        print("(n={}) (aprox.={}) (error={})".format(int(i), float(taylor) , error))
        error = abs(taylor - ln(1+val))
        i += 1
    return round(taylor, 9)

x = Symbol('x')
print("La mejor aprox. al valor 0.005 con el menor error posible es: {}\n".format(apTaylor(0, 0, ln(1+x), 0.005)))
print("La mejor aprox. al valor 0.0001 con el menor error posible es: {}\n".format(apTaylor(0, 0, ln(1+x), 0.0001)))
print("La mejor aprox. al valor 0.999999999 con el menor error posible es: {}\n".format(apTaylor(0, 0, ln(1+x), 0.499999999)))
graficar()