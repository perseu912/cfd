from cfd import cavity_flow as cf
import numpy
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D
 
x  = numpy.linspace(-2, 2, num=21)
y  = numpy.linspace(-2, 2, num=21)



nt = 500
nit = 50
c = 4
rho = 2
nu = .1
dt = .001

#Parâmetros da malha
nx = x.size
ny = y.size
dx = (x[-1] - x[0]) / (nx - 1)
dy = (y[-1] - y[0]) / (ny - 1)

X, Y = numpy.meshgrid(x, y)

#Inicialização
u = numpy.zeros((ny, nx))
v = numpy.zeros((ny, nx))
p = numpy.zeros((ny, nx)) 
b = numpy.zeros((ny, nx))


u = numpy.zeros((nx, ny))
v = numpy.zeros((nx, ny))
p = numpy.zeros((nx, ny))
b = numpy.zeros((nx, ny))
nt = 100
u, v, p = cf(nt, u, v, dt, dx, dy, p, rho, nu,ny,nx,nit)


fig = pyplot.figure(figsize=(11,7), dpi=100)

# plotting the pressure field as a contour
pyplot.contourf(X, Y, p.T, alpha=0.5, cmap='autumn') #cm.viridis)  
pyplot.colorbar()
# plotting the pressure field outlines
pyplot.contour(X, Y, p.T, cmap='autumn')  
# plotting velocity field
pyplot.quiver(X[::2, ::2], Y[::2, ::2], u[::2, ::2].T, v[::2, ::2].T) 
pyplot.xlabel('x')
pyplot.ylabel('y');
pyplot.savefig('cfd.jpg')
