import numpy as np
import math 
from time import time 
def brent(tol):
  a=0
  b=0
  f = lambda x: (x**3)-(2*x**2)+(4/3)*x-(8/27)
  i=0
  while True:
    if(i==0):
      a=1/6
      b=1
    if(i==1):
      a=c1
      b=1
    if(i>1):
      b=c1  
    c0=(a+b)/2
    F=(f(c0)/f(b))
    G=(f(c0)/f(a))
    H=(f(a)/f(b))
    c1=c0+((G*((H*(F-H)*(b-c0))-((1-F)*(b-a))))/((F-1)*(G-1)*(H-1)))
    r=c1-b
    print(i,c1,b,abs(r))
    if(abs(r)<10**-tol):
      break
    i+=1
menu=-1
while(menu!=0):
  print("ALGORITMO DE BRENT")
  print("1.Raiz de x^3 - 2x^2 + 4/3x - 8/27 con Tolerancia 10^-6")
  print("2.Raiz de x^3 - 2x^2 + 4/3x - 8/27 con Tolerancia 10^-8")
  print("3.Raiz de x^3 - 2x^2 + 4/3x - 8/27 con Tolerancia 10^-11 (Este resultado se demora aprox 990 segundos)")
  print("0. Salir")
  menu= int(input(" Ingrese una opcion: "))
  if(menu==1):
    tiempo_inicial = time() 
    brent(6)
    tiempo_final = time() 
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("El tiempo de ejecucion fue de: ", tiempo_ejecucion," segundos")
  if(menu==2):
    tiempo_inicial = time() 
    brent(8)
    tiempo_final = time() 
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("El tiempo de ejecucion fue de: ", tiempo_ejecucion," segundos")
  if(menu==3):
    tiempo_inicial = time() 
    brent(11)
    tiempo_final = time() 
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print("El tiempo de ejecucion fue de: ", tiempo_ejecucion," segundos")
  print(" ")
  print(" ")