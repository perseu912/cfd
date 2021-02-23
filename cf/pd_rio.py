import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

with open('rio_cod','r') as file:
	rio_coord = json.loads(file.read())

print(rio_coord) 

lat = [x[0] for x in rio_coord[0]]
lon = [y[1] for y in rio_coord[0]]
coord_rio = (lat,lon)

print(coord_rio)

rio = []
for i in rio_coord[0]:
	rio.append([i[1],i[0]])

rio_=[]
for i in range(len(rio)-1):
	lat_ = np.linspace(rio[i][0],rio[i+1][0],100)
	lon_ = np.linspace(rio[i][1],rio[i+1][1],100)
	for t in range(len(lat_)-1):
		rio_.append([lat_[t],lon_[t]])

print(rio_)
print(rio)


print('criando coord')
coords = list(coord_rio)
print(coords)

#print(len(coords[0]))

colunas = ['lat','lon']

rio_dp = pd.DataFrame(rio_,index=range(len(rio_)),columns=colunas)

print(rio_dp)

#rio_dp.plot(style='o')

#plt.scatter(rio_dp['lon'],rio_dp["lat"])
df = rio_dp
BBox = ((df.lon.min(), df.lon.max(),df.lat.min(), df.lat.max()))


ruh_m = plt.imread('rio_.jpg')

fig, ax = plt.subplots(figsize = (7,9))
ax.scatter(df.lon,df.lat, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('rio Sao Francisco')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
#ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')

#limitando area
ax.fill_between(df.lon,df.lat)

###/////////////////###
#plot#
# edição feita em 19/02/2021, às 15:23 

#diferencial do tempo
dt = 1e-4

#numéro de particulas(scatters) por segundo(/dt)
Np = 100
size_p = 1

#pontos iniciais
y0,x0 = -9.403, -40.51

#delimitando a localização iniciais dos scatters
_ = np.random.rand(Np)*dt
x,y = x0+_,y0+_

#vetor de velocidade do rio
vy = 0.3
vx = -0.29

#começando a iteração
print('começando a interação')
import random
Ni = 30
for i in range(Ni):
	#adicionando as velocidades de acordo com a taxa de variação do tempo'
	y = y + (vy*dt) -np.random.rand(len(y))*dt #np.random.rand(len(x)))*dt
	x = x + (vx*dt) +np.random.rand(len(x))*dt #np.random.rand(len(y)))*dt
	#limitando o espaço das particulas na dim. x
	for i_ in range(len(x)):
		for xl in df.lat:
			if x[i_] >= xl: x[i_] = xl
	#limitando o espaço das particulas na dim y.
	for i_ in range(len(y)):
		for yl in df.lon:
			if y[i_] == yl: y[i_] = yl
	print(f'plotando posições {round(i*100/Ni,2)}%[{i}/{Ni}]')
	x_,y_ = np.meshgrid(x,y)
	grad_x = np.gradient(x_,x_.size)[0] + np.random.rand(len(x))*1e-6
	grad_y = np.gradient(y_,y_.size)[0] + np.random.rand(len(y))*1e-6
	Z = np.sqrt(1/grad_y**2+1/grad_x**2)
	#print(f'{np.array(grad_x).ndim}')
	print(f'tamanho do Z eh [{Z.ndim}], de x eh [{x_.ndim}]')
	print(Z)
	#ax.contour(x_,y_,Z)
	ax.scatter(x,y,zorder=1,c='r',s=2)


###/////////////////###

plt.savefig('rio_pd.png',dpi=800)

print(max(lat),max(lon),min(lat),min(lon))


