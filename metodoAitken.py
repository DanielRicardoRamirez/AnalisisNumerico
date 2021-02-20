import math;

def rootuno(pcero,tol,cont):
  cont+=1
  puno= math.cos(pcero)
  pdos= math.cos(puno)
  p=pcero-(((puno-pcero)**2)/(pdos-(2*puno)+pcero))
  r=abs(p-pcero)
  if(r<tol):
      print(cont,p,r)
  else:
    print(cont,p,r)
    rootuno(p,tol,cont)

def rootdos(pcero,tol,cont):
  cont+=1
  puno= 1/math.sin(pcero)
  pdos= 1/math.sin(puno)
  p=pcero-(((puno-pcero)**2)/(pdos-(2*puno)+pcero))
  r=abs(p-pcero)
  if(r<tol):
    print(cont,p,r)
  else:
    print(cont,p,r)
    rootdos(p,tol,cont)

def roottres(pcero,tol,cont):
  cont+=1
  puno= 8/(27*((pcero**2)-(2*pcero)+(4/3)))
  pdos= 8/(27*((puno**2)-(2*puno)+(4/3)))
  if (pdos-(2*puno)+pcero) > (10**-20 ):
    p=pcero-(((puno-pcero)**2)/(pdos-(2*puno)+pcero))
  else:
    print("El divisor del metodo es muy pequeño")
    return
  r=abs(p-pcero)
  if r<tol :
    print(cont,p,r)
  else:
      
      print(cont,p,r)
      roottres(p,tol,cont)

def rootcuatro(pcero,tol,cont):
  cont+=1
  puno= (667.38 *(1 - math.exp((-0.146843*pcero))))/40
  pdos= (667.38 *(1 - math.exp((-0.146843*puno))))/40
  p=pcero-(((puno-pcero)**2)/(pdos-(2*puno)+pcero))
  r=abs(p-pcero)
  if r<tol :
    print(cont,p,r)
  else:
      print(cont,p,r)
      rootcuatro(p,tol,cont)


def rootcinco(pcero,tol,cont):
  cont+=1
  puno=5/((pcero**2)-2)
  pdos= 5/((puno**2)-2)
  p=pcero-(((puno-pcero)**2)/(pdos-(2*puno)+pcero))
  r=abs(p-pcero)
  if r<tol :
    print(cont,p,r)
  else:
      print(cont,p,r)
      rootcinco(p,tol,cont)

def menu():
  menu=-1;
  while(menu!=0):
    print("[NOTA: Este metodo solo funciona con las tolerancias 10^-8 y") 
    print("  10^-16. Si no se le es pedida la opcion el metodo termina ")
    print("  antes de que el error sea menor a 10^-8 o el denominador")
    print("  de la formula tiene el valor de 0  o se aproxima mucho")
    print(" ")
    print("           Algoritmo de Aitken")
    print("1.Raiz de cos^2(x) - x^2")
    print("2.Raiz de xsen(x) - 1")
    print("3.Raiz de x^3 - 2x^2 + 4/3x - 8/27")
    print("4.Coeficiente de caida libre ")
    print("5.Raiz de x^3 - 2x - 5")
  
    menu=int(input("Ingrese su opción: "))
    tol=-1
    
    if(menu==1):
       rootuno(1,10**-8,0)
    if(menu==2):
        while(tol!=1 and tol!=2 and tol!=3 and tol!=4):
          print("Tolerancias 10^-8(1) 10^-16(2) [LEER NOTA] ")
          tol=int(input("Ingrese su opción: "))
        if tol==1: rootdos(1,10**-8,0)
        if tol==2: rootdos(1,10**-16,0)
    if(menu==3):
      roottres(1,10**-8,0)
    if(menu==4):
      rootcuatro(14,10**-6,0)  
    if(menu==5):
      while(tol!=1 and tol!=2 and tol!=3 and tol!=4):
        print("Tolerancias 10^-8(1) 10^-16(2) [LEER NOTA] ")
        tol=int(input("Ingrese su opción: "))
      if tol==1: rootcinco(2,10**-8,0)
      if tol==2: rootcinco(2,10**-16,0)
    print(" ")
    
menu()