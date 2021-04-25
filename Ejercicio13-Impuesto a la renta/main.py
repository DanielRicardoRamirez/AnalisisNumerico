from scipy.interpolate import UnivariateSpline

baseImp = [4410000, 4830000, 5250000, 5670000]
quota = [1165978, 1329190, 1501474, 1682830]
tipoMarginal = [0.3886, 0.3886, 0.4102, 0.4318]

interpolacionCuadratica = UnivariateSpline(baseImp, tipoMarginal, k = 2)
interpolacionCubica = UnivariateSpline(baseImp, tipoMarginal, k = 3)

baseEjemplo = 5000000

tipoQuad = interpolacionCuadratica(baseEjemplo)
tipoCubic = interpolacionCubica(baseEjemplo)

print(tipoQuad*100, '%')
print(tipoCubic*100, '%')

print(((baseEjemplo-baseImp[2])*tipoQuad)+quota[2])
print(((baseEjemplo-baseImp[2])*tipoCubic)+quota[2])