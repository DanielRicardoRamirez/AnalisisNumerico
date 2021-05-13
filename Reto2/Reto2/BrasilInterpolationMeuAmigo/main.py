import csv
import numpy as np
#import matplotlib.pyplot as plt
 
def llenarMapa(upper):
   mapa = []
   for i in range(0,upper):
     mapa.append(0.0)
   return mapa

def imprimirLista(lista):
  for i in range (1,704):
    print(i,lista[i])

#FORTALEZA
lista = llenarMapa(704)
#Lectura de archivo de datos (Fortaleza)
with open('datos.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    for row in csv_reader:
      lista[int(row[0])] = float(row[1]);
      line_count += 1

#yx=y0+(((x-x0)/(x1-x0))*(y1-y0))
def interpolar(lista):
  for i in range (1,704):
   if(lista[i] == 0.0):
     if(lista[i+1]!= 0.0):
       lista[i]= lista[i-1]+(((i-(i-1))/((i+1)-(i-1)))*(lista[i+1]-lista[i-1]))

a = True
while (a):
  a = False #indica si ya no hay valores por interpolar
  for i in range (1,704):
    if(lista[i] == 0.0):
      a = True
  interpolar(lista)

#Guardando archivo CSV para graficar...
listaIndices = []
for i in range(len(lista)):
  listaIndices.append([i, lista[i]])

np.savetxt("InterpolacionFortaleza.csv", 
           listaIndices,
           delimiter ="\t", 
           fmt ='% s')

#ITATIRA
lista = llenarMapa(704)
#Lectura de archivo de datos (Fortaleza)
with open('Itatira.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    for row in csv_reader:
      lista[int(row[0])] = float(row[1]);
      line_count += 1

a = True
while (a):
  a = False #indica si ya no hay valores por interpolar
  for i in range (1,704):
    if(lista[i] == 0.0):
      a = True
  interpolar(lista)

#Guardando archivo CSV para graficar...
listaIndices = []
for i in range(len(lista)):
  listaIndices.append([i, lista[i]])

np.savetxt("InterpolacionItatira.csv", 
           listaIndices,
           delimiter ="\t", 
           fmt ='% s')

imprimirLista(lista)