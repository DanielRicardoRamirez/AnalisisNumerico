from scipy.interpolate import UnivariateSpline

baseImp = [4410000, 4830000, 5250000, 5670000]
quota = [1165978, 1329190, 1501474, 1682830]

interpolacionCuadratica = UnivariateSpline(baseImp, quota, k = 2)
interpolacionCubica = UnivariateSpline(baseImp, quota, k = 3)

quotaQuad = interpolacionCuadratica(5000000)
quotaCubic = interpolacionCubica(5000000)

print(quotaQuad)
print(quotaCubic)