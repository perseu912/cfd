import numpy
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D
#%matplotlib inline



def build_up_b(b, rho, dt, u, v, dx, dy):
    
    b[1:-1, 1:-1] = (rho * (1 / dt * 
                    ((u[2:,1:-1] - u[0:-2,1:-1]) / 
                     (2 * dx) + (v[1:-1,2:] - v[1:-1,0:-2]) / (2 * dy)) -
                    ((u[2:,1:-1] - u[0:-2,1:-1]) / (2 * dx))**2 -
                      2 * ((u[1:-1,2:] - u[1:-1,0:-2]) / (2 * dy) *
                           (v[2:,1:-1] - v[0:-2,1:-1]) / (2 * dx))-
                          ((v[1:-1,2:] - v[1:-1,0:-2]) / (2 * dy))**2))

    return b


def pressure_poisson(p, dx, dy, b,nit):
 
    pn = numpy.empty_like(p)
    pn = p.copy()
    
    for q in range(nit):
        pn = p.copy()
        p[1:-1, 1:-1] = (((pn[2:,1:-1] + pn[0:-2,1:-1]) * dy**2 + 
                          (pn[1:-1,2:] + pn[1:-1,0:-2]) * dx**2) /
                          (2 * (dx**2 + dy**2)) -
                          dx**2 * dy**2 / (2 * (dx**2 + dy**2)) * 
                          b[1:-1,1:-1])

        p[-1,:] = p[-2,:] # dp/dx = 0 at x = 2
        p[:,0] = p[:,1]   # dp/dy = 0 at y = 0
        p[0,:] = p[1,:]   # dp/dx = 0 at x = 0
        p[:,-1] = 0       # p = 0 at y = 2
      
    return p


def cavity_flow(nt, u, v, dt, dx, dy, p, rho, nu,ny,nx,nit):

    un = numpy.empty_like(u)
    vn = numpy.empty_like(v)
    b = numpy.zeros((ny, nx))
    
    for n in range(nt):
        un = u.copy()
        vn = v.copy()
        
        b = build_up_b(b, rho, dt, u, v, dx, dy)
        p = pressure_poisson(p, dx, dy, b,nit)
        
        u[1:-1, 1:-1] = (un[1:-1, 1:-1]-
                         un[1:-1, 1:-1] * dt / dx *
                        (un[1:-1, 1:-1] - un[0:-2,1:-1]) -
                         vn[1:-1, 1:-1] * dt / dy *
                        (un[1:-1, 1:-1] - un[1:-1,0:-2]) -
                         dt / (2 * rho * dx) * (p[2:,1:-1] - p[0:-2,1:-1]) +
                         nu * (dt / dx**2 *
                        (un[2:,1:-1] - 2 * un[1:-1,1:-1] + un[0:-2,1:-1]) +
                         dt / dy**2 *
                        (un[1:-1,2:] - 2 * un[1:-1, 1:-1] + un[1:-1,0:-2])))

        v[1:-1,1:-1] = (vn[1:-1, 1:-1] -
                        un[1:-1, 1:-1] * dt / dx *
                       (vn[1:-1, 1:-1] - vn[0:-2,1:-1]) -
                        vn[1:-1, 1:-1] * dt / dy *
                       (vn[1:-1, 1:-1] - vn[1:-1,0:-2]) -
                        dt / (2 * rho * dy) * (p[1:-1,2:] - p[1:-1,0:-2]) +
                        nu * (dt / dx**2 *
                       (vn[2:,1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2,1:-1]) +
                        dt / dy**2 *
                       (vn[1:-1,2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1,0:-2])))

        u[:,0]  = 1
        u[0,:]  = 0
        u[-1,:] = 0
        u[:,-1] = 1 # Definir velocidade na tampa da cavidade igual a 1
        v[:,0]  = 0
        v[:,-1] = 0
        v[0,:]  = 1
        v[-1,:] = 0
        
        
    return u, v, p
