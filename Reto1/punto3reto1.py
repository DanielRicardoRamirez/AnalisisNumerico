import time
import sympy as sym
from scipy import optimize

def f(x):
    return (x**3)-(2*x**2)+(4*x/3)-(8/27)

start_time = time.time()
print("SOL. PUNTO 1:")
raiz = optimize.brentq(f, 0, 1, xtol=2e-50)
print(raiz)
print("SOL. PUNTO 2:")
x=sym.Symbol('x')
y=sym.Symbol('y')
intersec=sym.solve([(x**2)+x*y-10, y+3*x*(y**2)-57], dict=True)
print(intersec)
print("\n {}TIEMPO EJECUCION --- %s segundos ---{}\n".format("\033[32m", "\033[0m") % (time.time() - start_time))