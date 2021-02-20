import numpy as np
import math 

salir = 'n'
while(salir == 'n'):
    print("\nFunciones para probar:")
    print("a) [f(x) = cos²(x)-x²]")
    print("b) [f(x) = x·sen(x)-1]")
    print("c) [f(x) = x³-2x²+(4/3)x-(8/27)]")
    print("d) [f(x) = x³-2x-5] \"Ecuacion historica\"")
    print("e) [f(x) = (9.8*68.1/x)*(1-e^(-x/68.1*10))-40] \"Ejercicio del paracaidista\"")
    opc = input("\n\tEscoja una opc -> ")

    if(opc == 'a'):
        f = lambda x: (math.cos(x)**2)-x**2
    elif(opc == 'b'): 
        f = lambda x: x*math.sin(x)-1
    elif(opc == 'c'):
        f = lambda x: (x**3)-(2*x**2)+(4/3)*x-(8/27)
    elif(opc == 'd'):
        f = lambda x: (x**3)-(2*x)-5
    elif(opc == 'e'):
        f = lambda x: (9.8*68.1/x)*(1-math.exp(-(x/68.1)*10))-40

    for i in range (4):
        a = -1
        b = 2
        if(i == 0):
            tol = 10**(-8)
        elif(i == 1):
            tol = 10**(-16)
        elif(i == 2):
            tol = 10**(-32)
        elif(i == 3):
            tol = 10**(-56)

        print("\n[Con tol=",tol,"]=================================+")
        n = 0
        tramo = abs(b-a)
        #TODO: Buscar cuál es el número máximo de iteraciones para la solución con el método de Bisección y reemplazarlo en la condición del while (...and n < numItBiseccion).
        while(tramo > tol and n < 56):
            c = b - (f(b)*(a-b))/(f(a)-f(b))
            if(np.sign(f(c))==np.sign(f(a))):
                tramo = abs(c-a)
                a = c
            else:
                tramo = abs(b-c)
                b = c
            print("n=[{}] | APROX.=[{:0.10f}] | ERROR=[{}]".format(n,c,tramo))
            n+=1
        
        print("[RESULTADO DESPUES DE {} ITERACIONES]-> {:0.10f}".format(n,c))

    salir = input("\nQuiere salir del programa? (s:si/n:no): ")
